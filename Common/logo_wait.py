"""
This module is used for waiting until the logo loads.
"""

# Imports
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def wait_for_logo(wait):
    """Wait untill the logo loads

    Args:
        wait (_type_): _description_
    """
    logo = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '.cUYAoG')))