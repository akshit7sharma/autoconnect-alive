from selenium import webdriver   # for webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome('/Users/akshitsharma/Random programs/bpgc-autoconnect',options=option)
