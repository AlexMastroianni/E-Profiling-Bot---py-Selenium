from hashlib import new
from select import select
from tkinter import E
from tkinter.tix import Select
from selenium import webdriver
import time
url = webdriver.Chrome()
url.get("https://elogbook.eprofiling.com.au/index.cfm?event=editCard&cardID=&qualificationID=E5C5B039-0A48-4103-869E-A7D2CB4417EC&yearNo=2020&weekNo=23&apprenticeID=389D8235-466A-6537-6E13-A4A219C87018")

time.sleep(5)

username = "al@dvineelectrics.com.au"
password = "password123"

usernameInput = url.find_element("xpath", "/html/body/div[1]/div[3]/div[1]/table/tbody/tr[2]/td[1]/form/table/tbody/tr[1]/td[2]/input")
usernameInput.send_keys(username)

passwordInput = url.find_element("xpath", "/html/body/div[1]/div[3]/div[1]/table/tbody/tr[2]/td[1]/form/table/tbody/tr[2]/td[2]/input")
passwordInput.send_keys(password)


time.sleep(2)
loginSubmit = url.find_element("xpath", "/html/body/div[1]/div[3]/div[1]/table/tbody/tr[2]/td[1]/form/div/input")
loginSubmit.click()


time.sleep(2)
cards = url.find_element("xpath", "/html/body/div[1]/div[2]/ul/li[2]/a")
cards.click()

time.sleep(2)
firstCard = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/table/tbody[2]/tr[1]/td[2]/a")
firstCard.click()


time.sleep(2)
expand = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/p/span[1]")
expand.click()



# Fault finding

