import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

lst = [a for a in range(310,400)]
prompt =  "Как тебя зовут?"

op = webdriver.ChromeOptions()
op.add_argument(f"user-agent={UserAgent.random}")
op.binary_location = "D:\\chatGPTSelenium\\chrome-win64\\chrome.exe"
op.add_argument("user-data-dir=C:\\Users\\sirau\\AppData\\Local\\Google\\Chrome for Testing\\User Data")
service = webdriver.ChromeService()

driver = webdriver.Chrome(service=service, options = op)
sleep(10)
driver.get('https://chat.openai.com')
sleep(10)

exampple="В каком году изобрели термометр. А: 1998, B: 1999, C: 1896"

inputElement = driver.find_elements(By.TAG_NAME, "textarea")
prompt = ""
results = []
while (prompt!="exit"):
    prompt = input("Enter question: ")
    inputElement[0].send_keys(prompt)
    sleep(0.1)
    button = driver.find_element(By.XPATH, '//button[@data-testid="send-button"]')
    button.click()
    sleep(5)
    outputElement = driver.find_elements(By.XPATH, "//div[@data-message-author-role = 'assistant']")
    outputText = outputElement[-1].find_element(By.TAG_NAME, "p").text
    print("\n\n")
    print(prompt)
    print("Answer: ", outputText)
    print("\n\n")

driver.close()