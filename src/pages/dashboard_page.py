from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.pages.base_page import BasePage


class DashboardPage(BasePage):

    DASHBOARD_BUTTON = (By.ID, "home_link")
    PROJECTS_BUTTON = (By.ID, "browse_link")
    ISSUES_BUTTON = (By.ID, "find_link")
    CREATE_BUTTON = (By.ID, "create_link")
    QUICK_SEARCH_FIELD = (By.ID, "quickSearchInput")
    PROFILE_LOGO = (By.ID, "header-details-user-fullname")
    CURRENT_SEARCH_ISSUES_SUBMENU_OPTION = (By.ID, "jira.top.navigation.bar:issues_drop_current_lnk")
    SEARCH_FOR_ISSUES_ISSUES_SUBMENU_OPTION = (By.ID, "issues_new_search_link")
    VIEW_SYSTEM_DASHBOARD_SUBMENU_OPTION = (By.ID, "dash_lnk_system_lnk")

    def __init__(self, driver):
        self.driver = driver

    def at_page(self):
        return ("System Dashboard - Hillel IT School JIRA" in self.driver.title) & (self.is_element_visible(self.PROFILE_LOGO))

    def open_create_issue_page(self):
        self.is_element_visible(self.CREATE_BUTTON)
        self.driver.find_element(*self.CREATE_BUTTON).click()

    def open_search_issues_page(self):
        self.is_element_visible(self.ISSUES_BUTTON)
        self.driver.find_element(*self.ISSUES_BUTTON).click()
        self.is_element_visible(self.SEARCH_FOR_ISSUES_ISSUES_SUBMENU_OPTION)
        self.driver.find_element(*self.SEARCH_FOR_ISSUES_ISSUES_SUBMENU_OPTION).click()

    def open_dashboard_page(self):
        self.is_element_visible(self.DASHBOARD_BUTTON)
        self.driver.find_element(*self.DASHBOARD_BUTTON).click()
        self.is_element_visible(self.VIEW_SYSTEM_DASHBOARD_SUBMENU_OPTION)
        self.driver.find_element(*self.VIEW_SYSTEM_DASHBOARD_SUBMENU_OPTION).click()

    def quick_search(self, search_text):
        self.driver.find_element(*self.QUICK_SEARCH_FIELD).send_keys(search_text)
        self.driver.find_element(*self.QUICK_SEARCH_FIELD).send_keys(Keys.ENTER)

    def open_issue(self, issue_id):
        self.driver.find_element(*self.QUICK_SEARCH_FIELD).send_keys(issue_id)
        self.driver.find_element(*self.QUICK_SEARCH_FIELD).send_keys(Keys.ENTER)
