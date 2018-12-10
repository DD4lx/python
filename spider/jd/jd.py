import re

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from lxml import etree
import time

from sqlalchemy_helper import save_db

chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.set_window_size(1400, 700)
wait = WebDriverWait(browser, 5)


def get_page(page):
    if page == 1:
        url = 'https://www.jd.com'
        browser.get(url)
        # print(browser.page_source)
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#key')))
        input.clear()
        input.send_keys('娃娃')

        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#search button.button')))
        submit.click()
        time.sleep(5)
        # print(browser.page_source)

    if page > 1:
        # 写页码
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage input.input-txt')))
        input.clear()
        input.send_keys(page)

        # 点击下一页
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage .btn.btn-default')))
        submit.click()


    for i in range(16):
      str_js = 'var step = document.body.scrollHeight / 16; window.scrollTo(0, step * %d)' % (i + 1)
      browser.execute_script(str_js)
      time.sleep(1)

    return browser.page_source


def parse_page(page_source):
    html_etree = etree.HTML(page_source)
    goodsList = html_etree.xpath('//div[@id="J_goodsList"]/ul[@class="gl-warp clearfix"]/li')
    # img_src = html_etree.xpath('//div[@id="J_goodsList"]//img/@src')
    # result_list = html_etree.xpath(
    #     '//div[@id="J_goodsList"]//div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]//em//text()')
    result_list = []
    for good in goodsList:
        try:
            result_dict = {}
            # sku
            sku = good.xpath('./@data-sku')[0]
            print(sku)
            # title
            title = good.xpath('./div[@class="gl-i-wrap"]/div[@class="p-img"]/a/@title')[0]
            # print(title)
            # href
            href = good.xpath('./div[@class="gl-i-wrap"]/div[@class="p-img"]/a/@href')[0]
            # img
            img = good.xpath('./div[@class="gl-i-wrap"]/div[@class="p-img"]/a/img/@src')
            if len(img) == 0:
                img = ''
            else:
                img = img[0]
            # price
            price = good.xpath('./div[@class="gl-i-wrap"]/div[@class="p-price"]//i/text()')
            print(price)
            if len(price) == 0:
                price = 0
            else:
                price = price[0]
            # name
            name = good.xpath('./div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]//em//text()')
            name = ''.join(name)
            # commit
            commit_url = good.xpath('./div[@class="gl-i-wrap"]/div[@class="p-commit"]/strong/a/@href')[0]
            commit = good.xpath('./div[@class="gl-i-wrap"]/div[@class="p-commit"]/strong/text()')[0]
            # shop
            shop_url = good.xpath('./div[@class="gl-i-wrap"]/div[@class="p-shop"]/span/a/@href')
            if len(shop_url) == 0:
                shop_url = ''
            else:
                shop_url = shop_url[0]
            shop_name = good.xpath('./div[@class="gl-i-wrap"]/div[@class="p-shop"]/span/a/text()')
            if len(shop_name) == 0:
                shop_name = ''
            else:
                shop_name = shop_name[0]
            result_dict['sku'] = sku
            result_dict['title'] = title
            result_dict['href'] = href
            result_dict['img'] = img
            result_dict['price'] = price
            result_dict['name'] = name
            result_dict['commit_url'] = commit_url
            result_dict['commit'] = commit
            result_dict['shop_url'] = shop_url
            result_dict['shop_name'] = shop_name
            result_list.append(result_dict)
        except Exception as e:
            continue
    return result_list


    # print(img_src)


def main():
    # page_source = get_page()
    # parse_page(page_source)
    # result_list = []
    for page in range(100):
        print(page)
        page_source = get_page(page + 1)
        result = parse_page(page_source)
        # result_list.extend(result)
        save_db(result)


if __name__ == '__main__':
    main()
