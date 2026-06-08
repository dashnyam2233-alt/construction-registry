import os, sys, json, time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
sys.path.insert(0, ".")
import django
django.setup()

from apps.public.models import Tender
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import re

CONSTRUCTION_KEYWORDS = [
    "барилга", "засвар", "угсралт", "зураг төсөл", "бетон", "хучилт",
    "дулаалга", "цахилгаан", "сантехник", "хаалга", "цонх", "дээвэр",
    "суурь", "төлөвлөлт", "зам", "гүүр", "усан хангамж", "халаалт",
    "өргөтгөх", "шинэчлэх", "их засвар", "дотоод засал"
]

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
tenders = []

def parse_rows():
    rows = driver.find_elements(By.CSS_SELECTOR, "table tr")
    count = 0
    for row in rows:
        try:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) < 3:
                continue
            try:
                link = row.find_element(By.CSS_SELECTOR, "a.tender-name")
                href = link.get_attribute("href") or ""
                title = link.text.strip()
            except:
                href = ""
                title = ""
            if not title or len(title) < 5 or not href:
                continue
            lines = [l.strip() for l in row.text.split("\n") if l.strip()]
            org = next((l.replace("Захиалагчийн нэр:", "").strip() for l in lines if "захиалагч" in l.lower()), "")
            price = next((l for l in lines if "₮" in l), "")
            method = next((l.replace("ХАА-ны журам:", "").strip() for l in lines if "журам" in l.lower() or "арга" in l.lower()), "")
            # Deadline — Cell 0-с авах (хүлээн авах огноо)
            # Cell 0: "11:00\n2026-06\n26" хэлбэртэй
            deadline = ""
            try:
                cell0 = cells[0].text.strip()
                # 2026-06 болон 26 гэсэн хэлбэрийг нэгтгэх
                parts = cell0.split("\n")
                # "2026-06" болон "26" хайх
                year_mon = ""
                day = ""
                for p in parts:
                    p = p.strip()
                    if re.match(r"\d{4}-\d{2}$", p):
                        year_mon = p
                    elif re.match(r"^\d{1,2}$", p):
                        day = p.zfill(2)
                if year_mon and day:
                    deadline = f"{year_mon}-{day}"
                else:
                    # Fallback: огноо хэлбэрээр хайх
                    m = re.search(r"(\d{4}-\d{2}-\d{2})", cell0)
                    if m:
                        deadline = m.group(1)
            except:
                deadline = ""
            tender_code = next((l for l in lines if re.match(r"[А-ЯӨҮ]+/\d+", l)), "")
            tenders.append({"title": title, "organization": org, "price": price,
                            "deadline": deadline, "method": method,
                            "tender_code": tender_code, "url": href})
            count += 1
        except:
            continue
    return count

try:
    print("Тендер татаж байна...")
    driver.get("https://user.tender.gov.mn/mn/invitation")
    time.sleep(6)

    page = 1
    while page <= 10:
        count = parse_rows()
        print(f"  Хуудас {page}: {count} тендер")
        try:
            first_title = driver.find_element(By.CSS_SELECTOR, "a.tender-name").text
            candidates = driver.find_elements(By.XPATH, "//a[contains(text(),'»')]")
            if not candidates:
                candidates = driver.find_elements(By.XPATH, f"//a[text()='{page + 1}']")
            if not candidates:
                break
            candidates[0].click()
            time.sleep(5)
            try:
                WebDriverWait(driver, 10).until(
                    lambda d: d.find_element(By.CSS_SELECTOR, "a.tender-name").text != first_title
                )
                page += 1
            except:
                break
        except:
            break
finally:
    driver.quit()

# Django-д хадгалах
added = 0
for item in tenders:
    text = (item.get("title", "") + " " + item.get("method", "")).lower()
    is_construction = any(kw in text for kw in CONSTRUCTION_KEYWORDS)
    _, created = Tender.objects.get_or_create(
        url=item["url"],
        defaults={
            "title": item.get("title", "")[:500],
            "organization": item.get("organization", "")[:300],
            "price": item.get("price", "")[:100],
            "deadline": item.get("deadline", "")[:20],
            "method": item.get("method", "")[:200],
            "tender_code": item.get("tender_code", "")[:100],
            "is_construction": is_construction,
        }
    )
    if created:
        added += 1
# Ангилал шинэчлэх
from apps.public.models import Tender as T2
CATEGORIES = {

    "construction": [
        "барилга угсралт", "барилга байгууламж барих", "барилгын ажил",
        "цутгалт", "суурь", "өргөтгөх барилга", "орон сууц барих",
        "сургууль барих", "эмнэлэг барих", "цэцэрлэг барих",
    ],
    "repair": [
        "их засвар", "дотоод засал", "гадаад засал", "засварын ажил",
        "засварчдын", "шинэчлэх ажил", "будагдах",
    ],
    "design": [
        "зураг төсөл", "зураг төслийн", "ded", "fed", "тэзү",
        "геодезийн", "геологийн", "архитектурын зураг",
    ],
    "road": [
        "авто зам", "хатуу хучилттай зам", "гүүр барих",
        "замын хучилт", "тротуар", "талбай хучих",
    ],
    "engineering": [
        "цахилгааны ажил", "сантехникийн ажил", "дулааны шугам",
        "халаалтын систем", "агааржуулалтын", "усан хангамжийн шугам",
        "лифт", "шугам хоолой угсралт",
    ],
    "material": [
        "материал нийлүүлэх", "бараа нийлүүлэх", "тоосго",
        "цемент", "арматур нийлүүлэх", "барилгын материал",
    ],
    "equipment": [
        "тоног төхөөрөмж", "машин механизм", "техник хэрэгсэл",
        "кран", "экскаватор",
    ],
    "consulting": [
        "зөвлөх үйлчилгээ", "судалгааны ажил", "үнэлгээний",
        "техникийн хяналт", "аудит",
    ],
    "service": ["үйлчилгээ"],
}
for t in T2.objects.filter(category="other"):
    text = (t.title + " " + t.method).lower()
    for cat, kws in CATEGORIES.items():
        if any(k in text for k in kws):
            t.category = cat
            t.is_construction = cat in ["construction","repair","design","road","engineering"]
            t.save(update_fields=["category","is_construction"])
            break
print("✅ Ангилал шинэчлэгдлээ")
print(f"\n✅ Шинэ тендер нэмэгдсэн: {added}")
print(f"📊 Нийт DB-д: {Tender.objects.count()}")