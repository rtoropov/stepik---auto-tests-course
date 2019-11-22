from selenium import webdriver
import pytest

@pytest.fixture
def driver(request):
    print("setup")
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    print("test")
    yield driver
    print("teardown")
    driver.quit()