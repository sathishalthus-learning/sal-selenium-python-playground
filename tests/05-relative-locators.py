# relative locators

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import ByType

# test
def test_relative_locators():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/relative_locators.html")

    # below
    raise Exception("not implemented")
    
    # above

    # right of

    # left of

    # chaining of relative locators

    # 
    driver.close()
    driver.quit()