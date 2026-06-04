content = open("apps/registry/templates/registry/budget_calculator.html", "r", encoding="utf-8").read()

# Form submit-д validation-г disable хийх
old = 'document.getElementById("main-form") && document.getElementById("main-form").addEventListener("submit", function() {'
new = '''document.getElementById("main-form") && document.getElementById("main-form").addEventListener("submit", function(e) {
  // Hidden field-үүдийн validation-г алгасах
  const inputs = document.querySelectorAll("input[type=number]");
  inputs.forEach(function(inp) { inp.removeAttribute("required"); inp.removeAttribute("min"); });'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")
    idx = content.find("main-form")
    print(repr(content[idx:idx+200]))