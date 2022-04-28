from features.pages.launch_page import LaunchPage
from features.pages.login_provider_page import ProviderPage
from features.pages.singin_email_page import SignInEmailPage
from features.pages.main_page import MainPage

class Application:
    def __init__(self, browser):
        self.launch_page = LaunchPage(browser)
        self.login_provider_page = ProviderPage(browser)
        self.signin_email_page = SignInEmailPage(browser)
        self.main_page = MainPage(browser)


