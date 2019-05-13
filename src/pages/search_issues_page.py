import time

from selenium.webdriver.common.action_chains import ActionChains
from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchIssuesPage(BasePage):

    SEARCH_TITLE = (By.CSS_SELECTOR, ".search-title")
    ADVANCED_MODE_SWITCHER = (By.CSS_SELECTOR, "[data-id='basic']")
    BASIC_MODE_SWITCHER = (By.CSS_SELECTOR, "[data-id='advanced']")
    SEARCH_TEXT_FIELD_ADVANCED_MODE = (By.ID, "advanced-search")
    SEARCH_TEXT_FIELD_BASIC_MODE = (By.ID, "searcher-query")
    SEARCH_BUTTON_SUBMIT = (By.CSS_SELECTOR, ".search-button")
    CHANGE_LAYOUT_BUTTON = (By.ID, "layout-switcher-button")
    DETAIL_VIEW_OPTION = (By.CSS_SELECTOR, ".aui-list-item-link")
    LIST_VIEW_OPTION = (By.ID, "")
    EMPTY_RESULTS_LIST = (By.CSS_SELECTOR, ".empty-results")
    NUMBER_OF_FOUND_ISSUES = (By.CSS_SELECTOR, ".results-count-text")

    def __init__(self, driver):
        self.driver = driver

    def switch_to_advanced_search_mode(self):
        if self.is_element_visible(self.ADVANCED_MODE_SWITCHER):
            self.driver.find_element(*self.ADVANCED_MODE_SWITCHER).click()

    def switch_to_basic_search_mode(self):
        if self.is_element_visible(self.BASIC_MODE_SWITCHER):
            self.driver.find_element(*self.BASIC_MODE_SWITCHER).click()

    def at_page(self):
        return self.is_element_visible(self.SEARCH_TITLE)

    def search_issue_by_text_basic_mode(self, search_text):
        self.switch_to_basic_search_mode()
        self.driver.find_element(*self.SEARCH_TEXT_FIELD_BASIC_MODE).send_keys(search_text)
        self.driver.find_element(*self.SEARCH_BUTTON_SUBMIT)

    def search_issue_by_text_advanced_mode(self, search_text):
        self.switch_to_advanced_search_mode()
        self.is_element_visible(self.SEARCH_BUTTON_SUBMIT)
        self.driver.find_element(*self.SEARCH_TEXT_FIELD_ADVANCED_MODE).click()
        self.driver.find_element(*self.SEARCH_TEXT_FIELD_ADVANCED_MODE).send_keys(search_text)
        self.is_element_visible(self.SEARCH_BUTTON_SUBMIT)
        self.driver.find_element(*self.SEARCH_BUTTON_SUBMIT).click()

    def is_empty_search_results(self):
        return self.is_element_visible(self.EMPTY_RESULTS_LIST)

    def is_present_search_results(self):
        return self.is_element_visible(self.NUMBER_OF_FOUND_ISSUES)

    def delete_issue(self):
        hover_over_button = ActionChains.move_to_element(self.driver.find_element(By.CSS_SELECTOR, ".aui-iconfont-more"))
        hover_over_button.perform()
        self.driver.find_element(By.ID, "actions_50157").click()
        self.driver.find_element(By.CSS_SELECTOR, ".issueaction-delete-issue").click()
        self.driver.switch_to_alert().accept()
