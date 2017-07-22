import pandas as pd 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

import time

driver = webdriver.Ie(executable_path = r"C:\Users\1hp\Downloads\IEDriverServer_x64_3.4.0\IEDriverServer.exe")
driver.get("https://vpn.iitr.ac.in/+CSCO+1h75676763663A2F2F70756E61617279762E7661++/placement/results/branch/")
driver.implicitly_wait(10)

degree=[]
branch=[]
placed=[]
company=[]

main = driver.find_elements_by_css_selector("div#content_middle>table>tbody>tr")

for n in range(0, len(main)):
	try:
		WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((By.ID, "content_middle")))

		main = driver.find_elements_by_css_selector("div#content_middle>table>tbody>tr")

		degree_temp= main[n].find_elements_by_css_selector("td")[1].text			
		branch_temp= main[n].find_elements_by_css_selector("td")[2].text			
		driver.get(main[n].find_elements_by_css_selector("td")[5]
			.find_element_by_css_selector("a")
			.get_attribute("href"))


		WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((By.ID, "content_middle")))

		main = driver.find_elements_by_css_selector("div#content_middle>table>tbody>tr")

		for i in range(0, len(main)):
			degree.append(degree_temp)
			branch.append(branch_temp)
			company.append(main2[i].find_elements_by_css_selector("td")[1].text)
			placed.append(main2[i].find_elements_by_css_selector("td")[2].text)

		temp= pd.DataFrame()
		temp["degree"]= degree
		temp["branch"]= branch
		temp["placed"]= placed
		temp["company"]=company 
		temp.to_csv("placement/"+ str(branch1)+ ".csv")
		driver.back()

	except Exception as e:
		print(e + str(n))