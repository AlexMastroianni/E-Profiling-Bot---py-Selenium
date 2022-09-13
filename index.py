from hashlib import new
from select import select
from tkinter import E
from tkinter.tix import Select
from selenium import webdriver
import time
url = webdriver.Chrome()
url.get("https://elogbook.eprofiling.com.au/index.cfm?event=editCard&cardID=&qualificationID=E5C5B039-0A48-4103-869E-A7D2CB4417EC&yearNo=2020&weekNo=23&apprenticeID=389D8235-466A-6537-6E13-A4A219C87018")

time.sleep(2)

username = "al@dvineelectrics.com.au"
password = "password123"

usernameInput = url.find_element("xpath", "/html/body/div[1]/div[3]/div[1]/table/tbody/tr[2]/td[1]/form/table/tbody/tr[1]/td[2]/input")
usernameInput.send_keys(username)

passwordInput = url.find_element("xpath", "/html/body/div[1]/div[3]/div[1]/table/tbody/tr[2]/td[1]/form/table/tbody/tr[2]/td[2]/input")
passwordInput.send_keys(password)


time.sleep(0.5)
loginSubmit = url.find_element("xpath", "/html/body/div[1]/div[3]/div[1]/table/tbody/tr[2]/td[1]/form/div/input")
loginSubmit.click()


time.sleep(2)
cards = url.find_element("xpath", "/html/body/div[1]/div[2]/ul/li[2]/a")
cards.click()

time.sleep(0.5)
firstCard = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/table/tbody[2]/tr[1]/td[2]/a")
firstCard.click()


time.sleep(2)
supervisorDropdown = url.find_element("xpath", "//tbody/tr/td/div[1]/select[2]")
supervisorDropdown.click()

time.sleep(0.5)
supervisorSelect = url.find_element("xpath","//tbody//div[1]//select[2]//option[2]")
supervisorSelect.click()


time.sleep(0.5)
expand = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/p/span[1]")
expand.click()



time.sleep(1)
# Timer 1
timer1Dropdown = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/select")
timer1Dropdown.click()

timer1Select = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/select/option[33]")
timer1Select.click()


# Card Fillout
time.sleep(2)
selectbutton1 = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/input")
selectbutton1.click()

selectbutton2 = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td[2]/table/tbody/tr/td[2]/input")
selectbutton2.click()

selectbutton3 = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]/table/tbody/tr/td[2]/input")
selectbutton3.click()

selectbutton4 = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]/table/tbody/tr[1]/td[1]/input")
selectbutton4.click()

selectbutton5 = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]/table/tbody/tr[3]/td[1]/input")
selectbutton5.click()

selectbutton6 = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]/table/tbody/tr[4]/td[1]/input")
selectbutton6.click()

selectbutton7 = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]/table/tbody/tr[11]/td[1]/input")
selectbutton7.click()

selectbutton8 = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]/table/tbody/tr[12]/td[1]/input")
selectbutton8.click()

selectbutton9 = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/table[2]/tbody/tr[2]/td/table[1]/tbody/tr/td/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]/table/tbody/tr[11]/td[2]/input")
selectbutton9.click()

time.sleep(1)
# Work Practices
button1 = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/table[4]/tbody/tr[1]/td/input")
button1.click()

button2 = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/table[4]/tbody/tr[2]/td/input")
button2.click()

button3 = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/table[4]/tbody/tr[3]/td/input")
button3.click()

button4 = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/table[4]/tbody/tr[4]/td/input")
button4.click()

button5 = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/table[4]/tbody/tr[5]/td/input")
button5.click()

button6 = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/table[4]/tbody/tr[6]/td/input")
button6.click()

button7 = url.find_element("xpath", "/html/body/div[1]/div[3]/div[2]/form/div[1]/table[4]/tbody/tr[7]/td/input")
button7.click()











