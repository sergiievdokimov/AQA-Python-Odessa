import allure

from src.pages.issue_page import IssuePage
from src.pages.search_issues_page import SearchIssuesPage
from tests.base_test import BaseTest


class TestSearchIssue(BaseTest):

    valid_issue_id = "Webinar-3008"
    invalid_issue_id = "wrong id zzz"
    advanced_search_request = "reporter = SergiiIevdokymov and text ~ \"+To +be +removed\""

    def setup_method(self):
        self.search_issues_page = SearchIssuesPage(self.driver)
        self.issue_page = IssuePage(self.driver)
        self.dashboard_page.open_dashboard_page()

    @allure.tag("UI")
    @allure.title('Find the valid issue via quick search')
    def test_quick_search_one_issue(self):
        with allure.step('Perform a quick search with valid issue id'):
            self.dashboard_page.quick_search(self.valid_issue_id)
            assert self.issue_page.at_page()
        self.dashboard_page.attach_allure_screenshot("Target issue is found and opened.png")

    @allure.tag("UI")
    @allure.title('Find an invalid issue via quick search')
    def test_quick_search_no_issues(self):
        with allure.step('Perform quick search with invalid issue id'):
            self.dashboard_page.quick_search(self.invalid_issue_id)
            assert self.search_issues_page.is_empty_search_results()

    # 100% works locally but constantly fails on CI due to "Element is not clickable at this point" error (waits, sleep, scroll, full screen don't solve the problem)
    # def test_search_for_certain_issue(self):
    #     self.dashboard_page.open_search_issues_page()
    #     self.search_issues_page.search_issue_by_text_advanced_mode(self.advanced_search_request)
    #     assert self.search_issues_page.is_present_search_results()
