content = open("apps/registry/templates/registry/budget_calculator.html", "r", encoding="utf-8").read()

old = '<a href="/budget/excel/?data={{ result|urlencode }}" class="download-btn" id="excel-btn">📥 Excel татах</a>'
new = '<button onclick="downloadExcel()" class="download-btn" id="excel-btn">📥 Excel татах</button>'

if old in content:
    content = content.replace(old, new, 1)
    print("OK — button солигдлоо")
else:
    print("NOT FOUND")

# JS нэмэх
old_js = '</script>'
new_js = '''
function downloadExcel() {
  const data = {{ result_json|safe }};
  const form = document.createElement("form");
  form.method = "POST";
  form.action = "/budget/excel/";
  const csrf = document.createElement("input");
  csrf.type = "hidden";
  csrf.name = "csrfmiddlewaretoken";
  csrf.value = "{{ csrf_token }}";
  form.appendChild(csrf);
  const inp = document.createElement("input");
  inp.type = "hidden";
  inp.name = "data";
  inp.value = JSON.stringify(data);
  form.appendChild(inp);
  document.body.appendChild(form);
  form.submit();
}
</script>'''

content = content.replace(old_js, new_js, 1)
open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8").write(content)
print("OK — JS нэмэгдлээ")