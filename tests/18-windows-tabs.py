from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_winduws():
    with webdriver.Firefox() as driver:
    # Open URL
        driver.get("https://seleniumhq.github.io")

        # Setup wait for later
        wait = WebDriverWait(driver, 10)

        # Store the ID of the original window
        original_window = driver.current_window_handle

        # Check we don't have other windows open already
        assert len(driver.window_handles) == 1

        # Opens a new window and switches to new window
        driver.switch_to.new_window('window')

                #Switch back to the old tab or window
        driver.switch_to.window(original_window)

        # Loop through until we find a new window handle
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        
        #Close the tab or window
        driver.close()


        driver.quit()