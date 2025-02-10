import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# hi
driver.get('https://monkeytype.com/')
time.sleep(4)
input_type = driver.find_element(By.ID, "wordsInput")
cookies = driver.find_element(By.XPATH, "/html/body/div[9]/dialog[2]/div[2]/div[2]/div[2]/button[1]")
cookies.click()
time.sleep(1)
words = driver.find_element(By.XPATH, "/html/body/div[10]/main/div/div[1]/div/div[3]/button[2]")
words.click()
time.sleep(3)
for i in range(50):
    word_current = driver.find_element(By.CSS_SELECTOR, ".word.active")
    input_type.send_keys(word_current.text + ' ')

time.sleep(10)
driver.quit()

