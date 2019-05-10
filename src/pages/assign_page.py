from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class AssignPage(BasePage):

    ASSIGNEE_FIELD = (By.ID, "assignee-field")
    COMMENT_FIELD = (By.ID, "mce_9_ifr")
    ASSIGN_BUTTON_SUBMIT = (By.ID, "assign-issue-submit")
    CANCEL_BUTTON = (By.ID, "assign-issue-cancel")

    def __init__(self, driver):
        self.driver = driver

    def set_assignee(self, assignee):
        assert self.at_page()
        self.driver.find_element(*self.ASSIGNEE_FIELD).send_keys(assignee)
        self.driver.find_element(*self.ASSIGN_BUTTON_SUBMIT).click()

    def close_dialog(self):
        self.is_element_visible(self.CANCEL_BUTTON)
        self.driver.find_element(*self.CANCEL_BUTTON).click()

    def at_page(self):
        return self.is_element_visible(self.ASSIGN_BUTTON_SUBMIT)
