from selenium.webdriver.support.wait import WebDriverWait

class Base:
    def __init__(self,driver):
        self.driver = driver

    def find_element_o(self,loc,timeout=10,poll=0.5):
        """
        :param loc:
        :param timeout:
        :param poll:
        :return:
        """
        return WebDriverWait(self.driver,timeout,poll)\
            .until(lambda x: x.find_elemnt(*loc))

    def click_element(self,loc):
        """
        :param loc:
        :return:
        """
        self.find_element_o(loc)

    def input_element(self,loc,text):
        """
        :param loc:
        :param text:
        :return:
        """
        ele = self.find_element_o(loc)
        ele.clear()
        ele.send_keys(text)
