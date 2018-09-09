from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from random import randint, choice
import string

myOptions = Options()
myOptions.add_argument("--no-sandbox")
browser = webdriver.Chrome(chrome_options = myOptions)

browser.get("http://sugang.korea.ac.kr")

def login():
	frames = None
	while not frames:
		try:
			frames = browser.find_elements_by_tag_name("frame")
		except:
			sleep(2)
	check = 0
	for frame in frames:
		if check == 0:
			check += 1
			continue
		else:
			browser.switch_to_frame(frame)
			idbut = None
			while not idbut:
				try:
					idbut = browser.find_element_by_name("id")
					idbut.send_keys("2015410225")
					browser.find_element_by_name("pw").send_keys("sm70562919")
					browser.find_element_by_id("loginButton").click()
				except:
					sleep(2)
			alert = None
			while not alert:
				try:
					alert = browser.switch_to_alert()
					alert.accept()
				except:
					sleep(2)
	browser.switch_to_default_content()

def findsub():
	frames = None
	while not frames:
		try:
			frames = browser.find_elements_by_tag_name("frame")
		except:
			sleep(2)
	browser.switch_to_frame(frames[0])
	browser.find_element_by_id("main1").click()
	browser.find_element_by_xpath("//*[@id='sub1']/li[2]/a").click()
	browser.switch_to_default_content()
	
	browser.switch_to_frame(browser.find_element_by_name("firstF"))
	browser.switch_to_frame(browser.find_element_by_name("ILec"))
	sleep(3)
	select = Select(browser.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/div[1]/div/select[4]"))
	select.select_by_value("32")
	browser.find_element_by_css_selector(".mbtn.submit.ui-button.ui-widget.ui-state-default.ui-corner-all").click()

hihihihihihihihdfjkdfjdf
fjakjdlfjalkdjfalkfjaflk
