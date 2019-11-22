from selenium import  webdriver
import time

driver: webdriver = None


def setup_module():
    print("setup module")
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(3) # явное ожидание


def teardown_module():
    print("teardown")
    driver.close()

def test_module_setup_driver():
    print("test started")
    driver.get("http://google.com")
    time.sleep(3)
    assert True