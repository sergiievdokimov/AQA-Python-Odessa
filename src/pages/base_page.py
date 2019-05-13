from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def is_element_visible(self, element_id):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(element_id))
        return element.is_displayed()
