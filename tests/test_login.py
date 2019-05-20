import allure
from webdriver_manager.chrome import ChromeDriverManager
from src.pages.create_issue_page import CreateIssuePage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage
from tests.base_test import BaseTest
from users_data import ValidUser, InvalidUser
from selenium import webdriver


class TestLogin(BaseTest):

    def setup_class(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        self.create_issue_page = CreateIssuePage(self.driver)

    @allure.tag("UI")
    @allure.title("Login with correct username & wrong password")
    def test_login_correct_username_wrong_password(self):
        self.login_page.open_page()
        assert self.login_page.at_page()
        self.login_page.login_to_jira(ValidUser.username, InvalidUser.password)
        assert self.login_page.is_error_shown()

    @allure.tag("UI")
    @allure.title("Login with wrong username & correct password")
    def test_login_wrong_username_correct_password(self):
        self.login_page.open_page()
        assert self.login_page.at_page()
        self.login_page.login_to_jira(InvalidUser.username, ValidUser.password)
        assert self.login_page.is_error_shown()

    @allure.tag("UI")
    @allure.title("Login with correct username & correct password")
    def test_login_correct_username_correct_password(self):
        self.login_page.open_page()
        assert self.login_page.at_page()
        self.login_page.login_to_jira(ValidUser.username, ValidUser.password)
        assert self.dashboard_page.at_page()
