from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.__firstProductDeleteButtonLocator = (By.XPATH, "(//input[@value = 'Delete'])[1]")
        self.__firstProductSaveForLaterButtonLocator = (By.XPATH, "(//input[@value='Save for later'])[1]")
        self.__allItemsDeselectFromCartLocator = (By.ID, "deselect-all")
    def delete_first_product_from_cart(self):
       firstProductDeleteButtonElement = self._find_element(self.__firstProductDeleteButtonLocator)
       self._click_to_element(firstProductDeleteButtonElement)

    def save_for_later_first_product_from_cart(self):
        firstProductSaveForLaterButtonElement = self._find_element(self.__firstProductSaveForLaterButtonLocator)
        self._click_to_element(firstProductSaveForLaterButtonElement)

    def deselect_all_items_from_cart(self):
        allItemsDeselectFromCartElement = self._find_element(self.__allItemsDeselectFromCartLocator)
