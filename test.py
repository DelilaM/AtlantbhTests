from calendar import month
import email
import time

from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')  

driver.get('http://automationpractice.com/index.php');

driver.implicitly_wait(10)

sign_box = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
sign_box.send_keys('ChromeDriver')
sign_box.click()

driver.implicitly_wait(10)

emailaddress_box = driver.find_element_by_id("email")
emailaddress_box.send_keys('mustaficdelila123@gmail.com')

password_box = driver.find_element_by_id("passwd")
password_box.send_keys('delila')

signin_button = driver.find_element_by_id("SubmitLogin")
signin_button.click()

driver.implicitly_wait(10)

search_box = driver.find_element_by_id("search_query_top")
search_box.send_keys('dress')

search_button = driver.find_element_by_xpath('//*[@id="searchbox"]/button')
search_button.click()

search_result = driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[2]')
print(search_result.text)

if(search_result.text == '7 results have been found.'):
    print('Test passed')
else:
    print('Test not passed')

driver.implicitly_wait(10)

driver.implicitly_wait(10)

time.sleep(5)

driver.quit()