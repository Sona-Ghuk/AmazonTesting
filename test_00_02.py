import time
from selenium import webdriver
from pages_.loginPage import LoginPage
from pages_.navigationBar import NavigationBar
from pages_.cartPage import CartPage

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")

loginPage = LoginPage(driver)
loginPage.click_login_link()
loginPage.fill_username_field("sona.ghukasyan@gmail.com")
loginPage.click_continue_button()
loginPage.fill_password_field("hasiko07")
time.sleep(5)
loginPage.click_signin_button()

navigationBarObj = NavigationBar(driver)
navigationBarObj.click_to_cart_button()

cartPageObj = CartPage(driver)
cartPageObj.delete_firstProduct_from_cart()

time.sleep(5)

driver.quit()