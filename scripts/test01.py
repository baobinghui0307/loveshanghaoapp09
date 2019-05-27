import  allure, pytest
class TestA:
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="测试步骤1")
    def test001(self):
        print("你好")
        allure.attach("测试1","对测试1的描述")
        allure.attach("用户名", "admin")
        allure.attach("密码", "123456")
        assert True


    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="测试步骤2")
    def test002(self):
        print("你好呀")
        allure.attach("测试2","对测试2的描述")
        with open("./text.PNG", "rb") as f:
            allure.attach("截图",f.read(),allure.attach_type.PNG)

            assert True