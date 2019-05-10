from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.pages.base_page import BasePage


class CreateIssuePage(BasePage):

    PROJECT_FIELD = (By.ID, "project-field")
    ISSUE_TYPE = (By.ID, "issuetype-field")
    SUMMARY = (By.ID, "summary")
    DESCRIPTION = (By.CSS_SELECTOR, ".mce-container")
    PRIORITY = (By.ID, "priority-field")
    LABELS = (By.ID, "labels-textarea")
    ASSIGNEE = (By.ID, "assignee-field")
    EPIC = (By.ID, "customfield_10000-field")
    CREATE_ISSUE_SUBMIT_BUTTON_ID = (By.ID, "create-issue-submit")
    CANCEL_BUTTON_ID = (By.CSS_SELECTOR, "a.cancel")
    SUBMISSION_ERROR = (By.CSS_SELECTOR, ".error")
    ISSUE_SUCCESSFULLY_CREATED_MESSAGE = (By.ID, "aui-flag-container")

    def __init__(self, driver):
        self.driver = driver

    def set_project(self, project_name):
        if project_name is not None:
            self.driver.find_element(*self.PROJECT_FIELD).clear()
            self.driver.find_element(*self.PROJECT_FIELD).send_keys(project_name)
            self.driver.find_element(*self.PROJECT_FIELD).send_keys(Keys.ENTER)
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.CREATE_ISSUE_SUBMIT_BUTTON_ID))

    def set_issue_type(self, type_name):
        if type_name is not None:
            self.driver.find_element(*self.ISSUE_TYPE).clear()
            self.driver.find_element(*self.ISSUE_TYPE).send_keys(type_name)
            self.driver.find_element(*self.ISSUE_TYPE).send_keys(Keys.ENTER)
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.CREATE_ISSUE_SUBMIT_BUTTON_ID))

    def set_summary(self, summary):
        if summary is not None:
            self.driver.find_element(*self.SUMMARY).send_keys(summary)

    def set_description(self, description):
        if description is not None:
            self.driver.find_element(*self.DESCRIPTION).click()
            self.driver.find_element(*self.DESCRIPTION).send_keys(description)

    def set_priority(self, priority_name):
        if priority_name is not None:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.CREATE_ISSUE_SUBMIT_BUTTON_ID))
            self.driver.find_element(*self.PRIORITY).location_once_scrolled_into_view
            self.driver.find_element(*self.PRIORITY).clear()
            self.driver.find_element(*self.PRIORITY).send_keys(priority_name)
            self.driver.find_element(*self.PRIORITY).send_keys(Keys.ENTER)

    def set_assignee(self, assignee):
        if assignee is not None:
            self.driver.find_element(*self.ASSIGNEE).location_once_scrolled_into_view
            self.driver.find_element(*self.ASSIGNEE).clear()
            self.driver.find_element(*self.ASSIGNEE).send_keys(assignee)
            self.driver.find_element(*self.ASSIGNEE).send_keys(Keys.ENTER)

    def click_submit_button(self):
        self.driver.find_element(*self.CREATE_ISSUE_SUBMIT_BUTTON_ID).click()

    def click_cancel_button(self):
        self.driver.find_element(*self.CANCEL_BUTTON_ID).click()

    def at_page(self):
        return self.is_element_visible(self.CREATE_ISSUE_SUBMIT_BUTTON_ID) & ("Create Issue - Hillel IT School JIRA" in self.driver.title)

    def is_successful_message_displayed(self):
        return self.is_element_visible(self.ISSUE_SUCCESSFULLY_CREATED_MESSAGE)

    def is_submission_error_displayed(self):
        return self.is_element_visible(self.SUBMISSION_ERROR)

    def create_issue(self, project_name, issue_type, summary, description, priority, assignee):
        self.set_project(project_name)
        self.set_issue_type(issue_type)
        self.set_summary(summary)
        self.set_description(description)
        self.set_priority(priority)
        self.set_assignee(assignee)
        self.click_submit_button()

    def accept_alert(self):
        self.driver.switch_to.alert.accept()
