import sys

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By



def test_copy_and_paste(firefox_driver):
    driver = firefox_driver
    driver.get('https://selenium.dev/selenium/web/single_text_input.html')
    cmd_ctrl = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL

    ActionChains(driver)\
        .send_keys("Selenium!")\
        .send_keys(Keys.ARROW_LEFT)\
        .key_down(Keys.SHIFT)\
        .send_keys(Keys.ARROW_UP)\
        .key_up(Keys.SHIFT)\
        .key_down(cmd_ctrl)\
        .send_keys("xvv")\
        .key_up(cmd_ctrl)\
        .perform()

    assert driver.find_element(By.ID, "textInput").get_attribute('value') == "SeleniumSelenium!"

    def test_click_and_hold(driver):
        driver.get('https://selenium.dev/selenium/web/mouse_interaction.html')

        clickable = driver.find_element(By.ID, "clickable")
        ActionChains(driver) \
            .click_and_hold(clickable) \
            .perform()

        sleep(0.5)
        assert driver.find_element(By.ID, "click-status").text == "focused"

        
def test_can_scroll_to_element(driver):
    driver.get("https://selenium.dev/selenium/web/scrolling_tests/frame_with_nested_scrolling_frame_out_of_view.html")

    iframe = driver.find_element(By.TAG_NAME, "iframe")
    ActionChains(driver)\
        .scroll_to_element(iframe)\
        .perform()

    assert _in_viewport(driver, iframe)