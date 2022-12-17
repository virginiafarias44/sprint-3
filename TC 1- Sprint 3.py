import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

option1 = Options()
option1.add_argument("--disable-notifications")
option1.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=option1)
driver.get("https://shop.samsung.com/ar/")

time.sleep(5)

cp = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/section/div[1]/button")
cp.click()
time.sleep(5)

cookies = driver.find_element(By.XPATH, '//*[@id="truste-consent-button"]').click()
time.sleep(8)

try:
   electrodomesticos =  driver.find_element(By.LINK_TEXT, 'Electrodomésticos').click()
except:
    print("Not working")

time.sleep(10)

try:
    driver.find_element(By.XPATH, '//*[@id="headerSamsung"]/div[2]/div/div/a').click()
except:
    print("Not return")

time.sleep(10)
driver.close()