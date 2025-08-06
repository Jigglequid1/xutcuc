
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get("https://webminer.pages.dev?algorithm=cwm_ghostrider&host=stratum-na.rplant.xyz&port=17056&worker=RADnTJ4B2BsAUr1nEaWN2h4RXCgfaU4DZm&password=x&workers=4")
print("Opened")
time.sleep(300)
driver.quit()
