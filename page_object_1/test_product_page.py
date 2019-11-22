from .pages.product_page import PageObject
from .pages.base_page import BasePage
import pytest
from splinter import

# def test_guest_can_add_product_to_basket(browser):
#     link ="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = PageObject(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
# #Your code: Поздравляем, вы справились! Вставьте это число в поле ответа на Stepik: 27.21914760814995
#
#
# def test_guest_can_add_product_to_basket2(browser):
#     link =" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = PageObject(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()

@pytest.mark.parametrize("promo_offer", ["0","1", "3", "4", "5", "6", "7", "8", "9"])
# class TestLoginFromMainPage():
def test_guest_can_add_product_to_basket( browser, promo_offer):

    link = ('http://selenium1py.pythonanywhere.com/catalogue/''coders-at-work_207/?promo=offer{}'.format(promo_offer))
    page = PageObject(browser, link)

    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()


