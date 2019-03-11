import uiautomator2 as u2
import pytest
import time

package="com.bright.appgilpm"
activity="com.bright.applenry.MainActivity"
number="17521125085"
passwd="qw121234"



def test_searchbalance(driver):
    d = driver
    d.app_start(package)
    d(text="确定").click_exists(timeout=5)
    time.sleep(1)        
    if d(description="我的").click_exists():
        time.sleep(2)
        str_balance = d(className="android.view.View", instance=17).child()[1].info.get('contentDescription')
        print(str_balance)
        if 50 > float(str_balance):
            print("少于50元，当前金额：{}".format(str_balance))
        else:
            print("当前金额可以提现 {}".format(str_balance))


