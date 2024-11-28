from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

def app_swipe(self, x1: int, y1: int, x2: int, y2: int):
    """
    Simulates a swipe gesture on the screen from one point to another.

    Args:
        x1 (int): The x-coordinate of the starting point.
        y1 (int): The y-coordinate of the starting point.
        x2 (int): The x-coordinate of the destination point.
        y2 (int): The y-coordinate of the destination point.
    
    This method uses the ActionChains API to simulate a touch swipe action,
    starting from the coordinates (x1, y1) and ending at (x2, y2).
    """
    actions = ActionChains(self.driver)
    actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(x1, y1)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(x2, y2)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

def app_tap(self, x, y):
    """
    Simulates a tap gesture on the screen at the specified coordinates.

    Args:
        x (int): The x-coordinate of the tap location.
        y (int): The y-coordinate of the tap location.

    This method uses the tap API to simulate a single touch tap at the coordinates (x, y).
    """
    self.driver.tap([(x, y)])