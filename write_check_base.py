path = r"templates\admin\base_site.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
print(f"Нийт урт: {len(content)}")
print(f"\n--- Эхний 500 тэмдэгт ---")
print(content[:500])
print(f"\n--- Сүүлийн 500 тэмдэгт ---")
print(content[-500:])