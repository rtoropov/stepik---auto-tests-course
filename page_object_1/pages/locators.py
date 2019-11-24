from selenium.webdriver.common.by import By

class MainPageLocator():                         # каждый класс будет соответствовать каждому классу PajeObject
    LOGIN_LINK= (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM=(By.ID, "#login_form")
    REGISTER_FORM=(By.ID, "#register_form")

class ProductPageLocators():
    BASKER_FORM=(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary")
    NAME_BOOK=(By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRICE_BOOK=(By.CSS_SELECTOR, ".col-sm-6.product_main > p[class=price_color]")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main > p[class=price_color]")

class BasePageLocators():
    LOGIN_LINK= (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")



