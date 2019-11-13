from time import sleep

import autoit
from selenium.webdriver import ActionChains


def test_input(driver):
    driver.get("http://ui.yansl.com/#/input")
    sleep(2)

    input = driver.find_element_by_xpath("//input[@name='t1']")
    #清空
    input.clear()
    #输入
    input.send_keys("小鲁，你好骚啊")
    sleep(2)


def test_rabio(driver):
    driver.get("http://ui.yansl.com/#/radio")
    sleep(2)

    radio = driver.find_element_by_xpath("//input[@name='sex'][2]")
    radio.click()
    sleep(2)

def test_select(driver):
    driver.get("http://ui.yansl.com/#/select")
    sleep(2)
    #点击
    radio = driver.find_element_by_xpath("//*[@id='form']/form/div[3]/div/div/div[2]/input")
    radio.click()
    sleep(2)
    option = driver.find_element_by_xpath("(//span[text()='双皮奶'])[last()]")
    actions = ActionChains(driver)
    actions.move_to_element(option).perform()
    sleep(2)
    option.click()
    sleep(2)

def test_slider(driver):
    driver.get("http://ui.yansl.com/#/slider")
    sleep(2)
    #点击
    slider = driver.find_element_by_xpath("(//div[@class='el-tooltip el-slider__button'])[last()]")
    slider.click()
    sleep(2)
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(slider,0,-200).perform()
    sleep(2)

#时间
def test_time(driver):
    driver.get("http://ui.yansl.com/#/dateTime")
    sleep(2)

    t1 = driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div[2]/div/div/input")
    #清空
    t1.clear()
    #输入
    t1.send_keys("14:17;00")
    sleep(2)
#文件
def test_upload(driver):
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)

    upload = driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div/input")
    #清空
    upload.clear()
    #输入
    upload.send_keys("c:\\Users\guoya\\Desktop\\178847431362956833.png")
    sleep(2)

#点击上传
def test_upload2(driver):
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)
    upload = driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/div[1]/button/span")
    upload.click()
    sleep(2)
    autoit.win_wait("打开", 10)
    sleep(1)
    # autoit.control_send("打开", "Edit1", os.path.abspath(file_path))
    autoit.control_set_text("打开", "Edit1", "c:\\Users\guoya\\Desktop\\178847431362956833.png")
    sleep(2)
    autoit.control_click("打开", "Button1")
