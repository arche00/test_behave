from features.pages.main_page import LaunchPage
from features.pages.login_provider_page import ProviderPage
from features.pages.singin_email_page import SignInEmailPage


class Application:
    def __init__(self, browser):
        self.main_page = LaunchPage(browser)
        self.login_provider_page = ProviderPage(browser)
        self.signin_email_page = SignInEmailPage(browser)


