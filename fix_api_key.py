content = open("config/settings.py", "r", encoding="utf-8").read()

old = 'ANTHROPIC_API_KEY = "sk-ant-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"'
new = 'ANTHROPIC_API_KEY = "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"'

if old in content:
    content = content.replace(old, new, 1)
    open("config/settings.py", "w", encoding="utf-8").write(content)
    print("OK — засагдлаа")
else:
    print("NOT FOUND")