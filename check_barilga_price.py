from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://barilga.mn/fwlink/barilgarate/")
    time.sleep(6)
    
    # Барилгын материалын үнэ холбоос хайх
    links = driver.find_elements(By.TAG_NAME, "a")
    material_links = []
    for l in links:
        txt = l.text.strip()
        href = l.get_attribute("href") or ""
        if "материалын үнэ" in txt.lower() or "материал" in txt.lower():
            material_links.append((txt, href))
            print(f"Холбоос: {txt} → {href}")
    
    # Хамгийн сүүлийн материалын үнэ нийтлэл рүү орох
    if material_links:
        url = material_links[0][1]
        print(f"\n{url} руу орж байна...")
        driver.get(url)
        time.sleep(5)
        
        body = driver.find_element(By.TAG_NAME, "body")
        print("\nНийтлэлийн текст:")
        print(body.text[:3000])

finally:
    driver.quit()