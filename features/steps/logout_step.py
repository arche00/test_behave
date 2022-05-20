from behave import given, when, then
from appium import webdriver
from selenium.webdriver.common.by import By
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("나는 앱을 열고 MY탭을 클릭한다")
def click_mytab(context):
    #MYTAB = context.browser.find_element(By.XPATH, "//android.widget.TextView[@text = 'MY']")
    #
    # context.action.move_to_element(MYTAB).click(MYTAB).perform()
    context.app.main_page.move_to_mytab()
@when("설정으로 이동한다")
def click_setting_btn(context):
    context.app.setting_page.move_to_setting()

@step("로그아웃을 클릭힌다")
def click_signout_btn(context):
    context.app.setting_page.sign_out()

@then("로그아웃이 완료되면 메인화면으로 이동한다")
def check_if_element_is_visible(context):
    context.app.launch_page.check_if_element_is_visible()