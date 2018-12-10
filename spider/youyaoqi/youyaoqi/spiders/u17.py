# -*- coding: utf-8 -*-
import json

import scrapy

from youyaoqi.items import YouyaoqiItem


class U17Spider(scrapy.Spider):
    name = 'u17'
    allowed_domains = ['www.u17.com']
    start_urls = ['http://www.u17.com/comic/ajax.php?mod=comic_list&act=comic_list_new_fun&a=get_comic_list']

    def start_requests(self):
        # url = 'http://www.u17.com/comic/ajax.php?mod=comic_list&act=comic_list_new_fun&a=get_comic_list'
        headers = {
            'Referer': 'http://www.u17.com/comic_list/th99_gr99_ca99_ss99_ob0_ac0_as0_wm0_co99_ct99_p1.html?order=2',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Host': 'www.u17.com'
        }

        for page in range(1, 411):
            data = {
                'data[group_id]': 'no',
                'data[theme_id]': 'no',
                'data[is_vip]': 'no',
                'data[accredit]': 'no',
                'data[color]': 'no',
                'data[comic_type]': 'no',
                'data[series_status]': 'no',
                'data[order]': '2',
                'data[page_num]': '%d' % page,
                'data[read_mode]': 'no',
            }

            yield scrapy.FormRequest(url='http://www.u17.com/comic/ajax.php?mod=comic_list&act=comic_list_new_fun&a=get_comic_list',
                                     headers=headers,
                                     formdata=data,
                                     method='POST',
                                     callback=self.parse,
                                     )

    def parse(self, response):
        result_json = json.loads(response.text)
        data_list = result_json['comic_list']
        print(len(data_list))
        print(result_json)
        for item in data_list:
            # result_dict = {}
            data = YouyaoqiItem()
            data['url'] = f"http://www.u17.com/comic/{item.get('comic_id')}.html"
            data['comic_id'] = item.get('comic_id', '')
            data['name'] = item.get('name', '')
            data['img'] = item.get('cover', '')
            data['category'] = item.get('line2')

            # data = result_dict
            # insert_youyaoqi(result_dict)

            yield data

