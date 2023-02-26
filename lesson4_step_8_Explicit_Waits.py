from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")


try:
    text = WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.ID,"price"),"$100")
        )#Ждем пока цена ну будет $100
    browser.find_element(By.CSS_SELECTOR,"button#book.btn.btn-primary").click()
    submit = browser.find_element(By.CSS_SELECTOR,"button#solve.btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);",submit) #скролим до submit
    x = int(browser.find_element(By.CSS_SELECTOR,"span#input_value.nowrap").text)
    y = str(calc(x))
    browser.find_element(By.CSS_SELECTOR,"input#answer.form-control").send_keys(y)
    submit.click()
    alert_obj = browser.switch_to.alert
    print(alert_obj.text)
finally:
    time.sleep(5)
    browser.quit()
    
    
