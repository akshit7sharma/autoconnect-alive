import sys
import ssl

import requests

import datetime
import time

def check_internet_1():
	while(True):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s = ssl.wrap_socket(s)
			s.connect(('google.com', 443))
			s.close()
			print('Connected to google.')
			time.sleep(5)
		except:
			print('Connection Lost at ' + str(datetime.datetime.now()))
			time.sleep(5)

def check_internet_2():
	url = 'http://www.google.com'
	timeout = 10
	try:
		request = requests.get(url, timeout=timeout)
		return True
		print('Connected to google ' + str(datetime.datetime.now()))
	except (requests.ConnectionError, requests.Timeout) as exception:
		return False
		print('Connection lost at  ' + str(datetime.datetime.now()))

def check_internet_3():
	pass

if __name__ == '__main__':
	for _ in range(30):
		check_internet_2()
		time.sleep(5)
	sys.exit(0)
