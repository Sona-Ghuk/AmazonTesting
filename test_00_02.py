import time
from selenium import webdriver
from pages_.loginPage import LoginPage
from pages_.navigationBar import NavigationBar
from pages_.cartPage import CartPage

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")

login_page = LoginPage(driver)
login_page.click_login_link()
login_page.fill_username_field("sona.ghukasyan@gmail.com")
login_page.click_continue_button()
login_page.fill_password_field("hasiko07")
time.sleep(5)
login_page.click_signin_button()

driver.get("https://www.amazon.com/gp/product/B077G7KHXC/ref=ox_sc_act_image_1?smid=ATVPDKIKX0DER&psc=1")

navigation_bar = NavigationBar(driver)
navigation_bar.click_to_cart_button()

cart_page = CartPage(driver)
cart_page.first_cart()

time.sleep(5)

driver.close()