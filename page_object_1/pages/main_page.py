from .base_page import BasePage # импортируем базовый класс
from selenium.webdriver.common.by import By
from .locators import MainPageLocator, BasePageLocators

class MainPage(BasePage): # делаем класс MainPage наследником класса BasePage, MainPage будет иметь доступ ко всем атрибутам и методам класса BasePage
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


