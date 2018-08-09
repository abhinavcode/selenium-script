from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pathlib
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import selenium.webdriver.common.alert 
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.binary_location =("/snap/bin/chromium");

#prefs = {"download.default_directory" : "/some/path"}
#chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "path/to/chromedriver.exe"
#chrome driver placed in same directory
driver = webdriver.Chrome('./chromedriver', chrome_options=chromeOptions);
#test that script is running
driver.get("http://www.google.com");
# A sample site
driver.get("http://services.ecourts.gov.in/ecourtindia_v5.1/")
#wait for page to load
driver.implicitly_wait(15)
#check if an element is present
case_status=driver.find_element_by_class_name("case-status-dp");
#click on the above element
case_status.click()
driver.implicitly_wait(10) # seconds
#alert box click
driver.switch_to.alert.accept();

state = Select(driver.find_element_by_id('sess_state_code'))
state.select_by_visible_text("Karnataka")
driver.implicitly_wait(10) # seconds

dis = Select(driver.find_element_by_id('sess_dist_code'))
dis.select_by_visible_text("BENGALURU")
driver.implicitly_wait(10) # seconds

court_complex_code=Select(driver.find_element_by_id('court_complex_code'))
court_complex_code.select_by_visible_text("CMM Court Complex, Bangalore")
driver.implicitly_wait(10) # seconds

CScaseType=driver.find_element_by_id("CScaseType");
CScaseType.click()

caseType=Select(driver.find_element_by_id("case_type44"))
caseType.select_by_visible_text("C.C. - CRIMINAL CASES")

driver.implicitly_wait(10) # seconds


year=driver.find_element_by_id("search_year")
#type year in the textbox
year.send_keys("1996")#year

driver.implicitly_wait(10) # seconds
pd=driver.find_element_by_id("radDis_captcha")
pd.click()

driver.implicitly_wait(10) # seconds
try:
	element = WebDriverWait(driver, 100).until(
		EC.presence_of_element_located((By.ID, "dispTable"))
	)
finally:
	print("mil gaya")

r=driver.find_elements_by_class_name("someclass")
print len(r)

data=[]


for j in range(len(r)):
	time.sleep(1)
	#j+=2	
	r[j].click()
	print j

	try:
		#wait until the elemnet hasnt loaded
		e = WebDriverWait(driver, 100).until(
			EC.visibility_of_element_located((By.ID, "shareSelect"))
		)
		e1 = WebDriverWait(driver, 100).until(
			EC.visibility_of_element_located((By.XPATH, '//*[@id="caseHistoryDiv"]/form/div/table[2]/tbody/tr/td'))
		)
	finally:	
		print "page loaded"
	try:

		driver.implicitly_wait(100) # seconds
		#select element by xpath (to select by xpath simply inspect that element and copy its xpath		
		casetype=driver.find_element_by_css_selector('#shareSelect > table.table.table-responsive.case_details_table > tbody > tr:nth-child(1) > td:nth-child(2)')
		print casetype.text

		driver.implicitly_wait(10) # seconds		

		fillingnumber=driver.find_element_by_xpath('//*[@id="shareSelect"]/table[1]/tbody/tr[2]/td[2]')
		print fillingnumber.text

		driver.implicitly_wait(10) # seconds

		fillingdate=driver.find_element_by_xpath('//*[@id="shareSelect"]/table[1]/tbody/tr[2]/td[4]')
		print fillingdate.text

		driver.implicitly_wait(10) # seconds
	
		regnumber=driver.find_element_by_xpath('//*[@id="shareSelect"]/table[1]/tbody/tr[3]/td[2]/label')
		print regnumber.text

		driver.implicitly_wait(10) # seconds
	
		regdate=driver.find_element_by_xpath('//*[@id="shareSelect"]/table[1]/tbody/tr[3]/td[4]')
		print regdate.text
	
		driver.implicitly_wait(10) # seconds	
	
		cnrnumber=driver.find_element_by_xpath('//*[@id="shareSelect"]/table[1]/tbody/tr[4]/td[2]/b')
		print cnrnumber.text
	
		driver.implicitly_wait(10) # seconds

		firsthearingdate=driver.find_element_by_xpath('//*[@id="shareSelect"]/table[2]/tbody/tr[1]/td[2]/strong')
		print firsthearingdate.text
	
		driver.implicitly_wait(10) # seconds

		decisiondate=driver.find_element_by_xpath('//*[@id="shareSelect"]/table[2]/tbody/tr[2]/td[2]/strong')
		print decisiondate.text

		driver.implicitly_wait(10) # seconds


		casestatus=driver.find_element_by_xpath('//*[@id="shareSelect"]/table[2]/tbody/tr[3]/td[2]/strong')
		print casestatus.text
	
		#driver.implicitly_wait(10) # seconds
	
		natureofdisposal=driver.find_element_by_xpath('//*[@id="shareSelect"]/table[2]/tbody/tr[4]/td[2]/label/strong')
		print natureofdisposal.text
	
		#driver.implicitly_wait(10) # seconds

		courtnumberandjudge=driver.find_element_by_xpath('//*[@id="shareSelect"]/table[2]/tbody/tr[5]/td[2]/label/strong')
		print courtnumberandjudge.text
	
		#driver.implicitly_wait(10) # seconds

		panda=driver.find_element_by_xpath('//*[@id="caseHistoryDiv"]/form/div/table[1]/tbody/tr/td')
		print panda.text
	
		#driver.implicitly_wait(10) # seconds

		resanda=driver.find_element_by_xpath('//*[@id="caseHistoryDiv"]/form/div/table[2]/tbody/tr/td')

	except:
		print "err"


	
	driver.implicitly_wait(100) # seconds
	time.sleep(1);
	print "wait done after view click"
	try:
		e = WebDriverWait(driver, 50).until(
			EC.visibility_of_element_located((By.XPATH, '//*[@id="backTopDiv"]/input'))
		)
		e = WebDriverWait(driver, 50).until(
			EC.presence_of_element_located((By.XPATH, '//*[@id="backTopDiv"]/input'))
		)
		print "got it"
	finally:	
		back= driver.find_element_by_css_selector('#backTopDiv > input[type="button"]')
		back.click()
	
print data

