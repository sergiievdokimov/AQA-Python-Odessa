import time
import allure

from src.pages.issue_page import IssuePage
from tests.base_test import BaseTest


class TestUpdateIssue(BaseTest):

    UPDATED_SUMMARY = "Updated summary"
    UPDATED_DESCRIPTION = "Updated description"
    UPDATED_ISSUETYPE = "Bug"
    UPDATED_PROJECT = "WEBINAR"
    UPDATED_PRIORITY = "Low"
    UPDATED_ASSIGNEE = "Unassigned"

    def setup_method(self):
        self.dashboard_page.quick_search("webinar-3008")
        self.issue_page = IssuePage(self.driver)

    @allure.tag("UI")
    @allure.title('Update summary of the issue')
    def test_update_summary(self):
        self.issue_page.set_summary(self.UPDATED_SUMMARY)
        time.sleep(0.2)
        assert self.issue_page.get_summary() == self.UPDATED_SUMMARY

    @allure.tag("UI")
    @allure.title('Update priority of the issue')
    def test_update_priority(self):
        self.issue_page.set_priority(self.UPDATED_PRIORITY)
        time.sleep(0.2)
        assert self.issue_page.get_priority() == self.UPDATED_PRIORITY

    @allure.tag("UI")
    @allure.title('Update assignee of the issue')
    def test_update_assignee(self):
        self.issue_page.set_assignee(self.UPDATED_ASSIGNEE)
        time.sleep(0.2)
        assert self.issue_page.get_assignee() == self.UPDATED_ASSIGNEE
