"""
This module is used for creating X amount of "Parceiros" users.
"""

# Imports
import os
from selenium.webdriver.common.by import By

# File path
upload_file = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../Images", "document.png"))

def input_document(driver):
    """Sends a file to a file input

    Args:
        driver (WebDriver): Selenium WebDriver instance used 
        for interacting with the browser.
    """
    try:
        document_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        document_input.send_keys(upload_file)
    except Exception as e:
        print('Error in sending a document.\n', e)