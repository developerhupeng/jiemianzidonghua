from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #定义了变量EC表示expected_conditions


import autoit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
#纯文本
#取出公共变量driver（打开浏览器）
def test_input(driver):
    #打来浏览器获取IP地址http://ui.yansl.com/#/input
    driver.get("http://ui.yansl.com/#/input")
    #停留2秒钟
    sleep(2)
    #取input为变量名，定位浏览器文本元素的位置
    input = driver.find_element_by_xpath("//input[@name='t1']")
    #清空输入框
    input.clear()
    #输入数据
    input.send_keys("小鲁，你好骚啊")
    #停留2秒
    sleep(2)
#单选框
#取出公共变量driver（打开浏览器）
def test_rabio(driver):
    #打开浏览器获取地址
    driver.get("http://ui.yansl.com/#/radio")
    #停留2秒
    sleep(2)
    #取radio为变量名，打开浏览器并定位点击元素的位置
    radio = driver.find_element_by_xpath("//input[@name='sex'][2]")
    #进行点击
    radio.click()
    #停留2秒
    sleep(2)
#下拉框
#取出公共变量driver（打开浏览器）
def test_select(driver):
    #打开浏览器并获取它的ip
    driver.get("http://ui.yansl.com/#/select")
    #进入网页后停留2秒
    sleep(2)
    #定位元素位置
    radio = driver.find_element_by_xpath("//*[@id='form']/form/div[3]/div/div/div[2]/input")
    #进行点击
    radio.click()
    #停留2秒
    sleep(2)
    #接着定位元素
    option = driver.find_element_by_xpath("(//span[text()='双皮奶'])[last()]")
    #取变量，把鼠标点击浏览器的功能给变量
    actions = ActionChains(driver)
    #在赋值变量中模仿鼠标运行点击变量option（双皮奶）接着继续运行一下
    actions.move_to_element(option).perform()
    #停留2秒
    sleep(2)
    #进行点击
    option.click()
    #停留2秒
    sleep(2)
#模块
def test_slider(driver):
    driver.get("http://ui.yansl.com/#/slider")
    sleep(2)
    #点击
    slider = driver.find_element_by_xpath("(//div[@class='el-tooltip el-slider__button'])[last()]")
    slider.click()
    sleep(2)
    actions = ActionChains(driver)
    #模仿鼠标滑动，拖动
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
#窗口切换
def test_windows(driver):
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    sleep(2)

    dang_dang = driver.find_element_by_link_text("当当")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dang_dang).key_up(Keys.CONTROL).perform()
    sleep(2)
    jd = driver.find_element_by_link_text("京东")
    actions = ActionChains(driver)
    #抬起鼠标，点击京东，运行京东
    actions.key_down(Keys.CONTROL).click(jd).key_up(Keys.CONTROL).perform()
    sleep(2)
    dn = driver.find_element_by_partial_link_text("度娘")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dn).key_up(Keys.CONTROL).perform()
    sleep(2)

    # 获取所有窗口的句柄
    handles = driver.window_handles
    for h in handles:
        # 根据窗口句柄，切换窗口
        driver.switch_to.window(h)
        sleep(2)
        #如果运行到包含京东的页面，
        if driver.title.__contains__("京东"):
            #结束
            break
#框架切换
def test_iframe(driver):
    driver.get("http://192.168.1.128:8082/xuepl1/frame/main.html")
    sleep(2)

    frame = driver.find_element_by_xpath('/html/frameset/frameset/frame[1]')
    driver.switch_to.frame(frame)
    sleep(2)
    driver.find_element_by_link_text('京东').click()
    sleep(2)
    #退出当前iframe
    driver.switch_to.parent_frame()
    #回到初始页面
    #driver.switch_to.default_content()
    sleep(2)
    iframe = driver.find_element_by_xpath("//*[@id='menu']/ul/li[2]/a")
    driver.switch_to.frame(iframe)
    sleep(2)
    inpu = driver.find_element_by_xpath('//input[@id]')
    inpu.click()
    inpu.send_keys("手机")
    sleep(5)
#页面等待
def test_wait(driver):
    driver.get("http://ui.yansl.com/#/loading")
    bt =driver.find_element_by_xpath("//span[contains(text(),'指令方式')]")
    bt.click()
    #显示等待
    WebDriverWait(driver, 5, 0.5).until(
        EC.presence_of_element_located((By.XPATH, '//tbody/tr[1]/td[2]/div'))
    )
    bg = driver.find_element_by_xpath("//tbody/tr[1]/td[2]/div")
    print(bg.text)
    sleep(2)
#文本断言
def test_text(driver):
    driver.get("http://ui.yansl.com/#/message")
    buttons = driver.find_elements_by_xpath("//label[contains(text(),'自动关闭提示')]/..//span[text()='消息']")
    buttons[0].click()
    message = driver.find_element_by_xpath("//div[@role='alert']/p")
    #消息
    text = message.text
    # 断言 这是一条消息在文本中
    assert "这是一条消息" in text
    sleep(2)
#对它的界面源代码做断言
def test_page_source(driver):
    driver.get("http://ui.yansl.com/")
    driver.find_element_by_xpath("//*[@id='app']/section/section/aside/ul/li[3]/div").click()
    driver.find_element_by_xpath("//*[@id='app']/section/section/aside/ul/li[3]/ul/li/ul/li[3]").click()
    #获取页面源代码
    source = driver.page_source
    print(source)
    # 断言 这是一条消息在文本中
    assert "手工关闭提示" in source
    sleep(2)
