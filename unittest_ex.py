
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MyTests(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome()
        print('In setup....')
    def test_testcase1(self):
        browser=self.browser
        browser.get('http://192.168.3.73:8080/login')
        user_field = browser.find_element_by_name('uname')
        pass_field = browser.find_element_by_name('pw')
        user_field.send_keys('abc')
        pass_field.send_keys('xyz')
        pass_field.send_keys(Keys.RETURN)
        assert 'log' in browser.title
        print('Test Case 1 Success')

    def test_testcase2(self):
        browser=self.browser
        browser.get('http://192.168.3.73:8080/login')
        user_field = browser.find_element_by_name('uname')
        pass_field = browser.find_element_by_name('pw')
        user_field.send_keys('abc')
        pass_field.send_keys('xyz')
        pass_field.send_keys(Keys.RETURN)
        assert 'log' in browser.title
        print('Test Case 2 Success')

    def test_testcase3(self):
        browser=self.browser
        browser.get('http://192.168.3.73:8080/login')
        user_field = browser.find_element_by_name('uname')
        pass_field = browser.find_element_by_name('pw')
        user_field.send_keys('abc')
        pass_field.send_keys('xyz')
        pass_field.send_keys(Keys.RETURN)
        assert 'log' in browser.title
        print('Test Case 3 Success')

    def tearDown(self):
        print('In Tear Down...')
        import time
        time.sleep(2)
        self.browser.close()

if __name__=='__main__':
    unittest.main()


