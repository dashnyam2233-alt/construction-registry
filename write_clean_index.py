html = """{% extends "admin/base_site.html" %}
{% load i18n %}

{% block content %}
  <div style="max-width: 980px;">
    <h1 style="font-weight: 500; margin-bottom: 18px;">Сайтын удирдлага</h1>

    <!-- Баннер / Мэдээллийн талбар -->
    <div style="border:1px solid #e5e7eb;border-radius:10px;padding:18px;margin-bottom:18px;background:#fff;">
      <div style="font-size:18px;font-weight:600;margin-bottom:6px;">Баннер / Мэдээллийн талбар</div>
      <div style="color:#6b7280;margin-bottom:8px;">Энд компани байгуулагуудын баннер, зар, мэдээлэл байрлуулна.</div>
      <div style="color:#9ca3af;font-size:13px;">(Admin дээр баруун талд баннер + чат байнга харагдана)</div>
      <div style="margin-top:12px;display:flex;gap:10px;flex-wrap:wrap;">
        <a href="/admin/public/banner/" class="button default">Баннер удирдах</a>
        <a href="/admin/public/publicpost/" class="button">Пост / Чат удирдах</a>
      </div>
    </div>

    <!-- Үнийн мэдээлэл -->
    <div style="border:1px solid #e5e7eb;border-radius:10px;padding:18px;margin-bottom:18px;background:#fff;">
      <div style="font-size:18px;font-weight:600;margin-bottom:12px;">💰 Үнийн мэдээлэл</div>
      <div style="display:flex;gap:10px;flex-wrap:wrap;">
        <a href="/admin/public/materialprice/?category__startswith=mat_" class="button">🧱 Материал</a>
        <a href="/admin/public/materialprice/?category__startswith=labor_" class="button">👷 Цалин</a>
        <a href="/admin/public/materialprice/?category__startswith=transport_" class="button">🚛 Тээвэр</a>
        <a href="/admin/public/materialprice/?category__startswith=machine_" class="button">🔩 Машин механизм</a>
        <a href="/admin/public/materialprice/?category__startswith=other_" class="button">📦 Бусад</a>
        <a href="/admin/public/materialprice/add/" class="button default">+ Үнэ нэмэх</a>
      </div>
    </div>

  </div>

  <script>
    document.addEventListener("DOMContentLoaded", function () {
      document.querySelectorAll('a.changelink').forEach(function (a) {
        a.textContent = "Бөлөглөх";
      });
    });
  </script>
{% endblock %}"""

with open("templates/admin/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("OK")