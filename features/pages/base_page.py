class Page:
    def __init__(self, driver):
        self.driver = driver
        #self.action = ActionChains(self.driver)

    def find_elements(self, locator):
        return self.driver.find_elements(by=locator[0],
                                         value=locator[1])

    def find_element(self, locator):
        return self.driver.find_element(by=locator[0],
                                        value=locator[1])

    def click_on_element(self, locator):
        element = self.driver.find_element(by=locator[0],
                                           value=locator[1])
        element.click()

    def input(self, text, locator):
        password_input = self.driver.find_element(by=locator[0],
                                                  value=locator[1])
        password_input.send_keys(text)

    def swipe_to_down(self, locator):
        self.driver.swipe(start_x=574, start_y=1896, end_x=562, end_y=938, duration=300)

    # def tap_element(self,locator):
    #
    #     element = self.driver.find_element(by=locator[0],
    #                                        value=locator[1])
    #
    #     self.action.move_to_element(element).click(element).perform()
