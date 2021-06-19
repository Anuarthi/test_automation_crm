import unittest
import time
import sys
sys.path.append("C:/Users/RAHUL/Documents/CRM automation/")
from selenium import webdriver
from PageObjects.login import login
from selenium.webdriver.common.by import By

class customersTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = login.base_url
        print(cls.base_url)
        cls.driver = webdriver.Chrome(executable_path="Driver\chromedriver.exe")

    def setUp(self):
        self.driver.maximize_window()
        print(self.base_url)
        self.driver.get(self.base_url)
        # time.sleep(3)

    def test_1_2_10_12_verify_ui(self):
        self.login_page()
        get_url = self.driver.current_url
        

    def login_page(self):
        # Set values into login page
        self.login = login(self.driver)
        login.login_page(self.login, "ocd", "john" , "12345")

    def logout_page(self):
        # logout the page
        login.logout_page(self.login)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()