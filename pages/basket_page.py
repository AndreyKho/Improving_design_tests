from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage, BasketPageLocators):
    
    def should_be_empty_text_busket(self):
        basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT)
        assert "Ваша корзина пуста Продолжить покупки" in basket_text.text
    
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRUDUCT_IN_BASKET), "Корзина с товаром"