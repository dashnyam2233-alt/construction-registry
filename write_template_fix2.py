path = r"apps\registry\templates\registry\budget_calculator.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Эхний мөрийг шалгах
first_line = content.split('\n')[0]
print("Эхний мөр:", first_line)

# humanize байгаа эсэх
if "humanize" in content:
    print("humanize template-д байна")
else:
    print("humanize БАЙХГҮЙ - нэмнэ")

# intcomma байгаа эсэх  
count = content.count("intcomma")
print(f"intcomma тоо: {count}")

# Засах — {% load static humanize %} болгох
old = "{% load static %}"
new = "{% load static humanize %}"

if old in content:
    content = content.replace(old, new, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXED - humanize нэмэгдлээ")
elif "{% load static humanize %}" in content:
    print("Аль хэдийн байна - OK")
else:
    print("load static олдсонгүй")