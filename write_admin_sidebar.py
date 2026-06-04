# admin_sidebar.py шинэчлэх
sidebar_tag = """from django import template
from apps.public.models import Banner, PublicPost, Ad, SliderAd

register = template.Library()

@register.inclusion_tag("admin/_sidebar_registry.html")
def registry_admin_sidebar():
    banners = list(
        Banner.objects.filter(is_active=True).order_by("sort_order", "-created_at")[:6]
    )
    posts = list(
        PublicPost.objects.filter(is_published=True)
        .select_related("author")
        .order_by("-created_at")[:8]
    )
    ads = list(
        Ad.objects.filter(status="active").order_by("-created_at")[:6]
    )
    slider_ads = list(
        SliderAd.objects.filter(is_active=True).order_by("sort_order")[:5]
    )
    ads_total = Ad.objects.count()
    ads_active = Ad.objects.filter(status="active").count()
    return {
        "sidebar_banners": banners,
        "sidebar_posts": posts,
        "sidebar_ads": ads,
        "slider_ads": slider_ads,
        "ads_total": ads_total,
        "ads_active": ads_active,
    }
"""

with open("apps/registry/templatetags/admin_sidebar.py", "w", encoding="utf-8") as f:
    f.write(sidebar_tag)
print("OK — admin_sidebar.py")

# _sidebar_registry.html шинэчлэх
sidebar_html = """<style>
.cr-stat-grid{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-bottom:12px;}
.cr-stat{background:#f0faf4;border:0.5px solid #c0e8d0;border-radius:7px;padding:8px;text-align:center;}
.cr-stat-n{font-size:18px;font-weight:700;color:#1a7a42;}
.cr-stat-l{font-size:10px;color:#64748b;margin-top:1px;}
.cr-box{margin-bottom:16px;}
.cr-box__title{font-size:11px;font-weight:600;color:#64748b;letter-spacing:0.05em;text-transform:uppercase;margin-bottom:8px;display:flex;align-items:center;justify-content:space-between;}
.cr-box__title a{font-size:10px;color:#2f6477;font-weight:400;text-transform:none;}
.cr-item{display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:0.5px solid #f1f5f9;}
.cr-item:last-child{border-bottom:none;}
.cr-thumb{width:36px;height:36px;border-radius:6px;background:#f8fafc;border:0.5px solid #e2e8f0;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0;overflow:hidden;}
.cr-thumb img{width:100%;height:100%;object-fit:cover;}
.cr-item__title{font-size:12px;font-weight:500;color:#1e293b;line-height:1.3;}
.cr-item__meta{font-size:10px;color:#94a3b8;margin-top:1px;}
.cr-empty{font-size:12px;color:#94a3b8;padding:8px 0;text-align:center;}
.cr-chat{padding:6px 0;border-bottom:0.5px solid #f1f5f9;}
.cr-chat:last-child{border-bottom:none;}
.cr-chat__title{font-size:12px;font-weight:500;color:#1e293b;line-height:1.3;}
.cr-chat__meta{font-size:10px;color:#94a3b8;margin-top:2px;}
.cr-add-btn{display:block;width:100%;padding:6px;background:#f0faf4;border:0.5px dashed #c0e8d0;border-radius:6px;font-size:11px;color:#1a7a42;text-align:center;text-decoration:none;margin-top:6px;}
.cr-add-btn:hover{background:#e0f4e8;}
.cr-ad-cat{display:inline-block;background:#fef3c7;color:#854f0b;font-size:9px;padding:1px 5px;border-radius:10px;}
.cr-slider-item{display:flex;align-items:center;gap:8px;padding:5px 0;border-bottom:0.5px solid #f1f5f9;}
.cr-slider-item:last-child{border-bottom:none;}
.cr-slider-dot{width:6px;height:6px;background:#f59e0b;border-radius:50%;flex-shrink:0;}
</style>

<!-- Статистик -->
<div class="cr-stat-grid">
  <div class="cr-stat">
    <div class="cr-stat-n">{{ ads_active }}</div>
    <div class="cr-stat-l">Идэвхтэй зар</div>
  </div>
  <div class="cr-stat">
    <div class="cr-stat-n">{{ ads_total }}</div>
    <div class="cr-stat-l">Нийт зар</div>
  </div>
</div>

<!-- Зарууд -->
<div class="cr-box">
  <div class="cr-box__title">
    <span>📢 Сүүлийн зарууд</span>
    <a href="/admin/public/ad/">Бүгд харах</a>
  </div>
  <div class="cr-list">
    {% for ad in sidebar_ads %}
    <div class="cr-item">
      <div class="cr-thumb">
        {% if ad.category == 'house' %}🏠
        {% elif ad.category == 'material' %}🧱
        {% elif ad.category == 'worker' %}👷
        {% elif ad.category == 'repair' %}🔧
        {% else %}📢{% endif %}
      </div>
      <div>
        <div class="cr-item__title">{{ ad.title|truncatechars:30 }}</div>
        <div class="cr-item__meta">
          <span class="cr-ad-cat">{{ ad.get_category_display }}</span>
          · {{ ad.created_at|date:"m-d" }}
        </div>
      </div>
    </div>
    {% empty %}
    <div class="cr-empty">Зар байхгүй байна.</div>
    {% endfor %}
  </div>
  <a href="/admin/public/ad/add/" class="cr-add-btn">+ Зар нэмэх</a>
</div>

<!-- Урсдаг зар -->
<div class="cr-box">
  <div class="cr-box__title">
    <span>🔄 Урсдаг зарууд</span>
    <a href="/admin/public/sliderad/">Засах</a>
  </div>
  <div>
    {% for s in slider_ads %}
    <div class="cr-slider-item">
      <div class="cr-slider-dot"></div>
      <div>
        <div class="cr-item__title">{{ s.title|truncatechars:28 }}</div>
        <div class="cr-item__meta">Эрэмбэ: {{ s.sort_order }}</div>
      </div>
    </div>
    {% empty %}
    <div class="cr-empty">Урсдаг зар байхгүй.</div>
    {% endfor %}
  </div>
  <a href="/admin/public/sliderad/add/" class="cr-add-btn">+ Урсдаг зар нэмэх</a>
</div>

<!-- Баннер -->
<div class="cr-box">
  <div class="cr-box__title">
    <span>🖼️ Баннерууд</span>
    <a href="/admin/public/banner/">Бүгд</a>
  </div>
  <div class="cr-list">
    {% for b in sidebar_banners %}
    <div class="cr-item">
      <div class="cr-thumb">
        {% if b.display_image_url %}
          <img src="{{ b.display_image_url }}" alt="{{ b.title }}">
        {% else %}AD{% endif %}
      </div>
      <div>
        <div class="cr-item__title">{{ b.title|default:"Баннер"|truncatechars:25 }}</div>
        <div class="cr-item__meta">Эрэмбэ: {{ b.sort_order }}</div>
      </div>
    </div>
    {% empty %}
    <div class="cr-empty">Баннер байхгүй байна.</div>
    {% endfor %}
  </div>
  <a href="/admin/public/banner/add/" class="cr-add-btn">+ Баннер нэмэх</a>
</div>

<!-- Мэдээ/Чат -->
<div class="cr-box">
  <div class="cr-box__title">
    <span>📰 Сүүлийн мэдээ</span>
    <a href="/admin/public/publicpost/">Бүгд</a>
  </div>
  <div class="cr-chatlist">
    {% for p in sidebar_posts %}
    <div class="cr-chat">
      <div class="cr-chat__title">{{ p.title|truncatechars:35 }}</div>
      <div class="cr-chat__meta">
        {{ p.created_at|date:"Y-m-d H:i" }}
        {% if p.author %} · {{ p.author }}{% endif %}
      </div>
    </div>
    {% empty %}
    <div class="cr-empty">Мэдээ байхгүй байна.</div>
    {% endfor %}
  </div>
  <a href="/admin/public/publicpost/add/" class="cr-add-btn">+ Мэдээ нэмэх</a>
</div>
"""

with open("templates/admin/_sidebar_registry.html", "w", encoding="utf-8") as f:
    f.write(sidebar_html)
print("OK — _sidebar_registry.html")