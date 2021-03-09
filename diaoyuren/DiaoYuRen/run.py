import pytest
import os
import sys
from common.bases.get_config import read_config
from common.bases.get_log import Log

BASE_DIR = os.path.dirname(__file__)

if sys.platform == 'win32':
    conf_file_path = os.path.join(BASE_DIR,'common/config/config.ini').replace('/','\\')
else:
    conf_file_path = os.path.join(BASE_DIR,'common/config/config.ini')

log_dir_path = read_config(conf_file_path,'log','log_dir_path')
img_dir_path = read_config(conf_file_path,'img','img_dir_path')
allure_results = read_config(conf_file_path, 'report', 'json_dir_path')
test_report = read_config(conf_file_path, 'report', 'html_dir_path')
logger = Log(log_dir_path)

if __name__ == '__main__':
    args = ['-s','-q','--alluredir', allure_results]
    self_args = sys.argv[1:]
    cmd = 'allure generate %s -o %s -c' % (allure_results, test_report)
    logger.info('========================开始执行测试用例=================')
    pytest.main(args + self_args)
    os.system(cmd)