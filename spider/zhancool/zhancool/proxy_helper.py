import json
import random
import requests

# def get_proxy_ip():
# 	ips = [{"port":"42684","ip":"115.230.62.156"},{"port":"44684","ip":"27.153.128.21"},{"port":"24076","ip":"59.61.39.120"},{"port":"34152","ip":"121.239.230.143"},{"port":"49043","ip":"115.225.155.240"},{"port":"45185","ip":"106.92.102.150"},{"port":"37246","ip":"116.115.210.116"},{"port":"38095","ip":"58.218.92.176"},{"port":"43774","ip":"123.12.238.169"},{"port":"35676","ip":"59.33.69.158"},{"port":"46880","ip":"220.191.102.152"},{"port":"44669","ip":"106.57.22.115"},{"port":"23973","ip":"27.29.144.206"},{"port":"28920","ip":"119.138.195.53"},{"port":"31489","ip":"114.226.93.203"},{"port":"34263","ip":"101.27.20.93"},{"port":"42660","ip":"219.131.250.194"},{"port":"31043","ip":"117.95.30.93"},{"port":"41977","ip":"115.219.75.133"},{"port":"38316","ip":"182.244.164.92"},{"port":"27209","ip":"114.231.4.156"},{"port":"14731","ip":"58.218.92.176"},{"port":"27246","ip":"49.81.19.1"},{"port":"38358","ip":"182.127.83.51"},{"port":"49990","ip":"115.209.48.171"},{"port":"28701","ip":"121.235.228.122"},{"port":"25934","ip":"60.219.214.225"},{"port":"50881","ip":"58.218.92.176"},{"port":"37863","ip":"58.218.92.176"},{"port":"25335","ip":"175.9.215.27"},{"port":"55844","ip":"58.218.92.176"},{"port":"33242","ip":"60.176.237.20"},{"port":"31036","ip":"144.0.92.169"},{"port":"22810","ip":"113.117.65.212"},{"port":"24474","ip":"113.87.193.241"},{"port":"44525","ip":"115.213.103.124"},{"port":"22665","ip":"115.208.14.43"},{"port":"35492","ip":"60.17.236.226"},{"port":"27179","ip":"116.55.26.103"},{"port":"33131","ip":"119.138.195.248"},{"port":"28074","ip":"60.185.206.168"},{"port":"37123","ip":"113.101.253.25"},{"port":"35873","ip":"110.18.141.192"},{"port":"38403","ip":"123.245.10.13"},{"port":"47966","ip":"220.186.145.195"},{"port":"39887","ip":"14.118.160.210"},{"port":"39569","ip":"116.55.26.72"},{"port":"26371","ip":"1.62.121.40"},{"port":"28857","ip":"182.38.124.218"},{"port":"42914","ip":"114.239.210.83"}]
# 	ip_dict = random.choice(ips)

# 	return ip_dict

def get_proxy_ip_from_pool():
    url = 'http://127.0.0.1:5555/random'

    headers =  {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)" 
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # print(response.text)
        return response.text
    return None


def get_proxy_ip():
	url = 'http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=72a2b845b4114d05aa77d110e9b97e03&count=20&expiryDate=0&format=1&newLine=2'

	headers =  {
		"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)" 
	}
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		# print(response.text)
		json_data = json.loads(response.text)
		ip_list = json_data['msg']
		ip_dict = random.choice(ip_list)

		return ip_dict
	return None


if __name__ == '__main__':
	ip = get_proxy_ip()
	print(ip)