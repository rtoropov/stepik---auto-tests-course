from selenium import webdriver
import time
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


def test_fixture_pytest(driver):
    print("test started")
    driver.get("http://google.com")
    time.sleep(3)

