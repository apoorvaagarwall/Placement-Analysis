from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

import pandas as pd 

import time 

driver = webdriver.Ie(executable_path = r"C:\Users\1hp\Downloads\IEDriverServer"
	"_x64_3.4.0\IEDriverServer.exe")
driver.get("https://vpn.iitr.ac.in/+CSCO+1h75676763663A2F2F70756E61617279762E7661"
	"++/placement/results/2016/companies")

# no. of offers by the companies
company_list= driver.find_elements_by_css_selector("div#content_middle>table>tbody>tr")


name_companies = []
number_of_offers =[]

for company in company_list:
    name_companies.append(item.find_elements_by_css_selector("td")[1].text)
    number_of_offers.append(item.find_elements_by_css_selector("td")[2].text)

company_list= pd.DataFrame(
	{
	"name": name_companies,
	"number_of_offers":  number_of_offers
	})

company_list.to_csv("companies_data2.csv")