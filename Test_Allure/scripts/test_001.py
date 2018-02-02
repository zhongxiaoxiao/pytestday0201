import pytest,allure
class Test_Abc:
    def setup(self):
        pass
    def teardown(self):
        pass
    @allure.step(title="第一个测试")
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_al(self):
        allure.attach("这是一个描述","试一下")
        assert 0
