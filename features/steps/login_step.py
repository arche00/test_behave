from behave import given, when, then, step
from appium import webdriver
from selenium.webdriver.common.by import By
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def compare_data_with_expected(expected, real):
    assert expected == real, "Expected '{}', but got '{}'".format(expected, real)

@given("나는 앱을 열고 로그인을 클릭한다")
def open_login_page(context):
    context.app.launch_page.login_with_existing_account()

@when('로그인 선택에서 이메일로 로그인을 선택한다')
def sign_in_email_account(context):
    context.app.login_provider_page.sign_in_email_account()

@step("{email} 과 {password} 를 입력하고 로그인한다")
def login_with_email_and_password(context, email, password ):
    context.app.signin_email_page.login_with_email_and_password(email, password)

@then("로그인이 완료되면 소식탭으로 포커스가 된다")
def check_current_tab(context):
    FEEDTAB = (By.XPATH, "//android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.TextView")
    feedtab = context.app.base_page.find_element(FEEDTAB).get_attribute("text")
    compare_data_with_expected(expected="소식", real=feedtab)
