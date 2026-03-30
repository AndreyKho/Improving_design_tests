from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUSKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators:
    REGISTRATION_EMAIL_FILD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FILD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2_FILD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form > .btn")

class MainPageLocators:
    pass    


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    PRUDUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")

class ProductPageLocators:
    # Локаторы как константы класса
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    SUCCESS_MESSAGE_NAME = (By.CSS_SELECTOR, "#messages > div.alert-success > div.alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages > div.alert-info > div.alertinner > p > strong")