import json
import hashlib
import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.cache import cache
from django.conf import settings
import anthropic

def set_language(request, lang_code):
    if lang_code in ["mn", "en"]:
        request.session["language"] = lang_code
        request.session.modified = True
    from django.shortcuts import redirect
    next_url = request.GET.get("next", "/")
    return redirect(next_url)

@csrf_exempt
@require_POST
def translate_content(request):
    try:
        data = json.loads(request.body)
        texts = data.get("texts", [])
        target_lang = data.get("target", "en")

        if not texts:
            return JsonResponse({"error": "No texts"}, status=400)

        combined = target_lang + "".join(texts)
        cache_key = "trans_" + hashlib.md5(combined.encode()).hexdigest()
        cached = cache.get(cache_key)
        if cached:
            return JsonResponse({"translations": cached, "cached": True})

        lang_instruction = (
            "Translate the following Mongolian construction industry texts to English."
            if target_lang == "en"
            else "Translate the following English construction industry texts to Mongolian."
        )
        texts_json = json.dumps(texts, ensure_ascii=False)

        client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": f"{lang_instruction}\nReturn ONLY a JSON array of translated strings, same order as input.\nNo explanations, no markdown, no code blocks, just the raw JSON array.\n\nInput texts:\n{texts_json}"
            }]
        )

        response_text = message.content[0].text.strip()
        # Markdown code block арилгах
        response_text = re.sub(r'^```[a-z]*\n?', '', response_text)
        response_text = re.sub(r'\n?```$', '', response_text)
        response_text = response_text.strip()

        translations = json.loads(response_text)
        cache.set(cache_key, translations, 60 * 60 * 24)
        return JsonResponse({"translations": translations, "cached": False})

    except json.JSONDecodeError as e:
        return JsonResponse({"error": f"JSON parse error: {e}"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)