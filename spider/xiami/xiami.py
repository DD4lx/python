import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from lxml import etree

import kaisha

chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.set_window_size(1400, 700)
wait = WebDriverWait(browser, 5)


def get_page(url):
    browser.get(url)
    return browser.page_source


def get_resource(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    return None


def parse_page(page_source):
    html_etree = etree.HTML(page_source)
    result_list = html_etree.xpath('//div[@id="chart"]/table/tr')
    print(result_list)
    for result in result_list:
        song_name = result.xpath('./@data-title')[0]
        if '/' in song_name:
            song_name = song_name.replace('/', '-')
        song_data = result.xpath('./@data-mp3')[0]
        song_url = kaisha.str2url(song_data)
        print(song_url)
        data = get_resource(song_url)
        with open(f'./songs/{song_name}.mp3', 'wb') as f:
            f.write(data)
    print('下载完成')


def main():
    url = 'https://www.xiami.com/chart?spm=a1z1s.6843761.1110925385.2.DzUm9P'
    page_source = get_page(url)
    print(page_source)
    parse_page(page_source)


if __name__ == '__main__':
    main()





