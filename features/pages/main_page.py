import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from features.pages.base_page import Page


class LaunchPage(Page):
    LOGIN_BTN = (By.XPATH, "//android.widget.TextView[@text = '로그인']")
    #SIGNUP_BTN = (By., "com.instagram.android:id/sign_up_with_email_or_phone")

    def login_with_existing_account(self):
        time.sleep(10)
        #self.WebDriverWait(driver, 15).until(EC.presence_of_element_located(self.LOGIN_BTN)
        self.click_on_element(self.LOGIN_BTN)
        time.sleep(10)

    # def create_new_account(self):
    #     self.click_on_element(self.BUTTON_CREATE_ACCOUNT)