from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x_str):
    return str(math.log(abs(12*math.sin(int(x_str)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    btn = browser.find_element_by_css_selector("#book")
    txt = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    btn.click()
    
    x_str = browser.find_element_by_css_selector("#input_value").text
    x = calc(x_str)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(x)
    
    btn2 = browser.find_element_by_css_selector("#solve")
    btn2.click()
    
finally:
    time.sleep(5)
    browser.quit()
    