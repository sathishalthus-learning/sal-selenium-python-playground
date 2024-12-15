# Locators 

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_traditional_locators():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    
    # by ID
    driver.find_element(By.ID,"my-text-id").send_keys("selenium")

    # by Name
    driver.find_element(By.NAME,"my-password").send_keys("pass")

    # by Class Name
    driver.find_element(By.CLASS_NAME,"form-range").click();

    # by link text
    isLinkVisible = driver.find_element(By.LINK_TEXT,"Return to index").is_displayed();
    print(isLinkVisible)

    # by partial link text
    linkFullText = driver.find_element(By.PARTIAL_LINK_TEXT,"Return").text;
    print(linkFullText)

    # by css selector
    driver.find_element(By.CSS_SELECTOR,"input.form-control.form-control-color")

    # by tag name
    driver.find_element(By.TAG_NAME,"textarea").send_keys("only paragraph text")

    # by xpath  
    driver.find_element(By.XPATH,"//label[normalize-space()='Checked checkbox']").click()



    # end session
    driver.close()
    driver.quit()