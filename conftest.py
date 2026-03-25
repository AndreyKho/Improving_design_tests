"""
Назначение: Создаёт браузер для всех тестов
Содержит:
- Фикстуры (browser, api_client, db_connection)
- Глобальные настройки pytest
- Общие данные (base_url, users)
"""

import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    #driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def product_link():
    return "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.fixture
def main_link():
    return "https://selenium1py.pythonanywhere.com/"