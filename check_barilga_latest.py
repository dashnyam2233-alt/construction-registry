from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://barilga.mn/nc/18/")
    time.sleep(5)
    
    # Хамгийн сүүлийн нийтлэлийн холбоос авах
    links = driver.find_elements(By.TAG_NAME, "a")
    article_links = []
    for l in links:
        href = l.get_attribute("href") or ""
        txt = l.text.strip()
        if "/n/" in href and txt:
            article_links.append((txt, href))
    
    print("Нийтлэлүүд:")
    for t, h in article_links[:5]:
        print(f"  {t} → {h}")
    
    # Хамгийн сүүлийн нийтлэл рүү орох
    if article_links:
        url = article_links[0][1]
        print(f"\n{url} руу орж байна...")
        driver.get(url)
        time.sleep(5)
        
        body = driver.find_element(By.TAG_NAME, "body")
        print("\nНийтлэлийн бүтэн текст:")
        print(body.text[:5000])

finally:
    driver.quit()