content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = '''            import json
            raw = message.content[0].text.strip()
            # JSON цэвэрлэх
            if raw.startswith("```"):
                raw = raw.split("```")[1]
                if raw.startswith("json"):
                    raw = raw[4:]
            raw = raw.strip()
            try:
                result = json.loads(raw)
            except:
                result = {"error": raw}'''

new = '''            import json, re
            raw = message.content[0].text.strip()
            # JSON цэвэрлэх
            raw = re.sub(r"^```json\s*", "", raw)
            raw = re.sub(r"^```\s*", "", raw)
            raw = re.sub(r"\s*```$", "", raw)
            raw = raw.strip()
            # JSON эхлэх хэсгийг олох
            start = raw.find("{")
            end = raw.rfind("}") + 1
            if start >= 0 and end > start:
                raw = raw[start:end]
            try:
                result = json.loads(raw)
            except Exception as je:
                result = {"error": f"JSON parse алдаа: {str(je)}", "raw": raw[:500]}'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")