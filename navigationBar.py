from selenium.webdriver.common.by import By
from selenium import webdriver

class NavigationBar():
    def __init__(self, driver):
        self.driver = driver

    def click_to_cart_button(self):
        cart_button_element = self.driver.find_element(By.XPATH, "//span[@id='nav-cart-count']")
        cart_button_element.click()
