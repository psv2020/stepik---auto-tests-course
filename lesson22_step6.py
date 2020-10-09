from selenium import webdriver
import time 
import math

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 200);")

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)



    #y_element = browser.find_element_by_id("num2")
    #y = y_element.text
   
    #z = str(str(int(x)+int(y)))

    #from selenium.webdriver.support.ui import Select

    #select = Select(browser.find_element_by_tag_name("select"))
    #select.select_by_value(z) 


    #input1 = browser.find_element_by_id("answer")
    #input1.send_keys(y)

    #browser.find_element_by_tag_name("select").click()
    #browser.find_element_by_css_selector("[value=z]").click()

 #   input1 = browser.find_element_by_id("answer")
 #   input1.send_keys(y)
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