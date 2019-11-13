from asyncio import sleep

from selenium import webdriver
#休眠
#sleep(1)

def test_brower(driver):
    driver.get("http://www.baidu.com")
    sleep(1)
    driver.get("http://www.jd.com")
    #后退
    driver.back()
    sleep(2)
    #前进
    driver.forward()
    sleep(2)
    #刷新
    driver.refresh()
    sleep(2)
    #关闭浏览器
    driver.quit()