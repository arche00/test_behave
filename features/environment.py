from appium import webdriver
from app.application import Application
from selenium.webdriver.common.action_chains import ActionChains
# from selenium import webdriver
import os, json


def before_scenario(context, scenario):
    context.browser = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_capabilities={
        "platformName": "Android",
        "udid": "R3CN50DKBJN",
        # office
        # "app": "/Users/classting/apk/com.Classting.apk",
        # home
        "app": "/Users/tj/apk/com.Classting.apk",
        "automationName": "Appium",
        "newCommandTimeout": 300,
        "noReset": "true",
        "appPackage": "com.Classting",
        "appActivity": ".MainActivity"})
    context.browser.implicitly_wait(15)


    context.action = ActionChains(context.browser)

    context.app = Application(context.browser)


def after_scenario(context, scenario):
    # Invoke driver.quit() after the test is done to indicate to BrowserStack
    # that the test is completed. Otherwise, test will appear as timed out on BrowserStack.
    context.browser.quit()


'''
config_file_path = os.path.join(os.path.dirname(__file__), '..', "config.json")
print("Path to the config file = %s" % (config_file_path))
with open(config_file_path) as config_file:
    CONFIG = json.load(config_file)

# Take user credentials from environment variables if they are defined
if 'BROWSERSTACK_USERNAME' in os.environ: CONFIG['capabilities']['browserstack.user'] = os.environ['BROWSERSTACK_USERNAME']
if 'BROWSERSTACK_ACCESS_KEY' in os.environ: CONFIG['capabilities']['browserstack.key'] = os.environ['BROWSERSTACK_ACCESS_KEY']

def before_feature(context, feature):
    desired_capabilities = CONFIG['capabilities']
    context.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://hub-cloud.browserstack.com/wd/hub"
    )
    context.action = ActionChains(context.browser)

    context.app = Application(context.browser)

def after_feature(context, feature):
    # Invoke driver.quit() after the test is done to indicate to BrowserStack
    # that the test is completed. Otherwise, test will appear as timed out on BrowserStack.
    context.browser.quit()
'''
