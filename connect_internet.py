import sys
import ssl

import requests

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import datetime
import time

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = os.getcwd() + '/chromedriver'

file = open('f20180610.txt', 'r')
from_file = file.read()
file.close()

users = [['f20180610', from_file]]

def insert_user(username, password):
	users.append([username, password])

def check_internet():
	# Internet connected but not logged in still shows as connected!
	# Change this function to be more reliable
	url = 'http://www.google.com'
	timeout = 10
	try:
		request = requests.get(url, timeout=timeout)
		return True
		print('Connected to google ' + str(datetime.datetime.now()))
	except (requests.ConnectionError, requests.Timeout) as exception:
		return False
		print('Connection lost at  ' + str(datetime.datetime.now()))

def log_in(username, password):
	website = 'https://campnet.bits-goa.ac.in:8090/httpclient.html'

	chrome_options = webdriver.ChromeOptions()
	chrome_options.headless = True
	driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
							  options = chrome_options)
	driver.get(website)
	
	elem = driver.find_element_by_name('username')
	elem.clear()
	elem.send_keys(username)

	elem = driver.find_element_by_name('password')
	elem.clear()
	elem.send_keys(password)
	elem.send_keys(Keys.RETURN)

	driver.quit()

if __name__ == '__main__':
	current_id = 0
	log_in(users[current_id][0], users[current_id][1])
	while (current_id < len(users)):
		if (check_internet()):
			print('Internet Active ' + str(datetime.datetime.now()))
			time.sleep(5)
		else:
			print('Internet Lost! ' + str(datetime.datetime.now()))
			print('Trying with the next ID')
			current_id += 1
			log_in(users[current_id][0], users[current_id][1])
	print('All ids extinguished!')
	sys.exit(0)
