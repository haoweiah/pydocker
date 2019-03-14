import uiautomator2 as u2
import pytest
import time
from extract import extract_money, login

import logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s:%(name)s_%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

package="com.bright.appgilpm"
activity="com.bright.applenry.MainActivity"


def test_searchbalance(driver):
    d = driver
    d.app_start(package)
    if d(resourceId="mobile").exists(timeout=10):
        login(d)
    logger.info("d.app_start('%s')"%package)
    time.sleep(5)
    d.click(0.500, 0.680)
    if d(description="我的").click_exists(timeout=10):
        logger.info("点击我的按钮")
        time.sleep(2)
        str_balance = d(className="android.view.View", instance=17).child()[1].info.get('contentDescription')
        logger.info(str_balance)
        if 100 > float(str_balance):
            logger.info("少于100元，当前金额：{}".format(str_balance))
        else:
            extract_money(d, str_balance)

