from appium import webdriver
from app.application import Application

def before_scenario(context, scenario):
    context.browser = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_capabilities={
        "platformName": "Android",
        "udid": "R3CN50DKBJN",
        "app": "/Users/tj/apk/com.Classting.apk",
        "automationName": "Appium",
        "newCommandTimeout": 300,
        "appPackage": "com.Classting",
        "appActivity": ".MainActivity"})
    context.browser.implicitly_wait(15)

    context.app = Application(context.browser)

def after_scenario(context, scenario):
    # Invoke driver.quit() after the test is done to indicate to BrowserStack
    # that the test is completed. Otherwise, test will appear as timed out on BrowserStack.
    context.browser.quit()