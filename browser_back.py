import time
from datetime import datetime
from pytz import timezone
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

url = "https://example.com"   # ここに更新したいページのURLを指定
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get(url)

try:
    while True:
        jst = timezone("Asia/Tokyo") # Japan Standard Time (JST)
        current_time = datetime.now(jst)

        # 毎朝9時にブラウザバック
        if current_time.hour == 9 and current_time.minute == 0:
            driver.back()  
            print("Performed browser back action at 9:00 AM JST")

            time.sleep(60)

        time.sleep(30)
except KeyboardInterrupt:
    print("Script terminated by user")
finally:
    driver.quit()
