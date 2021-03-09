#第二步 基础类，基础方法封装
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
from run import img_dir_path
from run import logger
import time
from selenium.webdriver.common.by import By


class BassPage:
    def __init__(self, driver):
        self.driver = driver

    def sleep(self, s):
        time.sleep(s)

    #查找页面元素
    def search_element(self, locator):
        logger.info('python查找页面元素：{}'.format(locator))
        return self.driver.find_element(*locator)

    #点击
    def click_element(self, locator):
        logger.info('开始点击页面元素：{}'.format(locator))
        self.search_element(locator).click()

    #发送数据
    def send_data(self, locator, data):
        logger.info('开始向页面元素发送数据：{}'.format(locator))
        self.search_element(locator).send_keys(data)

    #等待页面元素出现
    def wait_element_visible(self, locator, msg=''):
        try:
            now = datetime.now()
            WebDriverWait(self.driver, 20).\
                until(EC.visibility_of_element_located(locator))
            end = datetime.now()
            cost_time = (end - now).total_seconds()
            logger.info('等待元素可见共耗时{}s：'.format(cost_time))
        except Exception as e:
            logger.error(e)

    #获取页面元素
    def get_element_text(self, locator, msg=''):
        self.wait_element_visible(locator, msg)
        return self.search_element(locator).text

    #截图
    def save_picture(self, msg=''):
        img_path = img_dir_path + '{0}-{1}.png'.format(msg, time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime()))
        try:
            self.driver.save_screenshot(img_path)
            logger.info('截图成功，图片保存路径为：{}'.format(img_path))
        except Exception as e:
            logger.info('截图失败')
            logger.info(e)

    #判断toast是否存在
    def is_toast_show(self, msg, timeout=20, poll_frequency=0.5):
        '''
        presence_of_element_located： 等待元素存在，在使用toast时调用，不可使用visibility_of_element_located，否则，无法正确判断toast
        :param msg: toast文本提示信息
        :param timeout: 超时时间
        :param poll_frequency:查询频率
        :return: True为找到了toast，False为未找到
        '''
        locator = (By.XPATH, "//*[contains(@text, '%s')]" % msg)
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator))
            logger.info('找到toast'.format(locator))
            self.save_picture('toast截图')
            return True
        except Exception as e:
            logger.error(e)
            logger.warning('查找toast:{}失败'.format(locator))
            self.save_picture('no_toast')
            return False

