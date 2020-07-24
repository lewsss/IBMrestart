import os
# 方便延时加载
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains
import random

# 模拟手机浏览器打开网站
# mobileEmulation = {'deviceName': 'iPhone X'}
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option('w3c',  False)
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')
browser = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)
#window电脑本地
# browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver")

def scut():
    browser.get('https://cloud.ibm.com/login?redirect=%2Fcloudfoundry%2Fpublic')
    # 将窗口最大化
    browser.maximize_window()
    time.sleep(1)
    # browser.set_window_size(375,812)
    # 格式是PEP8自动转的
    # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
    time.sleep(random.randint(1, 2))
    browser.find_element_by_xpath("//*[@id='userid']").send_keys(os.environ['SCUT_USER'])
    time.sleep(random.randint(1, 2))
    browser.find_element_by_xpath("/html/body/main/div[2]/div/div/div[1]/form[1]/div[2]/div[1]/div[2]/div[2]/button").click()
    time.sleep(random.randint(1, 2))
    browser.find_element_by_xpath("//*[@id='password']").send_keys(os.environ['SCUT_PASSWORD'])
    # 在输入用户名和密码之后,点击登陆按钮
    time.sleep(random.randint(1, 3))
    browser.find_element_by_xpath("/html/body/main/div[2]/div/div/div[1]/form[1]/div[2]/div[2]/div[2]/div[2]/button").click()
    time.sleep(random.randint(1, 2))
    # huakuai = browser.find_element_by_xpath('//*[@id="layui-m-layer0"]/div[2]/div/div/div/div/div/div/div/span[1]')
    # tuodong = TouchActions(browser)
    # tuodong.flick_element(huakuai, 420, 0, 2).perform()
    time.sleep(random.randint(2, 10))
    browser.find_element_by_xpath("//*[@id='close-button']").click()
    time.sleep(random.randint(2, 10))
    browser.find_element_by_xpath("//*[@id='main-content']/div/main/div/div/div[1]/div/div[5]/div/div[21]/button").click()
    time.sleep(random.randint(2, 10))
    browser.find_element_by_xpath("/html/body/ul/li[2]/button").click()
    time.sleep(random.randint(2, 10))
    browser.find_element_by_xpath("//*[@id='modal']/div/div[3]/button[2]").click()
    time.sleep(random.randint(2, 10))
    print('已重启了吧！')
if __name__ == '__main__':
    scut()
    # 脚本运行成功,退出浏览器
    browser.quit()
