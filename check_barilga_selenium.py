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
    time.sleep(8)
    
    # Бүх текстийг харах
    body = driver.find_element(By.TAG_NAME, "body")
    text = body.text
    print("Нийт текст урт:", len(text))
    print("\nЭхний 2000 тэмдэгт:")
    print(text[:2000])

finally:
    driver.quit()