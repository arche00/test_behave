import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from features.pages.base_page import Page
from features.test_data import EMAIL, PASSWORD

class SignInEmailPage(Page):
    EMAIL_INPUT = (By.XPATH, "//android.view.View[1]/android.widget.EditText")
    PASSWORD_INPUT = (By.XPATH, "//android.view.View[2]/android.widget.EditText")
    SIGNIN_BTN = (By.XPATH, "//android.widget.Button[@text = '이메일로 로그인']")
    email = "teacher04@sharklasers.com"
    password = "a1234567"

    def login_with_email_and_password(self, email, password):
        time.sleep(15)

        self.input(email, self.EMAIL_INPUT)
        self.input(password, self.PASSWORD_INPUT)
        self.click_on_element(self.SIGNIN_BTN)
        time.sleep(15)