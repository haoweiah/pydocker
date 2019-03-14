# coding=utf-8

import time
import pytest

name = "17521125085"
passwd = "qw121234"

def extract_money(d, str_balance):
    assert d(description=u"立即提现").click_exists(), "点击立即取现按钮失败"
    d(resourceId="money").set_text(" ")
    d.shell(["input", "text", str_balance])
    assert str(str_balance) in d(resourceId="money").info.values(), "输入金额失败"
    d(resourceId="cash").click()


def login(d):
    d(resourceId="mobile").set_text(" ")
    time.sleep(1)
    d.shell(["input", "text", name])
    time.sleep(2)
    d.shell(["input", "keyevent", "61"])
    time.sleep(4)
    d.shell(["input", "text", passwd])
    time.sleep(4)
    d(resourceId="login").click()
