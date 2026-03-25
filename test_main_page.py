from pages.main_page import MainPage
from pages.basket_page import BasketPage

#Задание: наследование и отрицательные проверки
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, main_link):
    page = MainPage(browser, main_link)
    #Гость открывает главную страницу 
    page.open()
    #Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket()

    basket_page = BasketPage(browser, browser.current_url)
    #Ожидаем, что в корзине нет товаров
    basket_page.should_not_be_product_in_basket()
    #Ожидаем, что есть текст о том что корзина пуста 
    basket_page.should_be_empty_text_busket()
