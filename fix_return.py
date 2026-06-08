path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\templates\registry\budget_calculator.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old = """      form.submit();
    }
    return;
  }
  if(from === 1 && !btype && !document.getElementById('hidden_eng_type').value) {"""

new = """      form.submit();
      return;
    }
  }
  if(from === 1 && !btype && !document.getElementById('hidden_eng_type').value) {"""

if old in content:
    content = content.replace(old, new)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Засагдлаа")
else:
    print("❌ Олдсонгүй — текст өөр байна")