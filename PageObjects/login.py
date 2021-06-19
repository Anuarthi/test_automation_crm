import time
from selenium.webdriver.common.by import By


class login:
    base_url = "https://sadiq.oneclickdrive.com/login"

    textbox_companyname_xpath = "//*[@id='companyname']"
    textbox_username_xpath = "//*[@id='username']"
    textbox_password_id = "//*[@id='password']"
    button_loginIn_xpath = "//*[@id='user_login']"
    # logout
    button_logOut_xpath = "/html/body/div[3]/button"

    def __init__(self, driver):
        self.driver = driver

    def get_companyname(self):
        return self.driver.find_element(By.XPATH, self.textbox_companyname_xpath)

    def set_companyname(self , companyname):
        self.get_companyname().send_keys(companyname)

    def get_username(self):
        return self.driver.find_element(By.XPATH, self.textbox_username_xpath)
    
    def set_username(self, username):
        self.get_username().send_keys(username)

    def get_password(self):
        return self.driver.find_element(By.XPATH, self.textbox_password_id)

    def set_password(self, password):
        self.get_password().send_keys(password)

    def get_logIn_button(self):
        return self.driver.find_element(By.XPATH, self.button_loginIn_xpath)

    def get_logOut_button(self):
        return self.driver.find_element(By.XPATH, self.button_logOut_xpath)

    def login_page(login, companyname, username , password):
        # Set values into login page
        login.get_companyname().click()
        login.set_companyname(companyname)
        login.get_username().click()
        login.set_username(username)
        login.get_password().click()
        login.set_password(password)
        time.sleep(5)
        login.get_logIn_button().click()

    def logout_page(login):
        # logout the page
        login.get_logOut_button().click()