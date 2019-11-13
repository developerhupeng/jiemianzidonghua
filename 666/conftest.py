from time import sleep

import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    # 打开浏览器
    driver = webdriver.Chrome("../chromer/chromedriver.exe")
    sleep(1)
    # 最大化浏览器窗口
    driver.maximize_window()
    sleep(1)
    yield driver
    driver.quit()