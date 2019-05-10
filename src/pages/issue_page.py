from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.pages.base_page import BasePage


class IssuePage(BasePage):

    PROJECT_NAME = (By.ID, "project-name-val")
    ISSUE_NUMBER = (By.ID, "key-val")
    SUMMARY_FIELD = (By.ID, "summary-val")
    ACTIVATED_SUMMARY_FIELD = (By.ID, "summary")
    PRIORITY_FIELD = (By.ID, "priority-val")
    ACTIVATED_PRIORITY_FIELD = (By.ID, "priority-field")
    ASSIGNEE_FIELD = (By.ID, "assignee-val")
    ACTIVATED_ASSIGNEE_FIELD = (By.ID, "assignee-field")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".submit")
    EDIT_BUTTON = (By.ID, "edit-issue")
    ASSIGN_BUTTON = (By.ID, "assign-issue")
    MORE_BUTTON = (By.ID, "opsbar-operations_more")
    DELETE_SUBMENU_BUTTON = (By.ID, "delete-issue")
    DELETE_ISSUE_DIALOG = (By.ID, "delete-issue-dialog")
    DELETE_ISSUE_SUBMIT_BUTTON = (By.ID, "delete-issue-submit")
    BACKLOG_BUTTON = (By.ID, "action_id_11")
    SELECTED_FOR_DEVELOPMENT = (By.ID, "action_id_21")
    DROPDOWN_ARROW = (By.CSS_SELECTOR, ".drop-menu")

    def __init__(self, driver):
        self.driver = driver

    def set_summary(self, summary):
        self.driver.find_element(*self.SUMMARY_FIELD).click()
        self.is_element_visible(self.ACTIVATED_SUMMARY_FIELD)
        self.driver.find_element(*self.ACTIVATED_SUMMARY_FIELD).send_keys(summary)
        self.driver.find_element(*self.ACTIVATED_SUMMARY_FIELD).send_keys(Keys.ENTER)
        self.is_element_visible(self.SUMMARY_FIELD)

    def set_priority(self, priority):
        self.driver.find_element(*self.PRIORITY_FIELD).click()
        self.is_element_visible(self.DROPDOWN_ARROW)
        self.driver.find_element(*self.ACTIVATED_PRIORITY_FIELD).send_keys(priority)
        self.driver.find_element(*self.ACTIVATED_PRIORITY_FIELD).send_keys(Keys.ENTER)
        self.driver.find_element(*self.ACTIVATED_PRIORITY_FIELD).send_keys(Keys.ENTER)
        self.is_element_visible(self.PRIORITY_FIELD)

    def set_assignee(self, assignee):
        self.driver.find_element(*self.ASSIGNEE_FIELD).click()
        self.is_element_visible(self.DROPDOWN_ARROW)
        self.driver.find_element(*self.ACTIVATED_ASSIGNEE_FIELD).send_keys(assignee)
        self.driver.find_element(*self.ACTIVATED_ASSIGNEE_FIELD).send_keys(Keys.ENTER)
        self.is_element_visible(self.ASSIGNEE_FIELD)

    def open_assign_dialog(self):
        self.driver.find_element(*self.ASSIGN_BUTTON).click()

    def delete_issue(self):
        self.driver.find_element(*self.MORE_BUTTON).click()
        self.driver.find_element(*self.DELETE_SUBMENU_BUTTON).click()
        self.is_element_visible(self.DELETE_ISSUE_DIALOG)
        self.driver.find_element(*self.DELETE_ISSUE_SUBMIT_BUTTON).click()

    def at_page(self):
        return self.is_element_visible(self.PROJECT_NAME) & self.is_element_visible(self.ISSUE_NUMBER)

    def get_summary(self):
        self.driver.find_element(*self.SUMMARY_FIELD).click()
        self.is_element_visible(self.ACTIVATED_SUMMARY_FIELD)
        return self.driver.find_element(*self.ACTIVATED_SUMMARY_FIELD).get_attribute('value')

    def get_priority(self):
        self.driver.find_element(*self.PRIORITY_FIELD).click()
        self.is_element_visible(self.DROPDOWN_ARROW)
        return self.driver.find_element(*self.ACTIVATED_PRIORITY_FIELD).get_attribute('value')

    def get_assignee(self):
        self.driver.find_element(*self.ASSIGNEE_FIELD).click()
        self.is_element_visible(self.DROPDOWN_ARROW)
        return self.driver.find_element(*self.ACTIVATED_ASSIGNEE_FIELD).get_attribute('value')
