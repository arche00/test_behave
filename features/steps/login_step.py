from behave import given, when, then
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("나는 앱을 열고 로그인에서 이메일로 로그인을 클릭한다")
def open_login_page(context):
    context.app.main_page.login_with_existing_account()

def sign_in_email_account(context):
    context.app.login_provider_page.sign_in_email_account()

@when("이메일과 비밀번호를 입력하고 로그인한다")
def login_with_email_and_password(context):
    context.app.signin_email_page.login_with_email_and_password()

