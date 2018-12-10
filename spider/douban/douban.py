import requests
from lxml import etree

import douban_db_helper
from agent_helper import get_random_agent

user_agent = get_random_agent()
headers = {
    "User-Agent": user_agent
}
# 获取页面
def get_page(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


# 获取二进制资源
def get_resource(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    return None


# 存储图片
def save_img(url):
    img_name = url.split('/')[-1]
    img = get_resource(url)
    with open(f'./images/{img_name}', 'wb') as f:
        f.write(img)


# 解析一页
def parse_page(html):
    html = etree.HTML(html)
    channel_result = html.xpath('//div[@class="channel-item"]')
    # 连接数据库
    db = douban_db_helper.get_connection()
    # 游标
    cursor = douban_db_helper.get_cursor(db)

    for channel in channel_result:
        try:
            result_dict = {}
            # 文章标题
            titles = channel.xpath('./div[@class="bd"]/h3/a/text()')[0]
            if '\'' in titles:
                titles = titles.replace('\'', '')
            # 喜欢数
            likes = channel.xpath('./div[@class="likes"]/text()[1]')[0]
            # 简介
            contents = channel.xpath('./div[@class="bd"]/div[@class="block"]/p/text()')[0]
            if '\'' in contents:
                contents = contents.replace('\'', '')
            # 来自
            groups = channel.xpath('./div[@class="bd"]/div[@class="source"]/span[@class="from"]/a/text()')[0]
            if '\'' in groups:
                groups = groups.replace('\'', '')
            # 上传时间
            time = channel.xpath('./div[@class="bd"]/div[@class="source"]/span[@class="pubtime"]/text()')[0]
            # 来自小组链接
            group_url = channel.xpath('./div[@class="bd"]/div[@class="source"]/span[@class="from"]/a/@href')[0]
            # 图片
            images_url = channel.xpath('./div[@class="bd"]/div[@class="block"]/div[@class="pic"]/div[@class="pic-wrap"]/img/@src')
            if len(images_url) == 0:
                images_url = ''
            else:
                images_url = images_url[0]
                # save_img(images_url)

            result_dict['title'] = titles
            result_dict['likes'] = likes
            result_dict['content'] = contents
            result_dict['groups'] = groups
            result_dict['time'] = time
            result_dict['group_url'] = group_url
            result_dict['image_url'] = images_url
            # 插入数据库表
            douban_db_helper.insert_record(db, cursor, result_dict)
        except Exception as e:
            continue

    douban_db_helper.close_connection(db)


# 获取304页
def parse_pages():
    result_list = []
    for i in range(304):
        i = i * 30
        url = "https://www.douban.com/group/explore?start=" + str(i)
        html = get_page(url)
        parse_page(html)
    print('获取完成')


def main():
    parse_pages()


if __name__ == '__main__':
    main()