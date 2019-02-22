import os
import random
import time

import requests
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from urllib.parse import quote
# from lxml import etree
from PIL import Image
# from io import BytesIO
# from chaojiying import main1
# import time
#
# chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=chrome_options)
#
# # browser = webdriver.Chrome()
# browser.set_window_size(1400, 700)
# # 显式等待 针对某个节点的等待
# wait = WebDriverWait(browser, 10)


def get_resuorce(url):
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    return None


# def get_page():
#     url = 'http://www.1kkk.com/vipindex/'
#     browser.get(url)
#     html = browser.page_source
#     return html


def save_img():
    t = int(round(time.time() * 1000))
    url = f'http://www.1kkk.com/vipindex/image3.ashx?t={t}'
    img = get_resuorce(url)
    with open(f'./imgs/{t}.png', 'wb') as f:
        f.write(img)


def get_images():
    """
    获取图片
    :return: 图片对象
    """
    # top, bottom, left, right = self.get_position()
    # print('小图', top, bottom, left, right)

    img_list = os.listdir('./imgs')
    return img_list


def get_small_imgs():
    img_list = get_images()
    for img in img_list:
        # i = 0
        image = Image.open(f'./imgs/{img}')
        img_name = img.split('.')[0]
        small_img = image.crop((0, 0, 76, 76))
        small_img.save('./small/' + img_name + 'first.png')
        small_img2 = image.crop((76, 0, 152, 76))
        small_img2.save('./small/' + img_name + 'second.png')
        small_img3 = image.crop((152, 0, 228, 76))
        small_img3.save('./small/' + img_name + 'third.png')
        small_img4 = image.crop((228, 0, 304, 76))
        small_img4.save('./small/' + img_name + 'fouth.png')
        # print(i)
        # return small_img


def main():
    # for i in range(300):
    #     save_img()
    #     print(i)
    get_small_imgs()


if __name__ == '__main__':
    main()
