import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from jackbox_reader import read_question

op = webdriver.ChromeOptions()
op.binary_location = "D:\\chatGPTSelenium\\chrome-win64\\chrome.exe"
op.add_argument("user-data-dir=C:\\Users\\sirau\\AppData\\Local\\Google\\Chrome for Testing\\User Data")
service = webdriver.ChromeService()
driver = webdriver.Chrome(service=service, options = op)
sleep(1)
driver.get('D:\\chatGPTSelenium\\testwebpages\\jbp6_deadparty_question.html')

# Ожидание появления кнопки с типом 'submit' в течение 10 секунд
wait = WebDriverWait(driver, 10)
button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="prompt text"]')))
html_content = driver.page_source
print(read_question(html_content))

answer = 3

button_with_answer = driver.find_element(By.CSS_SELECTOR, f'button[data-action="choose"][data-index="{answer}"]')
button_with_answer.click()

sleep(1)