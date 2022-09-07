from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

songs = {"alive", "champions", "לייק וואנקה"}

PATH = "C:\Windows\System32\chromedriver.exe"
driver = webdriver.Firefox()

driver.get("https://free-mp3-download.net/")

for song in songs:
    search = driver.find_element("id", "q")
    search.send_keys(song)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="snd"]'))).click()
    time.sleep(2)
    element = driver.find_element(By.XPATH, value='/html/body/main/div/div[2]/div/table/tbody/tr[1]/td[3]/a/button')
    driver.execute_script("arguments[0].click();", element)
    driver.execute_script(
        """ for (let i of document.getElementsByClassName('adsbygoogle')){ i.style.display = 'none'; } """)
    element = driver.find_element(By.XPATH, value='/html/body/main/div/div[2]/div/table/tbody/tr[1]/td[3]/a/button')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(20)

    element = driver.find_element(By.XPATH, value='/html/body/main/div/div/div/div/div[3]/button')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(10)
    driver.back()
    time.sleep(3)
