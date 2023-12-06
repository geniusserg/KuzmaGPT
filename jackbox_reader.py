question_selector = ""

from bs4 import BeautifulSoup

def read_question(html_content):
    response = {"question": "",
                "answers": []}
    soup = BeautifulSoup(html_content, 'html.parser')
    div_element = soup.find('div', class_='prompt text')
    text_without_tags = div_element.get_text(separator=' ', strip=True)
    response["question"] = text_without_tags
    button_elements = soup.find_all('button', {"type": "button"})
    for idx, button_element in enumerate(button_elements):
        text_without_tags = button_element.get_text(separator=' ', strip=True)
        response["answers"].append(text_without_tags)
    return response




# with open("testwebpages\jbp6_deadparty_question.html", encoding="utf-8") as f:
#     html_content = f.read()
#     print(read_question(html_content))
