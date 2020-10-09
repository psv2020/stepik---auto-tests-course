from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    #robots_radio = browser.find_element_by_id("robotsRule")
    #robots_checked = robots_radio.get_attribute("checked")

    x_element = browser.find_element_by_css_selector("img")
    x = x_element.get_attribute("valuex")
    y = calc(x)


    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox") 
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    
    #input2 = browser.find_element_by_name("last_name")
    #input2.send_keys("Petrov")
    #input3 = browser.find_element_by_class_name("city")
    #input3.send_keys("Smolensk")
    #input4 = browser.find_element_by_id("country")
    #input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла