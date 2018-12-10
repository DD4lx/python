import json

import requests

import agent_helper
import sqlalchemy_helper
from proxy_helper import get_proxies


def get_page(url, proxies=None):
    agent = agent_helper.get_random_agent()
    headers = {
        'Referer': 'https://list.mogujie.com/s?page=2&q=%E5%A4%96%E5%A5%97&sort=pop&ppath=&ptp=1.5y18ub.0.0.3qt6RYGs',
        'User-Agent': agent,
        'Host': 'list.mogujie.com',
        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
    }

    if proxies is None:
        response = requests.get(url, headers=headers)
    else:
        response = requests.get(url, headers=headers, proxies=proxies)
    if response.status_code == 200:
        return response.text
    return None


def parse_page(html):
    index = html.index('(')
    html = html[index+1:]
    html = html[:-2]
    result_dict = json.loads(html)
    results = result_dict['result']['wall']['docs']
    result_list = []
    for item in results:
        result_dict = {}
        result_dict['tradeItemId'] = item.get('tradeItemId', '')
        result_dict['img'] = item.get('img', '')
        result_dict['itemType'] = item.get('itemType', '')
        result_dict['clientUrl'] = item.get('clientUrl', '')
        result_dict['link'] = item.get('link', '')
        result_dict['itemMarks'] = item.get('itemMarks', '')
        result_dict['acm'] = item.get('acm', '')
        result_dict['title'] = item.get('title', '')
        result_dict['type'] = item.get('type', '')
        result_dict['orgPrice'] = item.get('orgPrice', '')
        result_dict['hasSimilarity'] = item.get('hasSimilarity', '')
        result_dict['cfav'] = item.get('cfav', '')
        result_dict['price'] = item.get('price', '')
        result_dict['similarityUrl'] = item.get('similarityUrl', '')
        # print(result_dict)
        result_list.append(result_dict)
    return result_list


def parse_pages():
    for page in range(1, 101):
        url = f'https://list.mogujie.com/search?callback=jQuery21108192672312676796_1544250199259&_version=8193&ratio=3%3A4&cKey=43&sort=pop&page={page}&q=%25E8%25A3%25A4%25E5%25AD%2590&minPrice=&maxPrice=&ppath=&cpc_offset=&ptp=1.5y18ub.0.0.6TjAoINn&_=1544250199260'
        html = get_page(url)
        one_list = parse_page(html)

        print(page, len(one_list))
        sqlalchemy_helper.save_db(one_list)

    # page = 1
    # while True:
    #     url = f'https://list.mogujie.com/search?callback=jQuery21108192672312676796_1544250199259&_version=8193&ratio=3%3A4&cKey=43&sort=pop&page={page}&q=%25E8%25A3%25A4%25E5%25AD%2590&minPrice=&maxPrice=&ppath=&cpc_offset=&ptp=1.5y18ub.0.0.6TjAoINn&_=1544250199260'
    #     try:
    #         html = get_page(url)
    #         # 一页商品的列表
    #     except Exception as e:
    #         html = ''
    #     if '(' not in html:
    #         print('wait...............')
    #         proxies = get_proxies()
    #         print(proxies)
    #         continue
    #     one_list = parse_page(html)
    #     if one_list is None:
    #         break
    #     print(page, len(one_list))
    #     sqlalchemy_helper.save_db(one_list)
    #     page += 1
    print('获取完成')


def main():
    parse_pages()


if __name__ == '__main__':
    main()