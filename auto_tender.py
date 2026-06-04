import os, sys, json, time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
sys.path.insert(0, ".")
import django
django.setup()

from apps.public.models import Tender
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import re

CONSTRUCTION_KEYWORDS = [
    "барилга", "засвар", "угсралт", "зураг төсөл", "бетон", "хучилт",
    "дулаалга", "цахилгаан", "сантехник", "хаалга", "цонх", "дээвэр",
    "суурь", "төлөвлөлт", "зам", "гүүр", "усан хангамж", "халаалт",
    "өргөтгөх", "шинэчлэх", "их засвар", "дотоод засал"
]

options = uc.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = uc.Chrome(options=options, headless=False)
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
            deadline = ""
            for l in lines:
                m = re.search(r"\d{4}-\d{2}-\d{2}", l)
                if m:
                    deadline = m.group()
                    break
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
    "construction": ["барилга","угсралт","цутгалт","бетон","суурь","хана","дээвэр","орон сууц","өргөтгөх"],
    "repair": ["засвар","их засвар","шинэчлэх","дотоод засал","гадаад засал","будаг"],
    "design": ["зураг төсөл","зураг","төсөл","ded","fed","тэзү","геодези","геологи","архитектур"],
    "road": ["зам","гүүр","хучилт","авто зам","талбай","тротуар"],
    "engineering": ["цахилгаан","сантехник","дулаан","халаалт","агааржуулалт","усан хангамж","лифт","хоолой"],
    "material": ["материал","тоосго","цемент","арматур","хайрга","бараа","нийлүүлэлт"],
    "equipment": ["тоног төхөөрөмж","машин","механизм","техник","кран","экскаватор"],
    "consulting": ["зөвлөх","судалгаа","үнэлгээ","хяналт","аудит"],
    "service": ["үйлчилгээ","ажил"],
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