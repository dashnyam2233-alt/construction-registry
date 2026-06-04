import re
content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = '''    return render(request, "registry/budget_calculator.html", {
        "result": result,
        "error": error,
        "post_data": request.POST,
        "display_name": get_display_name(request.user),
    })'''

new = '''    import json as _json
    result_json = _json.dumps(result, ensure_ascii=False) if result else "{}"
    return render(request, "registry/budget_calculator.html", {
        "result": result,
        "result_json": result_json,
        "error": error,
        "post_data": request.POST,
        "display_name": get_display_name(request.user),
    })'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK — view шинэчлэгдлээ")
else:
    print("NOT FOUND")