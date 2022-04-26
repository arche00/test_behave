from appium import webdriver
from app.application import Application

def before_scenario(context, scenario):
    context.browser = webdriver.Remote("http://0.0.0.0:4723/wd/hub",
                                       desired_capabilities={"platformName": "Android",
                                                            "udid": "287860acb13f7ece",
                                                            "app": "/Users/classting/apk/com.Classting.apk",
                                                            "automationName": "Appium",
                                                            "newCommandTimeout": 300,
                                                            "appPackage": "com.Classting",
                                                            "appActivity": ".MainActivity"
                                                            })

    context.browser.implicitly_wait(30)

    context.app = Application(context.browser)


def after_scenario(context, scenario):
    context.browser.quit()