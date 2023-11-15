from selenium.webdriver.common.by import By
from selenium import webdriver
from pages_.basePage import BasePage


class NavigationBar(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.__cartButtonLocator = (By.ID, "nav-cart-count-container")
        self.__textFieldLocator = (By.NAME, "field-keywords")
        self.__searchButtonLocator = (By.ID, "nav-search-submit-button")

    def click_to_cart_button(self):
        cartButtonElement = self._find_element(self.__cartButtonLocator)
        self._click_to_element(cartButtonElement)

    def fill_search_field(self, searchElement):
        textFieldElement = self._find_element(self.__textFieldLocator)
        self._fill_field(textFieldElement, searchElement)

    def click_to_search_button(self):
        searchButtonElement = self._find_element(self.__searchButtonLocator)
        self._click_to_element(searchButtonElement)
