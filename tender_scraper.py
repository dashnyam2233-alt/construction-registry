import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time, json, re

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
            if not title or len(title) < 5:
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
    print("Сайт нээж байна...")
    driver.get("https://user.tender.gov.mn/mn/invitation")
    time.sleep(6)

    page = 1
    while page <= 30:
        print(f"Хуудас {page} уншиж байна...")
        count = parse_rows()
        print(f"  ✅ {count} тендер (нийт: {len(tenders)})")

        try:
            first_title = driver.find_element(By.CSS_SELECTOR, "a.tender-name").text
            candidates = driver.find_elements(By.XPATH, "//a[contains(text(),'»')]")
            if not candidates:
                candidates = driver.find_elements(By.XPATH, f"//a[text()='{page + 1}']")
            if not candidates:
                print("  Дараах товч байхгүй — дууслаа")
                break

            driver.execute_script("arguments[0].scrollIntoView(true);", candidates[0])
            time.sleep(1)
            candidates[0].click()
            time.sleep(6)

            try:
                WebDriverWait(driver, 12).until(
                    lambda d: d.find_element(By.CSS_SELECTOR, "a.tender-name").text != first_title
                )
                print(f"  → Хуудас {page+1} руу шилжлээ")
                page += 1
            except:
                print("  Хуудас өөрчлөгдсөнгүй — дууслаа")
                break

        except Exception as e:
            print(f"  Алдаа: {e}")
            break

finally:
    driver.quit()

with open("tenders.json", "w", encoding="utf-8") as f:
    json.dump(tenders, f, ensure_ascii=False, indent=2)

print(f"\n✅ Нийт {len(tenders)} тендер → tenders.json")