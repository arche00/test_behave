import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from features.pages.base_page import Page
from features.test_data import EMAIL, PASSWORD

class SignInEmailPage(Page):
    EMAIL_INPUT = (By.XPATH, "//android.view.View[1]/android.widget.EditText")
    PASSWORD_INPUT = (By.XPATH, "//android.view.View[2]/android.widget.EditText")
    SIGNIN_BTN = (By.XPATH, "//android.widget.Button[@text = '이메일로 로그인']")


    def login_with_email_and_password(self):
        time.sleep(10)

        self.input(EMAIL, self.EMAIL_INPUT)
        self.input(PASSWORD, self.PASSWORD_INPUT)
        self.click_on_element(self.SIGNIN_BTN)
        time.sleep(15)