from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from src.pages.create_issue_page import CreateIssuePage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage
from users_data import ValidUser


class BaseTest:

    driver = None

    def setup_class(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.login_page = LoginPage(self.driver)
        self.login_page.open_page()
        self.dashboard_page = DashboardPage(self.driver)
        self.login_page.login_to_jira(ValidUser.username, ValidUser.password)
        assert self.dashboard_page.at_page()
        self.create_issue_page = CreateIssuePage(self.driver)

    def teardown_class(self):
        self.driver.close()




