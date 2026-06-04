# base_site.html-аас sidebar болон price nav устгах
content = open("templates/admin/base_site.html", "r", encoding="utf-8").read()

import re

# Sidebar устгах
old = """{% block footer %}
  {{ block.super }}
  {% if request.user.is_authenticated %}
    <aside style="position:fixed;top:90px;right:0;width:280px;height:calc(100vh - 90px);overflow-y:auto;background:#fff;border-left:0.5px solid #e2e8f0;padding:14px;z-index:100;">
      {% registry_admin_sidebar %}
    </aside>
  {% endif %}
{% endblock %}"""

new = """{% block footer %}
  {{ block.super }}
{% endblock %}"""

if old in content:
    content = content.replace(old, new, 1)
    print("OK — sidebar устгагдлаа")
else:
    print("sidebar NOT FOUND")

# Price nav устгах
content = re.sub(r'<style>\s*\.price-nav.*?</style>\s*', '', content, flags=re.DOTALL)
content = re.sub(r'{% if request\.user\.is_authenticated %}\s*<div class="price-nav">.*?</div>\s*{% endif %}\s*', '', content, flags=re.DOTALL)

open("templates/admin/base_site.html", "w", encoding="utf-8").write(content)
print("OK — base_site.html цэвэрлэгдлээ")

# index.html анхны байдалд буцаах
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
{% endblock %}"""

with open("templates/admin/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("OK — index.html цэвэрлэгдлээ")

# _sidebar_registry.html-аас үнийн хэсэг устгах
content2 = open("templates/admin/_sidebar_registry.html", "r", encoding="utf-8").read()
content2 = re.sub(r'<!-- Үнийн мэдээлэл -->.*?</div>\s*\n', '', content2, flags=re.DOTALL)
open("templates/admin/_sidebar_registry.html", "w", encoding="utf-8").write(content2)
print("OK — sidebar_registry цэвэрлэгдлээ")