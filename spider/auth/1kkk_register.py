import os

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
from compare import compare
from compare_helper import get_compare

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

# browser = webdriver.Chrome()
browser.set_window_size(1400, 700)
# 显式等待 针对某个节点的等待
wait = WebDriverWait(browser, 10)


def get_page():
    url = 'http://www.1kkk.com/register/'
    browser.get(url)
    html = browser.page_source
    return html


# 取浏览器窗口内全图
def get_big_image():
    # browser.execute_script('window.scrollTo(0, 300)')
    screenshot = browser.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))
    return screenshot


# 取验证码坐标位置（左上角和右下角）
def get_position():
    img = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.rotate-background')))
    loc = img.location
    size = img.size
    print(loc)
    print(size)
    x1 = loc['x']
    # 记住减去滚动高度
    y1 = loc['y']
    x2 = loc['x'] + size['width']
    y2 = y1 + size['height']
    return (x1, y1, x2, y2)


def parse_html(html):
    # etree_html = etree.HTML(html)
    screenshot = get_big_image()
    screenshot.save('img_screen.png')
    x1, y1, x2, y2 = get_position()
    crop_image = screenshot.crop((x1, y1, x2, y2))
    file_name = 'crop_img.png'
    crop_image.save(file_name)

    crop_image2 = screenshot.crop((x2+3, y1, x2+79, y2))
    file_name2 = 'crop_img2.png'
    crop_image2.save(file_name2)

    crop_image3 = screenshot.crop((x2+81, y1, x2+157, y2))
    file_name3 = 'crop_img3.png'
    crop_image3.save(file_name3)

    crop_image4 = screenshot.crop((x2+158, y1, x2+234, y2))
    file_name4 = 'crop_img4.png'
    crop_image4.save(file_name4)
    # captha_str = main1(file_name)

    username = '1409448010@qq.com'
    password = 'a12345678'

    # print(captha_str)

    input_username = wait.until(EC.presence_of_element_located
                                ((By.XPATH, '//input[@name="txt_reg_name"]')))
    input_password1 = wait.until(EC.presence_of_element_located
                                 ((By.XPATH, '//input[@name="txt_reg_password"]')))
    input_password2 = wait.until(EC.presence_of_element_located
                                 ((By.XPATH, '//input[@name="txt_reg_password2"]')))
    change_btn = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, '//a[@class="rotate-refresh"]')))
    input_checks = wait.until(EC.presence_of_all_elements_located
                              ((By.XPATH, '//div[@class="rotate-background"]')))
    sublime3 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button')))
    input_username.send_keys(username)
    input_password1.send_keys(password)
    input_password2.send_keys(password)
    # input_tel.send_keys(tel)
    # input_check.send_keys(captha_str)
    time.sleep(2)
    # print(compare('crop_img.png'))

    result = compare()
    print(result)
    if len(result) < 4:
        change_btn.click()
    # print(len(input_checks))
    for i in range(len(result)):
        for j in range(result[i]):
            input_checks[i].click()

    sublime3.click()


def main():
    html = get_page()
    parse_html(html)
    # result = compare()
    # print(result)


if __name__ == '__main__':
    main()