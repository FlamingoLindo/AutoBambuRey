from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

def teste(self, wait, subcategory):
    end_x_ = 500
    end_y_ = 1630
    max_retries = 1
    retry_count = 0
    while retry_count < max_retries:
        try:
            # Try to find the element with "0 Vendido(s)"
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0 Vendido(s)")')))
            print(f'Ad with "0 Vendido(s)" found in the "{subcategory}" tab!')
            # If the ad with "0 Vendido(s)" is found, you can proceed with your logic
            another_button = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().className("com.horcrux.svg.PathView").instance(0))')))
            another_button.click()
            break
        except TimeoutException:
            print(f'No ad with "0 Vendido(s)" found in "{subcategory}", trying to find "R$"...')
            try:
                # If "0 Vendido(s)" is not found, try to find an element with "R$"
                wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("R$")')))
                print(f'Found "R$" in the "{subcategory}" tab!')
                # Proceed with your logic after finding "R$"
                another_button = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().className("com.horcrux.svg.PathView").instance(0))')))
                another_button.click()
                break
            except TimeoutException:
                print(f'No ad with "R$" found, trying to swipe again...')
                # Swipe again to try to find the ad
                end_x_ -= 150
                end_y_ -= 150
                self.driver.swipe(start_x=543, start_y=1630, end_x=end_x_, end_y=end_y_, duration=90)
                retry_count += 1
                if retry_count == max_retries:
                    print(f"Failed to find the ad after {max_retries} attempt(s), pressing go back button.")
                    # Press the "go back" button (adjust the selector if necessary)
                    another_button = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')))
                    another_button.click()
