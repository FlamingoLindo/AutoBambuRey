import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

def app_scroll(driver):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(540, 1933)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(540, 1540)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
        


def select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators):
    """
    Function to select a category with scroll functionality and multiple subcategories.
    
    Parameters:
    - self: The instance of the current test case.
    - wait: The WebDriverWait instance used for waiting for elements.
    - category_locator: Locator type for the category (e.g., AppiumBy.ANDROID_UIAUTOMATOR).
    - category_value: The value for the category to be located (e.g., 'Academia').
    - subcategory_locators: A list of tuples containing the locator type and value for the subcategories.
    """
    try:
        # Scroll and click the category
        category_element = wait.until(EC.visibility_of_element_located((
            category_locator, 
            f'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().text("{category_value}"))'
        )))
        category_element.click()
        print(f"Category '{category_value}' selected.")
        time.sleep(0.5)
        # Iterate through the list of subcategories
        for subcategory_locator, subcategory_value in subcategory_locators:
            try:
                # Wait and click the subcategory
                subcategory_element = wait.until(EC.visibility_of_element_located((
                    AppiumBy.ACCESSIBILITY_ID, 
                    subcategory_value
                )))
                subcategory_element.click()
                print(f"Subcategory '{subcategory_value}' selected.")
                
                # Call the test or any other function for further actions after selecting the subcategory
                teste(self, wait, subcategory_value)
                
            except Exception as e:
                print(f"Error while selecting subcategory '{subcategory_value}': {e}")
        
        # Click another button as per your original code
        another_button = wait.until(EC.element_to_be_clickable((
            AppiumBy.ANDROID_UIAUTOMATOR, 
            'new UiSelector().className("android.view.ViewGroup").instance(14)'
        )))
        time.sleep(1.5)
        another_button.click()
        
    except Exception as e:
        print(f"Error while selecting category '{category_value}': {e}")



def teste(self, wait, subcategory):
    total_value = 0
    end_x_ = 500
    end_y_ = 1630
    max_retries = 1
    retry_count = 0
    while retry_count < max_retries:
        try:
            # Try to find the element with "0 Vendido(s)"
            ad = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("R$")')))
            print(f'Ad with "R$" found in the "{subcategory}" tab!')
            print(ad.text, '\n')
            # If the ad with "R$" is found, you can proceed with your logic
            another_button = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().className("com.horcrux.svg.PathView").instance(0))')))
            another_button.click()
            break
        except TimeoutException:
            print(f'No ad with "R$" found in "{subcategory}", trying to find "Vendido(s)"...\n')
            try:
                # If "R$" is not found, try to find an element with "Vendido(s)"
                ad = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Vendido(s)")')))
                print(f'Found "Vendido(s)" in the "{subcategory}" tab!')
                print(ad.text, '\n')
                # Proceed with your logic after finding "Vendido(s)"
                another_button = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().className("com.horcrux.svg.PathView").instance(0))')))
                another_button.click()
                break
            except TimeoutException:
                print(f'No ad with "R$" found, trying to swipe again...\n')
                # Swipe again to try to find the ad
                end_x_ -= 150
                end_y_ -= 150
                self.driver.swipe(start_x=543, start_y=1630, end_x=end_x_, end_y=end_y_, duration=90)
                retry_count += 1
                if retry_count == max_retries:
                    print(f"Failed to find the ad after {max_retries} attempt(s), pressing go back button.\n")
                    # Press the "go back" button (adjust the selector if necessary)
                    another_button = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')))
                    another_button.click()
