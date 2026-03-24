from selenium.webdriver.common.by import By

class ProductPageLocators:
    # Локаторы как константы класса
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '[value="Добавить в корзину"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    SUCCESS_MESSAGE_NAME = (By.CSS_SELECTOR, "#messages > div.alert-success > div.alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages > div.alert-info > div.alertinner > p > strong")