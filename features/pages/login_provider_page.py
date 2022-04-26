import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages.base_page import Page


class ProviderPage(Page):
    SIGNIN_EMAIL = (By.XPATH, "//android.widget.TextView[@text = '이메일로 로그인']")

    def sign_in_email_account(self):
        self.click_on_element(self.SIGNIN_EMAIL)
        time.sleep(10)


