from selenium.webdriver.common.by import By

class CartPage():
    def __init__(self, driver):
        self.driver = driver

    def first_cart(self):
        cart_icon = driver.find_element(By.ID, 'nav-cart')
        cart_icon.click()

    def first_cart(self):
        first_product_delete_button_element = self.driver.find_element(By.XPATH, "(//input[contains(@value, 'Delete')])[1]")
        first_product_delete_button_element.click()
