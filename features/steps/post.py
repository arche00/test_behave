from behave import given, when, then, step
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@when("나는 클래스홈으로 이동한다")
def move_to_classhome(context):
    CLASSLIST = (By.XPATH, "//android.widget.TextView[@text = '전체 클래스 >']")
    context.app.main_page.move_to_classtab()
    context.app.main_page.move_to_classhome()

@when('글쓰기를 선택한다')
def click_write_btn(context):
    write_btn = (By.XPATH, "//android.view.View[2]/android.widget.Image")

    # context.app.base_page.wait_for_element(write_btn)
    # ele = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located(write_btn))
    context.app.base_page.wait_for_element(write_btn)
    context.app.main_page.click_write_btn(write_btn)

@when('텍스트를 입력하고 완료를 클릭한다')
def type_text_and_submit(context):
    field = (By.XPATH, "//android.widget.EditText[@text = '본문을 입력하세요.\n']")
    submit = (By.XPATH, "//android.widget.Button[@text = '게시']")
    close_btn = (By.XPATH, "//android.widget.Button[@text = 'Close']")

    context.app.base_page.input(1234,field)
    context.app.base_page.swipe_to_down()
    context.app.base_page.click_on_element(submit)
    context.app.base_page.click_on_element(close_btn)

@then('글쓰기가 완료되면 작성한 게시글이 게시된다')
def check_post_displayed(context):
    pass