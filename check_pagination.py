from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

driver = webdriver.Chrome(options=options)
driver.get("https://user.tender.gov.mn/mn/invitation")
time.sleep(5)

# Pagination товч хайх
btns = driver.find_elements(By.CSS_SELECTOR, "a, button")
print("Pagination холбоостой товчнууд:")
for b in btns:
    txt = b.text.strip()
    href = b.get_attribute("href") or ""
    cls = b.get_attribute("class") or ""
    if any(x in txt for x in ["»", "›", "дараа", "next", "2", "3"]) or "page" in cls.lower() or "next" in cls.lower():
        print(f"  TEXT: '{txt}' | CLASS: '{cls}' | HREF: '{href[:80]}'")

driver.quit()