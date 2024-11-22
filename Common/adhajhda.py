from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

def app_scroll(wait, self, locator_type, value):
    element = wait.until(EC.presence_of_element_located((locator_type, value)))

    self.driver.execute_script("mobile: scrollGesture", {
        "elementId": element.id,  # ID of the target element
        "direction": "down",       # Scroll direction ('up', 'down')
        "percent": 1.4,            # Larger scroll (150%)
    })
        
import time

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
        time.sleep(1)
        another_button.click()
        
    except Exception as e:
        print(f"Error while selecting category '{category_value}': {e}")



def teste(self, wait, subcategory):
    end_x_ = 500
    end_y_ = 1630
    max_retries = 1
    retry_count = 0
    while retry_count < max_retries:
        try:
            # Try to find the element with "0 Vendido(s)"
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Vendido(s)")')))
            print(f'Ad with "0 Vendido(s)" found in the "{subcategory}" tab!\n')
            # If the ad with "0 Vendido(s)" is found, you can proceed with your logic
            another_button = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().className("com.horcrux.svg.PathView").instance(0))')))
            another_button.click()
            break
        except TimeoutException:
            print(f'No ad with "0 Vendido(s)" found in "{subcategory}", trying to find "R$"...\n')
            try:
                # If "0 Vendido(s)" is not found, try to find an element with "R$"
                wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("R$")')))
                print(f'Found "R$" in the "{subcategory}" tab!\n')
                # Proceed with your logic after finding "R$"
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
