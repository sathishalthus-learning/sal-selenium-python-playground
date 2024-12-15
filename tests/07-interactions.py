#  interactions with elements
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_interactions_with_elements():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/inputs.html")

    # Click on the checkbox
    check_input = driver.find_element(By.NAME, "checkbox_input")
    check_input.click()

    is_checked = check_input.is_selected()
    assert is_checked == False

    # Handle the email input field
    email_input = driver.find_element(By.NAME, "email_input")
    email_input.clear()  # Clear field
    
    email = "admin@localhost.dev"
    email_input.send_keys(email)  # Enter text

    # Verify input
    data = email_input.get_attribute("value")
    assert data == email

    # Clear the email input field again
    email_input.clear()
    data = email_input.get_attribute("value")
    assert data == ""

    driver.quit()