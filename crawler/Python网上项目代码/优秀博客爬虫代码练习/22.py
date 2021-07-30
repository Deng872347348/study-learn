# coding=gbk
import re
import requests
from requests import RequestException
import time
import random
def get_page(url):
	try:
		headers = {
			'Referer': 'https://blog.csdn.net',  # αװ�ɴ�CSDN����������������
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'  # αװ�������
		}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		print('�������')
		return None
def parse_page(html):
	try:
		read_num = int(re.compile('<span.*?read-count.*?(\d+).*?</span>').search(html).group(1))
		return read_num
	except Exception:
		print('��������')
		return None
def main():
	try:
		while 1:
			url = 'https://blog.csdn.net/Deng872347348/article/details/114956215'  # ��ˢ��������͵�url
			html = get_page(url)
			if html:
				read_num = parse_page(html)
				if read_num:
					print('��ǰ�Ķ�����', read_num)
			url = 'https://blog.csdn.net/Deng872347348/article/details/114654710'  # ��ˢ��������͵�url
			html = get_page(url)
			if html:
				read_num = parse_page(html)
				if read_num:
					print('��ǰ�Ķ�����', read_num)
			url = 'https://blog.csdn.net/Deng872347348/article/details/114636752'  # ��ˢ��������͵�url
			html = get_page(url)
			if html:
				read_num = parse_page(html)
				if read_num:
					print('��ǰ�Ķ�����', read_num)
			url = 'https://blog.csdn.net/Deng872347348/article/details/114334480'  # ��ˢ��������͵�url
			html = get_page(url)
			if html:
				read_num = parse_page(html)
				if read_num:
					print('��ǰ�Ķ�����', read_num)
			sleep_time = random.randint(60, 83)
			print('please wait', sleep_time, 's')
			time.sleep(sleep_time)  # ���÷���Ƶ�ʣ�����Ƶ���ķ��ʻᴥ��������
	except Exception:
		print('��������')
if __name__ == '__main__':
	main()
