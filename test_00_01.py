import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

email_input = driver.find_element(By.ID, "ap_email")
email_input.send_keys("sona.ghukasyan@gmail.com")

continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

password_input = driver.find_element(By.ID, "ap_password")
password_input.send_keys("hasiko07")

signin_button = driver.find_element(By.ID, "signInSubmit")
signin_button.click()

time.sleep(5)

driver.quit()