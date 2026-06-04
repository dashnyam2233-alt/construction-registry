from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

driver = webdriver.Chrome(options=options)

# Зөв URL туршина
urls = [
    "https://user.tender.gov.mn/mn/invitation",
    "https://user.tender.gov.mn/mn/invitation?page=2",
    "https://user.tender.gov.mn/mn/invitation?page=1&perpage=20",
]

for url in urls:
    driver.get(url)
    time.sleep(5)
    rows = driver.find_elements(By.CSS_SELECTOR, "table tr")
    links = driver.find_elements(By.CSS_SELECTOR, "a.invitation-title, .tender-name a, table tr a")
    print(f"URL: {url}")
    print(f"  → Одоогийн URL: {driver.current_url}")
    print(f"  → TR тоо: {len(rows)}, Link тоо: {len(links)}")
    if rows:
        print(f"  → Эхний мөр: {rows[1].text[:100] if len(rows)>1 else ''}")
    print()

driver.quit()