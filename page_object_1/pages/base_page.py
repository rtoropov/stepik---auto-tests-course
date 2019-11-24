from selenium.common.exceptions import  NoSuchElementException
import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import  BasePageLocators


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def __init(self, browser, url, timeout=10): # добавим команду для неявного ожидания со значением по умолчанию = 10
        self.browser = browser
        self.url = url
        self.browser.implicity_wait(timeout)

    def is_element_present(self, how, what): # перехватываем исключение. аргументы как искать (тип селектора)  и что искать (строку селектор)
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_ptresent(self, how, what, timeout=4): # метод, проверяющий, что данный элемент не появится на странице в течение timeout
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
