from time import sleep

import allure

#生成报告
@allure.feature("一级分类")
@allure.story("二级分类")
@allure.title("标题")
@allure.issue("http://www.baidu.com",'bug')
@allure.testcase("http://www.baidu.com",'用例')
def test_report(driver):
    url = "http://ui.yansl.com/#/checkbox"
    #连接allure的步骤，并通过
    with allure.step("打开网页:{}".format(url)):pass
    driver.get(url)
    with allure.step("点击多选框:{}".format('//*[id="form"]/form/div[1]/div/input[1]')):
        #引入文件，获取文件内容，文件类型
        allure.attach(driver.get_screenshot_as_png(),'',allure.attachment_type.PNG)
    driver.find_element_by_xpath("//input[@value='1']").click()
    with allure.step("点击多选框:{}".format("//input[@value='2']")):
        allure.attach(driver.get_screenshot_as_png(), '', allure.attachment_type.PNG)
    driver.find_element_by_xpath("//input[@value='2']").click()
    sleep(2)