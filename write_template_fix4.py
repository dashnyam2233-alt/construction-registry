path = r"apps\registry\templates\registry\budget_calculator.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# intcomma-г бүгдийг устгаж floatformat:0 болгох
import re
content = re.sub(r'\|floatformat:0\|intcomma', '|floatformat:0', content)

# </table> дараа JavaScript нэмэх
old = '</script>\n</body>'
new = '''</script>
<script>
// Тоог 3 оронгоор таслалтай болгох
document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll("td.r, .val, .grand-box .val").forEach(function(el) {
    var text = el.textContent.trim();
    if (text.endsWith("₮")) {
      var num = text.replace("₮","").replace(/,/g,"").trim();
      var n = parseFloat(num);
      if (!isNaN(n)) {
        el.textContent = n.toLocaleString("en-US").replace(/\./g,"") + "₮";
      }
    }
  });
});
</script>
</body>'''

if old in content:
    content = content.replace(old, new, 1)
    print("OK - JS нэмэгдлээ")
else:
    print("NOT FOUND")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("DONE")