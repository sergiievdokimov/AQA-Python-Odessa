from tests.base_test import BaseTest
from random import randint
import time
import allure
import random
import string


class TestCreateIssue(BaseTest):

    project_name = "Webinar"
    issue_type = "Bug"
    summary = 'Issue summary #' + str(randint(1, 9999))
    description = "Description of the issue"
    priority = "High"
    assignee = "SergiiIevdokymov"
    exceeded_summary = ''.join(random.choices(string.ascii_lowercase, k=256))

    def setup_method(self):
        self.dashboard_page.open_create_issue_page()
        assert self.create_issue_page.at_page()

    @allure.tag("UI")
    @allure.title('Successful issue creation with customizing all necessary parameters')
    def test_create_issue(self):
        with allure.step('Create issue with setting project, issue type, summary, description, priority & assignee'):
            self.create_issue_page.create_issue(self.project_name, self.issue_type, self.summary, self.description, self.priority, self.assignee)
        with allure.step('Assure that issue has been created'):
            self.create_issue_page.is_successful_message_displayed()
            time.sleep(1)

    @allure.tag("UI")
    @allure.title("Successfully create an issue with customizing only summary field")
    def test_create_issue_only_summary(self):
        self.create_issue_page.create_issue(None, None, self.summary, None, None, None)
        assert self.create_issue_page.is_successful_message_displayed()
        self.create_issue_page.attach_allure_screenshot("Issue is correctly created.png")
        time.sleep(2)

    @allure.tag("UI")
    @allure.title('Try to create issue without the summary')
    def test_create_issue_no_summary(self):
        with allure.step('Create issue without setting summary'):
            self.create_issue_page.create_issue(self.project_name, self.issue_type, summary=None,
                                                description=self.description, priority=self.priority, assignee=self.assignee)
        with allure.step('Check that creation is failed & error message displayed'):
            assert self.create_issue_page.is_submission_error_displayed()
        self.create_issue_page.attach_allure_screenshot("missed summary.png")
        self.create_issue_page.click_cancel_button()
        self.create_issue_page.accept_alert()
        time.sleep(1)

    @allure.tag("UI")
    @allure.title('Try to create issue with the summary longer then supported')
    def test_exceeded_summary_length(self):
        self.create_issue_page.create_issue(None, None, self.exceeded_summary, None, None, None)
        with allure.step('Check that creation is failed & error message displayed'):
            assert self.create_issue_page.is_submission_error_displayed()
        self.create_issue_page.attach_allure_screenshot("exceeded summary error.png")
        self.create_issue_page.click_cancel_button()
        self.create_issue_page.accept_alert()
        time.sleep(1)

    @allure.tag("UI")
    @allure.title('Cancel issue creation via click Cancel button')
    def test_cancel_create_issue(self):
        self.create_issue_page.click_cancel_button()
