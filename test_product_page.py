"""
Назначение: Сам тест
Содержит:
- Arrange (подготовка)
- Act (действия)
- Assert (проверки результата)
НЕ содержит: find_element, локаторы, Selenium-код.
"""

import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, product_with_code_links):
    page = ProductPage(browser, product_with_code_links)
    page.open()
    page.get_product_name()
    page.get_product_price()
    
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    
    page.should_be_add_to_basket_success_message()
    page.should_be_product_name_in_success_message()
    page.should_be_basket_total_equal_to_product_price()

@pytest.mark.xfail    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail    
def test_message_disappeared_after_adding_product_to_basket(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_to_basket()
    page.should_not_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

#Задание: наследование и отрицательные проверки
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, product_link):
    page = ProductPage(browser, product_link)
    #Гость открывает страницу товара
    page.open()
    #Переходит в корзину по кнопке в шапке 
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    #Ожидаем, что в корзине нет товаров
    basket_page.should_not_be_product_in_basket()
    #Ожидаем, что есть текст о том что корзина пуста 
    basket_page.should_be_empty_text_busket()

@pytest.mark.login
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, product_with_code_link):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page = ProductPage(browser, product_with_code_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, product_with_code_link):
        page = ProductPage(browser, product_with_code_link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, product_with_code_link):
        page = ProductPage(browser, product_with_code_link)
        page.open()
        page.get_product_name()
        page.get_product_price()
    
        page.add_to_basket()
        page.solve_quiz_and_get_code()
    
        page.should_be_add_to_basket_success_message()
        page.should_be_product_name_in_success_message()
        page.should_be_basket_total_equal_to_product_price()