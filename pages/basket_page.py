from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage, BasketPageLocators):
    
    def should_be_empty_text_busket(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT)
        
    
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRUDUCT_IN_BASKET), "Корзина с товаром"