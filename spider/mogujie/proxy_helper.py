import requests


def get_page():
    url = "http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=12eb2c94244342f7a28e67361d030a9b&count=1&expiryDate=0&format=1&newLine=2"
    headers =  {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    # print(response.status_code)
    if response.status_code == 200:
        return response.json()


def get_proxies():
    ip_json = get_page()
    print(ip_json)
    ip = ip_json['msg'][0]['ip']
    port = ip_json['msg'][0]['port']
    proxy = ip + ':' + port

    proxies = {
        'http': 'http://' + proxy, 
        'https': 'https://' + proxy 
    }

    return proxies


def main():
    print(get_proxies())


if __name__ == '__main__':
    main()
