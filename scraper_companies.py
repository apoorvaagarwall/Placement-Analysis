from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

import pandas as pd 

import time 


name=[]
category = []
branch_UG = []
branch_PG = []
CTC_UG = []
CTC_PG = []
sector=[]
name_of_post=[]
Total_vacancies =[]
CGPA_requirement = []

driver = webdriver.Ie(executable_path = r"C:\Users\1hp\Downloads\IEDriverServer_x64_3.4.0\IEDriverServer.exe")
driver.get("https://vpn.iitr.ac.in/+CSCO+1h75676763663A2F2F70756E61617279762E7661++/placement/company/list/")
homepage_wait= WebDriverWait(driver, 10).until(
	EC.visibility_of_element_located((By.ID, "all_companies")))
AllCompanies = driver.find_elements_by_css_selector("div#all_companies>table>tbody>tr")


for n in range(0, len(AllCompanies)):

    try:
        homepage_wait
        AllCompanies = driver.find_elements_by_css_selector("div#all_companies>table>tbody>tr")
        name_of_company= AllCompanies[n].find_elements_by_css_selector("td")[1].find_element_by_css_selector("a").text

        if name_of_company not in name:
        	#basic_information
            name.append(name_of_company)
            category.append(AllCompanies[n].find_elements_by_css_selector("td")[2].text)


            #opened for graduate and undergraduate branches
            driver.get(AllCompanies[n].find_elements_by_css_selector("td")[4]
            	.find_element_by_css_selector("a").get_attribute("href"))
            WebDriverWait(driver, 20).until(
            	EC.visibility_of_element_located((By.CSS_SELECTOR, "div#main")))

            #Undergraduate
            try:
             	elem= driver.find_element_by_css_selector("div#Under_Graduate")
             	driver.execute_script("arguments[0].setAttribute('class','tab-pane active')", elem)
             	items= elem.find_elements_by_css_selector("ul>li")

             	for item in items:
             		branch_UG0.append(item.text)

             	branch_UG.append(branch_UG0)

            except NoSuchElementException:
                branch_UG.append("NA")

            #PostGraduate
            try:
                branch_PG0=[]
                elem = driver.find_element_by_css_selector("div#Post_Graduate")
                driver.execute_script("arguments[0].items('class','tab-pane active')", elem)
                items = elem.find_elements_by_css_selector("ul>li")
                for item in items:
                    branch_PG0.append(item.text)
                branch_PG.append(branch_PG0)

            except NoSuchElementException:
                branch_PG.append("NA")
            driver.back()

            #Details about company
            homepage_wait
            driver.get(driver.find_elements_by_css_selector("div#all_companies>table>tbody>tr")[n]
            	.find_elements_by_css_selector("td")[1]
            	.find_element_by_css_selector("a").get_attribute("href"))

            company_details= driver.find_elements_by_css_selector("div#content_middle>table>tbody>tr")
            CTC_UG.append(company_details[5].find_elements_by_css_selector("td")[1].text)
            CTC_PG.append(company_details[6].find_elements_by_css_selector("td")[1].text)
            CGPA_requirement.append(company_details[9].find_elements_by_css_selector("td")[1].text)
            Total_vacancies.append(company_details[25].find_elements_by_css_selector("td")[1].text)
            sector.append(company_details[28].find_elements_by_css_selector("td")[1].text)
            name_of_post.append(company_details[22].find_elements_by_css_selector("td")[1].text)


            driver.back()
            time.sleep(1)


    except TimeoutException:
        print("ERROR ")
        print(n)
        continue

comapnies_data = pd.DataFrame(
	{
	"Company_name": name,
	"Category": category,
	"Branch_UG": branch_UG,
	"Branch_PG": branch_PG,
	"CTC_UG": CTC_UG,
	"CTC_PG": CTC_PG,
	"Sector": sector,
	"Name_of_post_offered": name_of_post,
	"Total_Vacancies": Total_Vacancies,
	"CGPA_requirement_if_any": CGPA_requirement
	})       

comapnies_data.to_csv("companiesdata.csv")