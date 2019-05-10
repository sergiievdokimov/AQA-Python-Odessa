from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_INPUT_FIELD = (By.ID, "login-form-username")
    PASSWORD_INPUT_FIELD = (By.ID, "login-form-password")
    LOGIN_BUTTON = (By.ID, "login")
    REMEMBER_LOGIN_CHECKMARK = (By.ID, "login-form-remember-me")
    LOGIN_ERROR_MESSAGE = (By.ID, "usernameerror")
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://jira.hillel.it/secure/Dashboard.jspa")
        return self

    def login_to_jira(self, username, password):
        self.driver.find_element(*self.LOGIN_INPUT_FIELD).clear()
        self.driver.find_element(*self.LOGIN_INPUT_FIELD).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT_FIELD).click()
        self.driver.find_element(*self.PASSWORD_INPUT_FIELD).clear()
        self.driver.find_element(*self.PASSWORD_INPUT_FIELD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).submit()

    def at_page(self):
        return "System Dashboard - Hillel IT School JIRA" in self.driver.title

    def is_error_shown(self):
        return self.is_element_visible(self.LOGIN_ERROR_MESSAGE)
