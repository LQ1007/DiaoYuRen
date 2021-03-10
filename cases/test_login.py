from test_data.data_for_login import success_data
from run import logger
import pytest
from test_data.data_for_login import failed_data
from time import sleep
import allure


@pytest.fixture(scope='module')
def prepare_to_login(handler):
    handler[1].go_to_login_page()


@allure.epic('钓鱼人APP自动化测试')
@allure.feature('钓鱼人APP自动化测试-登录模块')
@pytest.mark.usefixtures('prepare_to_login')
class TestLogin:
    @allure.story('钓鱼人APP自动化测试-登录模块-正向用例测试')
    @allure.title('登录正向用例测试')
    @pytest.mark.last
    def test_login_success(self, handler):
        logger.info('=========================开始执行正向用例==============')
        handler[1].login(success_data['username'], success_data['password'])
        logger.info('登录操作完成')
        sleep(3)
        assert handler[1].is_nickname_exists()
        logger.info('==================正向用例测试通过:pass======================')
        handler[1].save_picture('正向用例测试截图')

    @allure.story('钓鱼人APP自动化测试-登录模块-反向用例测试')
    @allure.title('登录反向用例测试')
    @pytest.mark.parametrize('data',failed_data)
    def test_login_failed(self, handler, data):
        logger.info('开始执行反向测试用例：{}'.format(data['name']))
        handler[1].login(data['username'], data['password'])
        logger.info('登录操作完成')
        assert handler[1].is_toast_show(data['error_mag'])
        handler[1].save_picture(data['name'])



