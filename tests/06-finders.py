# element finding strategies

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_find_strategies():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/html5Page.html")

    # first matching element

    firstElement = driver.find_element(By.TAG_NAME,"img");
    print(firstElement.get_attribute("id"))

    # finding element in subset of dom
    colors = driver.find_element(By.ID,"images")
    red = colors.find_element(By.ID,"red")


    # evaluating shadow dom
    

    # optimized locator

    # find all matching elements
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    form_labels = driver.find_elements(By.CLASS_NAME,"form-label")
    for label in form_labels:
        print(label.text)

    # find element from element

    # get active element

    # 