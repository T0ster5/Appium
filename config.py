from appium import webdriver
import pytest

@pytest.fixture(scope="session")
def setup_driver():

    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Android Emulator',
        'app': 'app-debug.apk',
        "appPackage": "ru.netology.testing.uiautomator"
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    yield driver

    driver.quit()