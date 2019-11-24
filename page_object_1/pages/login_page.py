from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url,"login no in url"
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        assert "Войти" in self.is_element_present(*LoginPageLocators.LOGIN_FORM), "The login form is not presented"
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        assert "Зарегистрироваться" in self.is_element_present(*LoginPageLocators.REGISTER_FORM), "The register form is not presented"
        assert True

