#selenium is a library for web app testing
'''
Test case:
Open browser->type url->find field->type usr,pswd->press enter->verify
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome()
#download the chrome driver and keep it in the bin
browser.get('http://192.168.3.73:8080/login')
user_field=browser.find_element_by_name('uname')
pass_field=browser.find_element_by_name('pw')
user_field.send_keys('abc')
pass_field.send_keys('xyz')
pass_field.send_keys(Keys.RETURN)
assert 'log' in browser.title
print('Test Case Success')
import time
time.sleep(2)
browser.close()