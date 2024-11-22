"""
This module is used for clicking at the "next" button.
"""

# Imports
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def click_next_btn(wait, driver):
    """Clicks at the "next" button if forms

    Args:
        wait (WebDriverWait): Selenium WebDriverWait instance used 
        for waiting for elements to be in a certain state.
        
        driver (WebDriver): Selenium WebDriver instance used 
        for interacting with the browser.
    """
    try:
        next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cScPww')))
        ActionChains(driver).scroll_to_element(next_btn).perform()
        next_btn.click()
    except Exception as e:
        print('Error in "next button".\n', e)