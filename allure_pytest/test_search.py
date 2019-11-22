import pytest
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType  # какой тип скриншота хотим сделать
import time


class TestPageSetup:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()
    '''
    severity - важность метода который мы используем 
    бывают blocker, critical, normal, minor, trivial
    '''

    @allure.feature("Open pages") # декоратор даёт доступ к пакету методов
    @allure.story("Открываем страницу google.com") # описываем что проверяет тест
    @allure.severity("blocker")      # важность метода
    def test_google_search(self):
        link = "https://www.google.ru/"
        self.driver.get(link)
        with allure.step("Делаем скриншот"):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screen", attachment_type=AttachmentType.PNG)
        assert self.driver.title == "Google"

    @allure.feature("Open pages")
    @allure.story("Открываем страницу yandex")
    @allure.severity("critical")
    def test_yandex_search(self):
        link = "https://www.yandex.ru/"
        self.driver.get(link)
        with allure.step("Делаем скриншот"):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screen", attachment_type=AttachmentType.PNG)
        assert self.driver.title == "Яндекс"

    @allure.feature("Open pages")
    @allure.feature("Открываем страницу yahoo")
    @allure.severity("minor")
    def test_yahoo_search(self):
        link = "https://www.yahoo.ru/"
        self.driver.get(link)
        with allure.step("Делаем скриншот"):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screen", attachment_type=AttachmentType.PNG)
        assert self.driver.title == "12"

#allure_pytest>py.test -sv --alluredir results test_search.py # создает папку results в которой будут репорты от прогона