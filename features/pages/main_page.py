import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from features.pages.base_page import Page


def compare_data_with_expected(expected, real):
    assert expected == real, "Expected '{}', but got '{}'".format(expected, real)

class MainPage(Page):
    MYTAB = (By.XPATH, "//android.widget.TextView[@text = 'MY']" )
    CLASSTAB = (By.XPATH, "//android.widget.TextView[@text = '클래스']")
    FEEDTAB = (By.XPATH, "//android.widget.TextView[@text = '소식']")

    def move_to_mytab(self):
        time.sleep(5)
        self.tap_element(self.MYTAB)
        time.sleep(5)

    def move_to_classtab(self):
        time.sleep(5)
        self.tap_element(self.CLASSTAB)
        time.sleep(5)

    def move_to_feedtab(self):
        time.sleep(5)
        self.tap_element(self.FEEDTAB)
        time.sleep(5)

class ClassHome(MainPage):
    CLASSLIST = (By.XPATH, "//android.widget.TextView[@text = '전체 클래스 >']")
    el = (By.XPATH, "//android.widget.TextView[@text = '테스트클래스04']")
    #//android.widget.TextView[@text = '테스트클래스04']
    #//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ImageView
    def move_to_classhome(self):
        time.sleep(5)
        self.tap_element(self.CLASSLIST)
        time.sleep(5)
        self.click_on_element(self.el)
        time.sleep(5)

    def click_write_btn(self, write_btn):
        time.sleep(5)
        # self.tap_element(write_btn)
        self.click_on_element(write_btn)
        time.sleep(5)

    def select_post_type(self,type):
        time.sleep(2)
        self.click_on_element(type)
        time.sleep(2)



