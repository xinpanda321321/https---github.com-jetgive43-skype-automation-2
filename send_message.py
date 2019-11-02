import requests
from selenium import webdriver
import time
import urllib
import json

def input_userdata():
	username = input('Please input your skype username : ')
	password = input('Please input your skype password : ')
	skype_id = input('Please input Skype id to send invitation : ')
	message = input('Please input message')
	return username, password, skype_id, message

def start_webbrowser():
	username, password, skype_id, message = input_userdata()
	driver = webdriver.Chrome()
	driver.get('https://web.skype.com')
	time.sleep(2)

	driver.find_element_by_xpath("//input[@name='loginfmt']").send_keys(username+'\n')
	time.sleep(2)
	driver.find_element_by_xpath("//input[@name='passwd']").send_keys(password+'\n')
	time.sleep(10)

	try:
		driver.find_element_by_xpath("//button[@aria-label='Got it!']").click()
	except:
		pass

	time.sleep(1)

	driver.find_element_by_xpath("//button[@title='People, groups & messages']").click()
	time.sleep(1)

	driver.find_element_by_xpath("//input[@placeholder='Search Skype']").send_keys(skype_id+'\n')
	time.sleep(10)

	# click skype searching user
	driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div[4]/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div[2]').click()
	time.sleep(3)

	# send message to specific user
	driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/div/div/div/div').send_keys(message + '\n')

if __name__ == '__main__':
	start_webbrowser()