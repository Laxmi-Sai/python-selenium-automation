from selenium import webdriver
from selenium.webdriver.common.by import By

Problem=2
Amazon_Logo=(By.XPATH, "//i[@class='a-icon a-icon-logo']")
Email=(By.XPATH, "//input[@type='email']")
Continue=(By.XPATH, "//input[@id='continue']")
Need_Help=(By.XPATH, "//span[@class='a-expander-prompt']")
Forgot_Password_link=(By.XPATH, "//a[@id='auth-fpp-link-bottom']")
Other_Issues_Link=(By.XPATH, "//a[@id='ap-other-signin-issues-link']")
Create_Amazon_Account_Button=(By.XPATH, "//a[@id='createAccountSubmit']")
Conditions=(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]")
Privacy_of_Notice=(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy')]")


