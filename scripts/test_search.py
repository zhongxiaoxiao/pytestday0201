import sys,os
sys.path.append(os.getcwd())
from Base.InitDriver import init_driver
from Base.Read_Data import ret_yaml_data
import pytest

def yaml_data():
    data_list = []
    data = ret_yaml_data("search_data").get("Search_Data")
    for i in data.keys():
        data_list.append((i,data.get(i).get("test"),data.get(i).get("expect_data")))
    return data_list

class Test_Search_Page:
    def setup_class(self):
        self.driver = init_driver()
    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("test_num,text,expect_data",yaml_data())
    def test_input_text(self,test_num,text,expect_data):
        print("用例编号:",test_num)
        self.driver.get_screenshot_as_file("./screen/%s.png" % test_num)
        assert expect_data == 456