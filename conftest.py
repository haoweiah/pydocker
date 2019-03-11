import pytest
import uiautomator2 as u2
import subprocess
import time

number="17521125085"
passwd="qw121234"

def log_in(d):
    d.

@pytest.fixture(scope="session")
def driver():
    with subprocess.Popen("adb get-serialno", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as adb_check:
        adb_status, _ = adb_check.communicate()
        print(adb_status.decode())
        if not adb_status:
            print("设备未连接")
            assert False
        
        d = u2.connect_usb("3578ea5c")

        if not d.info.get("screenOn"):
            d.screen_on()
        for _ in range(3):
            d.unlock()
            time.sleep(1)
            d(text="4").click_gone()
        if "com.github.uiautomator" in d.current_app().values():
            d.press("home")

    yield d
    d.app_stop_all()
    d.screen_off()        

