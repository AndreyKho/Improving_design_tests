"""
Назначение : Локаторы и методы страницы товара(конкретно эта страницы)
Содержит:
- Методы ЭТОЙ страницы:
  * Действия (клик, ввод текста)
  * Получение данных (текст, атрибуты)
  * Проверки ЭТОЙ страницы (assert-методы)
"""

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage, ProductPageLocators):
    #Добавление товара в коризну
    def add_to_basket(self):
        self.browser.find_element(*self.ADD_TO_BASKET_BUTTON).click()

    def get_product_name(self):
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def should_be_add_to_basket_success_message(self):
        assert self.is_element_present(*self.SUCCESS_MESSAGE), "No success message"

    def should_be_product_name_in_success_message(self):
        product_name = self.get_product_name()
        success_message_name = self.browser.find_element(*self.SUCCESS_MESSAGE_NAME).text
        assert product_name == success_message_name, "Product name mismatch"

    def should_be_basket_total_equal_to_product_price(self):
        product_price = self.get_product_price()
        basket_total = self.browser.find_element(*self.BASKET_TOTAL).text
        assert product_price in basket_total, "Basket total mismatch"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*self.SUCCESS_MESSAGE), \
         "Success message is presented, but should not be"
        
    def should_not_not_be_success_message(self):
        assert self.is_disappeared(*self.SUCCESS_MESSAGE), \
         "Success message is presented, but should not be"