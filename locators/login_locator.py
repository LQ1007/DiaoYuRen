#第一步  登录相关元素定义
from appium.webdriver.extensions.search_context import android
from selenium.webdriver.common.by import By


class LoginLocator:
    #页面元素定义
    fishman_account_text_loc = (By.ID, 'com.lchr.diaoyu:id/tv_account_login')
    username_input_loc = (By.ID, 'com.lchr.diaoyu:id/user_id')
    password_input_loc = (By.ID, 'com.lchr.diaoyu:id/passwd_id')
    login_btn_loc = (By.ID, 'com.lchr.diaoyu:id/btn_login')
    # agree_privacy_loc = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.CheckBox')


