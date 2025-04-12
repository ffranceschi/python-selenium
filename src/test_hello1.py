import time

from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://www.google.com")
browser.maximize_window()
time.sleep(3)
