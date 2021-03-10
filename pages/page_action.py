#第三步 登录页面内的操作
from common.bases.base_page import BassPage
from locators.login_locator import LoginLocator
from locators.main_page_locator import MainPageLocator
from locators.mine_page_locator import MinePageLocator
from locators.setting_page_locator import SettingPageLocator
from run import logger


class PageAction(BassPage):
    def login(self, username, password):
        self.send_data(LoginLocator.username_input_loc, username)
        self.send_data(LoginLocator.password_input_loc, password)
        self.click_element(LoginLocator.login_btn_loc)

    def go_to_me_page(self):
        self.click_element(MainPageLocator.me_icon_loc)
        self.sleep(3)

    # # 勾选用户协议
    # def checkbox_agree(self):
    #     self.search_element(LoginLocator.agree_privacy_loc).click()

    def is_user_login(self):
        '''

        :return: True为已登录，False为未登录
        '''
        try:
            if self.search_element(MinePageLocator.click_login_text_loc):
                return False
        except Exception as e:
            logger.info('未找到页面元素：{}'.format(MinePageLocator.click_login_text_loc))
            logger.error(e)
            return True

    def logout(self):
        try:
            self.click_element(MinePageLocator.setting_btn_loc)
            self.sleep(1)
            self.click_element(SettingPageLocator.logout_btn_loc)
            self.sleep(1)
            self.click_element(SettingPageLocator.logout_confirm_loc)
            self.sleep(3)
        except Exception as e:
            logger.warning('退出登录失败！')
            logger.warning(e)

    def is_nickname_exists(self):
        try:
            if self.search_element(MinePageLocator.nickname_loc):
                return True
        except Exception as e:
            logger.warning('未发现昵称：{}'.format(MinePageLocator.nickname_loc))
            logger.warning(e)
            return False

    def go_to_login_page(self):
        try:
            self.go_to_me_page()
            if self.is_user_login():
                self.logout()
            self.click_element(MinePageLocator.click_login_text_loc)
            self.sleep(2)
            self.click_element(LoginLocator.fishman_account_text_loc)
            self.sleep(2)
        except Exception as e:
            logger.warning('到登录页面失败')
            logger.warning(e)
