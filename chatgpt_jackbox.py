import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

lst = [a for a in range(310,400)]
prompt =  "Как тебя зовут?"

def generate_prompt(question_dict):
    question = question_dict["question"]
    answers = question_dict["answers"]
    answers_str = ""
    for idx, answer in enumerate(answers):
        answers_str += f"{str(idx)}: {answer}, "
    answers_str = answers_str[:-2]
    prompt = (f'Ты играешь в телевикторину. Вопрос: {question}. Ответы: {answers_str}. Скажи только цифру, если скажешь слово Ответ или слова содержащие ответ - проигрыш')
    return prompt

def send_prompt(prompt):
    inputElement = driver.find_elements(By.TAG_NAME, "textarea")
    inputElement[0].send_keys(prompt)
    sleep(0.1)
    button = driver.find_element(By.XPATH, '//button[@data-testid="send-button"]')
    button.click()
    sleep(5)
    outputElement = driver.find_elements(By.XPATH, "//div[@data-message-author-role = 'assistant']")
    outputText = outputElement[-1].find_element(By.TAG_NAME, "p").text
    return outputText

def test_chat():
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

op = webdriver.ChromeOptions()
op.binary_location = "D:\\chatGPTSelenium\\chrome-win64\\chrome.exe"
op.add_argument("user-data-dir=C:\\Users\\sirau\\AppData\\Local\\Google\\Chrome for Testing\\User Data")
service = webdriver.ChromeService()

driver = webdriver.Chrome(service=service, options = op)
sleep(10)
driver.get('https://chat.openai.com')
sleep(3)

# code here
example = {'question': 'Популярность какого фильма привела к созданию в Minecraft режима, который можно считать ранней версией жанра "Королевская битва"?', 'answers': ['Дивергент', 'Гарри Поттер и Кубок огня', '300 спартанцев', 'Голодные игры']}

prompt = generate_prompt(example)
print("Log: ", prompt)
answer = send_prompt(prompt)
print("Answer from ChatGPT: ", answer)

sleep(4)

driver.close()

