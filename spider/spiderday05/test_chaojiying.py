from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from lxml import etree
from PIL import Image
from io import BytesIO
from chaojiying import main1
import time

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

# browser = webdriver.Chrome()
browser.set_window_size(1400, 700)
# 显式等待 针对某个节点的等待
wait = WebDriverWait(browser, 10)

def get_page():
    url = 'http://bm.e21cn.com/log/reg.aspx'
    browser.get(url)
    html = browser.page_source
    return html

# 取浏览器窗口内全图
def get_big_image():
    browser.execute_script('window.scrollTo(0, 300)')
    screenshot = browser.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))
    return screenshot

# 取验证码坐标位置（左上角和右下角）
def get_position():
    img = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#imgCheckCode')))
    loc = img.location
    size = img.size
    print(loc)
    print(size)
    x1 = loc['x']
    # 记住减去滚动高度
    y1 = loc['y'] - 300
    x2 = loc['x'] + size['width']
    y2 = loc['y'] + size['height']
    return (x1, y1, x2, y2)

def parse_html(html):
    # etree_html = etree.HTML(html)
    screenshot = get_big_image()
    screenshot.save('full_screen.png')
    x1, y1, x2, y2 = get_position()
    crop_image = screenshot.crop((x1, y1, x2, y2))
    file_name = 'crop.png'
    crop_image.save(file_name)
    captha_str = main1(file_name)
    
    username = 'carmack55'
    password = '123456'
    tel = '15775978922'

    print(captha_str)

    input_username = wait.until(EC.presence_of_element_located
                       ((By.CSS_SELECTOR, 'input#username')))
    input_password1 = wait.until(EC.presence_of_element_located
                       ((By.CSS_SELECTOR, 'input#pwd')))
    input_password2 = wait.until(EC.presence_of_element_located
                                 ((By.CSS_SELECTOR, 'input#pwd_Q')))
    input_tel = wait.until(EC.presence_of_element_located
                                 ((By.CSS_SELECTOR, 'input#tel')))
    input_check = wait.until(EC.presence_of_element_located
                                 ((By.CSS_SELECTOR, 'input#CheckCode')))
    sublime = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#btn_login')))
    input_username.send_keys(username)
    input_password1.send_keys(password)
    input_password2.send_keys(password)
    input_tel.send_keys(tel)
    input_check.send_keys(captha_str)
    time.sleep(2)
    sublime.click()

def main():
	html = get_page()
	parse_html(html)

if __name__ == '__main__':
	main()