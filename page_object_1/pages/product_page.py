from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class PageObject():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_not_element_ptresent(self, how, what, timeout=4): # метод, проверяющий, что данный элемент не появится на странице в течение timeout
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def add_to_basket(self):
        # name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        # price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        basket_link = self.browser.find_element(*ProductPageLocators.BASKER_FORM)
        basket_link.click()

    # def is_disappeared(self):
    #     assert self.is_not_element_ptresent(*ProductPageLocators.SUCCESS_MESSAGE), "Succes message is presented, but should not be "

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # def add_to_basket2(self):
    #     name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
    #     price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
    #     if name_book and price_book is not None:
    #         assert name_book.text == "Coders at Work"
    #         assert price_book == "19,99 £"
    #         basket_link = self.browser.find_element(*ProductPageLocators.BASKER_FORM)
    #         basket_link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")