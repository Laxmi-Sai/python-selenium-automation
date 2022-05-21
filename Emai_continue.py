from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\sunsa\\python-selenium-automation\\chromedriver.exe')
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
#By.XPATH
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
driver.find_element(By.XPATH, "//input[@type='email']").send_keys('sunsailaxmi24@yahoo.com')
#By ID
driver.find_element(By.XPATH, "//input[@id='continue']").click()
#By XPATH
driver.find_element(By.XPATH, "//input[@type='password']").send_keys('selenium!')

#By ID
driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()

expected_result = (By.XPATH, "//a[@href='/ref=nav_logo']")
actual_result = driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo']")
assert  expected_result == actual_result, f'Error! Actual result {actual_result} does not match expected {expected_result}'

print('Test case passed')

driver.quit()