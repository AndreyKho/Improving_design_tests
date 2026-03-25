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

@pytest.mark.parametrize('links', ["https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, links):
    page = ProductPage(browser, links)
    page.open()
    page.get_product_name()
    page.get_product_price()
    
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    
    page.should_be_add_to_basket_success_message()
    page.should_be_product_name_in_success_message()
    page.should_be_basket_total_equal_to_product_price()

@pytest.mark.xfail    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()

    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail    
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

#Задание: наследование и отрицательные проверки
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