import unittest
from selenium import webdriver
from pages_.loginPage import LogInPage
from time import sleep
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener


class TestLogIn(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fsign%2Fs%3Fk%3Dsign%2Bin%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")


    def test_logIn(self):
        #test Amazon Log in with valid data

        self.logInPageObj = LogInPage(self.driver)
        self.logInPageObj.fill_username_field("jenyakirakosyan27@gmail.com")
        self.logInPageObj.click_to_continue_button()
        self.logInPageObj.fill_password_fild("//eva[@tsaturyan]")
        sleep(5) # Added sleep time to avoid captcha from amazon
        self.logInPageObj.click_to_signin_button()

    def test_logIn_with_invalid_password(self):
        self.logInPageObj = LogInPage(self.driver)
        self.logInPageObj.fill_username_field("jenyakirakosyan27@gmail.com")
        self.logInPageObj.click_to_continue_button()
        self.logInPageObj.fill_password_fild("WrongPassword")
        sleep(5) # Added sleep time to avoid captcha from amazon
        self.logInPageObj.click_to_signin_button()
        self.logInPageObj.validate_incorrect_password_alert()


    def tearDown(self):
        self.driver.close()

