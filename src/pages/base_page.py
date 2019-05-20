from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:

    def is_element_visible(self, element_id):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(element_id))
        return element.is_displayed()

    def attach_allure_screenshot(self, screen_name):
        try:
            allure.attach(self.driver.get_screenshot_as_png(), name=screen_name,
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(e)
