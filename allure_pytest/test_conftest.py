from selenium import webdriver



def test_conftest(driver):
    print("start test_conftest")
    driver.get("http://google.com")
    print("end test_conftest")