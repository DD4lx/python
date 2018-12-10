import re

import requests

import maoyan_db_helper
from agent_helper import get_random_agent


# 抓取二进制资源
def get_resource(url):
    headers = {
        "User-Agent": get_random_agent()
    }
    response = requests.get(url, headers)
    if response.status_code == 200:
        return response.content
    return None


# 存储图片
def write_image_file(img_url):
    img_name = img_url.split('/')[-1].split('@')[0]
    content = get_resource(img_url)
    with open(f'./images/{img_name}', 'wb') as f:
        f.write(content)

# 抓取页面
def get_page(url):
    headers = {
        "User-Agent": get_random_agent()
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


# 解析每一页
def parse_page(html):
        star_pattern = re.compile('<p class="star">(.*?)</p>', re.S)
        star = re.findall(star_pattern, html)
        name_pattern = re.compile('<p class="name"><a href="/films/.*?" title=".*?" data-act="boarditem-click" data-val="{movieId:.*?}">(.*?)</a></p>', re.S)
        name = re.findall(name_pattern, html)
        score_pattern = re.compile('<p class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>', re.S)
        score = re.findall(score_pattern, html)
        rate_pattern = re.compile('<i class="board-index board-index-.*?">(.*?)</i>', re.S)
        rate = re.findall(rate_pattern, html)
        time_pattern = re.compile('<p class="releasetime">上映时间：(.*?)</p>', re.S)
        time = re.findall(time_pattern, html)
        img_url_pattern = re.compile('.*?movieId:.*?>.*?<img.*?<img.*?src="(.*?)"', re.S)
        img_url = re.findall(img_url_pattern, html)

        # 连接mysql
        db = maoyan_db_helper.get_connection()
        # cursor
        cursor = maoyan_db_helper.get_cursor(db)

        result_list = []
        for i in range(len(star)):
            result_dict = {}
            result_dict['star'] = star[i].strip().split('：')[-1]
            result_dict['name'] = name[i].strip()
            result_dict['score'] = ''.join(score[i])
            result_dict['rate'] = rate[i].strip()
            result_dict['time'] = time[i].strip()
            result_dict['img_url'] = img_url[i].strip()
            write_image_file(img_url[i].strip())

            # 循环插入
            maoyan_db_helper.insert_record(db, cursor, result_dict)
            print(result_dict)

        # return result_list
        maoyan_db_helper.close_connection(db)


# 取10页
def parse_pages():
    for i in range(10):
        page = i * 10
        url = 'http://maoyan.com/board/4?offset=' + str(page)
        html = get_page(url)
        parse_page(html)
    print('存储完成')


def main():
    parse_pages()


if __name__ == '__main__':
    main()

