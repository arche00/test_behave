from selenium.webdriver.common.by import By
from features.pages.base_page import Page

def compare_data_with_expected(expected, real):
    assert expected == real, "Expected '{}', but got '{}'".format(expected, real)

class MainPage(Page):
    