from behave import given, when, then
from appium import webdriver
from selenium.webdriver.common.by import By
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("나는 앱을 열고 로그인을 클릭한다")
def open_login_page(context):
    context.app.main_page.login_with_existing_account()

@when('로그인 선택에서 이메일로 로그인을 선택한다')
def sign_in_email_account(context):
    context.app.login_provider_page.sign_in_email_account()

@when("{email} 과 {password} 를 입력하고 로그인한다")
def login_with_email_and_password(context, email, password ):
    context.app.signin_email_page.login_with_email_and_password(email=email, password=password)

