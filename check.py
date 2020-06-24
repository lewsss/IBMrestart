import os
# 方便延时加载
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.touch_actions import TouchActions

# 模拟手机浏览器打开网站
mobileEmulation = {'deviceName': 'iPhone X'}
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option('w3c',  False)
chrome_options.add_argument('user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1')
browser = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)
#window电脑本地
# browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver")



def scut():
    browser.get('https://member.dossen.com/member/login/phone?redirect_uri=https%253A%252F%252Fshop.m.dossen.com%252Fsignin%252Findex&salerCode=')
    # 将窗口最大化
    browser.maximize_window()
    time.sleep(1)
    browser.set_window_size(375,812)
    # 格式是PEP8自动转的
    # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
    browser.find_element_by_xpath("//*[@id='userName']").send_keys(os.environ['SCUT_USER'])
    browser.find_element_by_xpath("//*[@id='password']").send_keys(os.environ['SCUT_PASSWORD'])
    # 在输入用户名和密码之后,点击登陆按钮
    browser.find_element_by_xpath("/html/body/div[1]/div[2]").click()
    time.sleep(1)
    huakuai = browser.find_element_by_xpath('//*[@id="layui-m-layer0"]/div[2]/div/div/div/div/div/div/div/span[1]')
    tuodong = TouchActions(browser)
    tuodong.flick_element(huakuai, 420, 0, 2).perform()
    time.sleep(2)
    all_browser=browser.window_handles
    browser.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[3]').click()
    chenggong = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div')
    text = chenggong.text
    print(text)
    time.sleep(3)
    saveFile("签到成功")
if __name__ == '__main__':
    scut()
    # 脚本运行成功,退出浏览器
    browser.quit()
