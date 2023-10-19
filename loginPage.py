from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_login_link(self):
        login_link = self.driver.find_element(By.XPATH, "//a[@id='nav-link-accountList']")
        login_link.click()

    def fill_username_field(self, email):
        email_input = self.driver.find_element(By.ID, "ap_email")
        email_input.send_keys(email)

    def click_continue_button(self):
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

    def fill_password_field(self, password):
        password_input = self.driver.find_element(By.ID, "ap_password")
        password_input.send_keys(password)

    def click_signin_button(self):
        signin_button = self.driver.find_element(By.ID, "signInSubmit")
        signin_button.click()
