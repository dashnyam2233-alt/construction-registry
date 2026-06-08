path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\templates\registry\budget_calculator.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1898-р мөрийн дараах } хаалтын ард функцийн нэр нэмэх
old = """  form.submit();
}
  if (!showLen && !count) {"""

new = """  form.submit();
}

function submitEngForm2() {
  if (!showLen && !count) {"""

content = content.replace(old, new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Засагдлаа")