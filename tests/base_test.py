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

    def log_full(r):
        req = r.request
        """
        At this point it is completely built and ready
        to be fired; it is "prepared".

        However pay attention at the formatting used in
        this function because it is programmed to be pretty
        printed and may differ from the actual request.
        """
        print()
        print('{}\n{}\n{}\n\n{}'.format(
            '-----------REQUEST-----------',
            req.method + ' ' + req.url,
            '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
            req.body,
        ))

        print()

        print('{}\n{}\n{}\n\n{}'.format(
            '-----------RESPONSE-----------',
            r.status_code,
            '\n'.join('{}: {}'.format(k, v) for k, v in r.headers.items()),
            r.text,
        ))
        print()
