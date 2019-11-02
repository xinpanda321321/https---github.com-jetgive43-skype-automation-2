import requests
from selenium import webdriver
import time
import urllib
import json

def input_userdata():
	username = input('Please input your skype username : ')
	password = input('Please input your skype password : ')
	search_cl = input('Please input Search keyword : ')
	return username, password, skype_id, message

def start_webbrowser():
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

	driver.find_element_by_xpath("//input[@placeholder='Search Skype']").send_keys(search_cl+'\n')
	time.sleep(10)

	# send post request to fetch profiles
	cookies_list = driver.get_cookies()
	cookies_dict = {}
	for cookie in cookies_list:
	    cookies_dict[cookie['name']] = cookie['value']

	url = 'https://skypegraph.skype.com/v2.0/search'
	params = {
		'searchString' : search_cl,	# variable
		'requestId' : '1572168746234'	# variable random
	}

	headers = {
		'X-ECS-ETag' : 'pJJRlu+tkxGVX/sMkk0kYY2AgatWKJfBf4SI6YxSRQQ=',	# variable fixed
		'X-Skype-Client' : '1418/8.53.0.85',
		'X-SkypeGraphServiceSettings' : '"experiment":"Default","geoProximity":"disabled","demotionScoreEnabled":"true"',
		'X-Skypetoken' : cookies_dict['skypeToken']	# variable
	}

	response = requests.get(url, headers=headers, params=params)

	# get profile users as json
	print (response.content)

if __name__ == '__main__':
	start_webbrowser()