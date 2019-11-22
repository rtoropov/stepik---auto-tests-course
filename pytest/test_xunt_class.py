from selenium import webdriver

class TestXunitClass:

    def setup_method(self):
        print("setup")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_method(self):
        print("teardown")
        self.driver.close()

    def test_xunit_class(self):
        print("test started")
        self.driver.get("http://google.com")
        assert True


    def test_xunit_class_2(self):
        print("test 2 started")
        self.driver.get("http://yandex.ru")
        assert self.driver.title == "Яндекс"