import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


service = ChromeService(executable_path="C:/Users/user/Documents/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service = service)
f = open(r"C:/Users/user/Desktop/pay/test.csv", 'a', encoding= 'UTF-8', newline = '')
writer = csv.writer(f)

driver.get("https://www.univstore.com/category/computer?ctg_sub_code=020100&ctg_third_code=020101")
wait = WebDriverWait(driver, 5)

def crawl():
    while(True):
        h = driver.execute_script('return window.scrollY')
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        if(h == driver.execute_script('return window.scrollY')):
            break
    wait = WebDriverWait(driver, 10)  # 10초 동안 대기
    # element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'product_info_area__xxCTi')))
    time.sleep(1)
    titles = driver.find_elements(By.CLASS_NAME, 'usItemInfoLink')
    prices = driver.find_elements(By.CLASS_NAME, 'usItemCardInfoPrice1Value')
    print(titles)
    time.sleep(20)

    print(len(titles), len(prices))
    for i in range(len(titles)):
        row = [titles[i].text, prices[i].text]
        print(row)
        writer.writerow(row)

crawl()
# for i in range(10):
#     crawl()
#     driver.find_element(By.CLASS_NAME, 'pagination_next__pZuC6').send_keys(Keys.ENTER)
#     time.sleep(0.7)
    
    # element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'basicList_title__VfX3c')))
    # element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'price_num__S2p_v')))