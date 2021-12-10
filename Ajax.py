import requests
import csv
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from selenium import webdriver
from pip._vendor.distlib import resources
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import math


import os,sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]
common_dir = "/".join(base_dir.split('/')[:-1])
sys.path.insert(0, base_dir)
sys.path.insert(0, currentdir)
sys.path.insert(0, common_dir)

from Common_intern import *



def GetCount(MakeId,DealerId,start_url,soup, driver):
	# soup = GetSoup_from_selenium(start_url)
	VCnt = 0
	# print(soup)
	if VCnt == 0:#216
		try:
			link1 = soup.find('div', 'facet-breadcrumb-title pull-left')
			# ~ print('1')
			link = link1.find('span', 'vehicle-count')
			text = link.get_text().strip()
			
			VCnt = int(text)
		except: VCnt = 0		
	
	if VCnt == 0:#214
		try:
			link1 = soup.find('div', 'selections')
			# ~ print('2')
			link = link1.find('strong')			
			text = link.get_text().strip()
			
			VCnt = int(text[:text.find(' Items Matching:')].replace(',','').strip())
		except: VCnt = 0
	
	if VCnt == 0:#217
		try:
			link1 = soup.find('div', 'breadcrumb-vehicle-count-wrapper')
			# ~ print('3')
			link = link1.find('div','v3-vehicle-count')			
			text = link.get_text().strip()
			
			VCnt = int(text[:text.find(' Vehicles')].replace(',','').strip())
		except: VCnt = 0
							
	if VCnt == 0:#212
		try:
			link1 = soup.find('span', 'push-half--right')
			# ~ print('4')
			link = link1.find('strong')			
			text = link.get_text().strip()
			
			VCnt=text[text.find(' of ')+4:]
		except: VCnt = 0
		
	if VCnt == 0:#169
		try:
			link1 = soup.find('section', 'listing-count')
			# ~ print('5')
			link = link1.find('h5')	
			link2 = link.find('schema','color viewingTotal')			
			text = link2.get_text().strip()
			VCnt=int(text)
		except: VCnt = 0
		
	if VCnt == 0:#206
		try:
			link1 = soup.find('div', 'search-results-count-title')
			# ~ print('6')
			text = link1.get_text().strip()
			VCnt=int(text[:text.find(' vehicles')].replace(',','').strip())
		except: VCnt = 0
		
	if VCnt == 0:#202
		try:
			link1 = soup.find('section', 'listing-count')
			# ~ print('7')
			link = link1.find('h5')	
			text = link.get_text().strip()
			text = text[text.find(' of ')+4:text.find(' results')]
			VCnt=int(text)
		except: VCnt = 0
		
	if VCnt == 0:#200
		try:
			link1 = soup.find('div', 'filters-action-header')
			# ~ print('8')
			link = link1.find('div','total-found')
			link2 = link.find('span','count')			
			text = link2.get_text().strip()
			VCnt=int(text)
		except: VCnt = 0
		
	if VCnt == 0:#186
		try:
			link1 = soup.find('span', 'ribbon')
			# ~ print('9')
			link = link1.find('strong')
			link2 = link.find('span','number_of_listings')			
			text = link2.get_text().strip()
			VCnt=int(text)
		except: VCnt = 0
							
	if VCnt == 0:#182
		try:
			link1 = soup.find('span', 'TotalCount')
			# ~ print('10')
			link2 = link1.find('span','TotalCountNumber')			
			text = link2.get_text().strip()
			VCnt=int(text[:text.find(' Results')].replace(',','').strip())
		except: VCnt = 0
		
	if VCnt == 0:#179
		try:
			link1 = soup.find('span', 'inventory-listing__results-info-count')
			# ~ print('11')
			text = link1.get_text().strip()
			VCnt=int(text)
		except: VCnt = 0
		
	if VCnt == 0:#134
		try:
			link1 = soup.find('h2', 'mb20')
			# ~ print('12')
			link2 = link1.find('span',id ='ContentPlaceHolderDefault_cphBody_cphBody_ctl00_Inventory_2_lblVFTotalVehicles')			
			text = link2.get_text().strip()
			VCnt=int(text)
		except: VCnt = 0
		
	if VCnt == 0:#133
		try:
			link1 = soup.find('div', id ='paginate_top')
			# ~ print('13')
			link2 = link1.find('div','results_count')	
			text = link2.get_text().strip()
			text = text[text.find(' of ')+4:text.find(' vehicles')]
			VCnt=int(text)
		except: VCnt = 0
		
	if VCnt == 0:#132
		try:
			link1 = soup.find('div', 'col-md-6 text-left')
			# ~ print('14')
			link2 = link1.find('p',id = 'pTopResultsTxt')	
			text = link2.get_text().strip()
			text = text[text.find(' are ')+4:text.find(' vehicles')]
			VCnt=int(text)
		except: VCnt = 0
		
	if VCnt == 0:#129
		try:
			link1 = soup.find('div', 'inv-record inv-record-header')
			# ~ print('15')
			text = link1.get_text().strip()
			text = text[text.find(' of ')+4:text.find(' vehicles')]
			VCnt=int(text)
		except: VCnt = 0
		
	if VCnt == 0:#125
		try:
			link1 = soup.find('div', 'tri')
			# ~ print('16')
			link3 = link1.find('p','pull-left')	
			text = link3.get_text().strip()
			text = text[text.find(' des ')+4:text.find(' résultats')]
			VCnt=int(text)
		except: VCnt = 0
		
	if VCnt == 0:#105
		try:
			link1 = soup.find('div', 'total-count')
			# ~ print('17')
			link = link1.find('span','count')			
			text = link.get_text().strip()
			VCnt = int(text)
		except: VCnt = 0
		
	if VCnt == 0:#101
		try:
			link1 = soup.find('span', 'inventory-list__results-info')
			# ~ print('18')
			link = link1.find('span','inventory-list__results-info-count')	
			text = link.get_text().strip()
			VCnt = int(text)
		except: VCnt = 0
		
	if VCnt == 0:#19
		try:
			link1 = soup.find('div', 'listingHub')
			# ~ print('19')
			link3 = link1.find('div','listing listingResults')	
			text = link3.get_text().strip()
			text = text[text.find('Il y a ')+7:text.find(' résultat(s)')]
			VCnt=int(text)
		except: VCnt = 0
		
	if VCnt == 0:#8
		try:
			link1 = soup.find('div', 'searchResultsCount')
			# ~ print('20')
			text = link1.get_text().strip()
			VCnt=int(text[:text.find(' results')].replace(',','').strip())
		except: VCnt = 0
		
	if VCnt == 0:#153
		try:
			link1 = soup.find('div', 'nbVehicles')
			# ~ print('21')
			link3 = link1.find('span','currentCount')	
			text = link3.get_text().strip()
			VCnt=int(text[:text.find(' results')].replace(',','').strip())
		except: VCnt = 0
		
	if VCnt == 0:#136
		try:
			link1 = soup.find('li', 'result-count')
			# ~ print('22')
			text = link1.get_text().strip()
			text = text[text.find(' is ')+4:text.find(' results')]
			VCnt=int(text)
		except: VCnt = 0
		
	if VCnt == 0:#61
		try:
			link1 = soup.find('fieldset', 'search-engine form-dropdown')
			# ~ print('23')
			link2 = link1.find('legend')	
			link3 = link2.find('a')	
			text = link3.get_text().strip()
			VCnt=int(text[:text.find(' vehicle')].replace(',','').strip())
		except: VCnt = 0
		
	if VCnt == 0:#376
		try:
			link1 = soup.find_all('div', 'text')
			# ~ print('24')
			for link in link1:		
				link2 = link.find_all('div','title')	
				for link3 in link2:
					link4 = link3.find_all('h3')
					for link5 in link4:
						if link5 is not None:
							text = link5.text.strip()
							VCnt=int(text[:text.find(' Vehicles Found')].replace(',','').strip())
		except: VCnt = 0
		
	if VCnt == 0:#372
		try:
			link1 = soup.find('p', 'srpVehicleCount')
			# ~ print('25')
			text = link1.get_text().strip()
			text = text[text.find(' of ')+4:text.find(' Vehicles')]
			VCnt=int(text)
		except: VCnt = 0
	if VCnt == 0:#344
		try:
			link1 = soup.find('h1')
			# ~ print('26')
			link2 = link1.find('span','total-found')			
			text = link2.get_text().strip()
			VCnt=int(text)
		except: VCnt = 0
		
	if VCnt == 0:#8
		# ~ print('27')
		try:
			link1 = soup.find('div', 'srp_results_count_container').find('span')
			text = link1.get_text().strip()
			VCnt=int(text[:text.find(' vehicles found')].replace(',','').strip())
		except: VCnt = 0
	if VCnt == 0:#8
		# ~ print('28')
		try:
			link1 = soup.find('div', 'srp-selected').find('span')
			text = link1.get_text().strip()
			VCnt=int(text[:text.find(' Matching Vehicles:')].replace(',','').strip())
		except: VCnt = 0
		
	if VCnt == 0:#372
		try:
			# ~ print('29')
			link1 = soup.find('span', 'sf-count')
			text = link1.get_text().strip()
			text = text[text.find('(')+1:text.find(')')]
			VCnt=int(text)
		except: VCnt = 0
	
	if VCnt == 0:#108
		try:
			link1 = soup.find('div','resultsCount')
			text = link1.get_text().strip().replace(' found','').replace(' vehicles','')
			VCnt = int(text)
		except: VCnt = 0

	if VCnt == 0:#266
		try:
			link1 = soup.find('div', 'ml-lg-4 vehicle_results_label')
			text = link1.get_text().upper().strip().replace('RESULTS: ','').replace('VEHICLES','')
			VCnt=int(text)
		except: VCnt = 0
		
	if VCnt == 0:#2 selenium
		try:
			link1 = soup.find('div', id = 'inventory-filters1-app-root').find_all('span')
			for sp in link1:
				if 'vehicles' in sp.text.lower().strip():
					text = sp.get_text().upper().replace('RESULTS','').replace('VEHICLES','').replace('FOUND','').replace(':','').strip()
					VCnt=int(text)
		except: VCnt = 0
	if VCnt == 0:#3 selenium
		try:
			link1 = soup.find('span', id = 'results-title').find('span',class_="stats")
			if 'vehicles' in link1.text.lower().strip() or 'RESULTS' in link1.text.upper().strip():
				# ~ text = link1.get_text().upper().replace('RESULTS','').replace('VEHICLES','').replace('FOUND','').replace(':','').strip()
				text = link1.get_text().upper().strip()
				##### remove non-digit character from string
				text = re.sub('\D', '', text)
				VCnt=int(text.strip())
		except: VCnt = 0
	if VCnt == 0:
		try:
			VCnt = soup.find('div',id ='vlp-search-results').find('span',id = 'vehicleCount').get_text().strip()
		except: VCnt = 0
	# if VCnt==0:
	print ('Getcount is ---> ',VCnt)		
	return (VCnt, soup)

# 	return 


# def Next(driver):
# 	try:
# 		if driver.find_element_by_class_name('next').text.strip() in 'Next Page »':
# 			# print(driver.find_element_by_class_name('next').text.strip())
# 			return True
# 	except:pass
	
# 	try:
# 		if driver.find_element_by_class_name('next'):
# 			return True
# 	except:pass
	
# 	# ~ try: #https://www.myislandkia.com, MakeId=85, DealerId=152
# 		# ~ if driver.find_element_by_class_name('btn-xs').send_keys(Keys.RETURN):
# 			# ~ print('print True')
# 			# ~ return True
# 	# ~ except:pass
	
# 	return False


def Next(driver):
	next_button=''#False
	nxt_condition = 0
	try:
		text = driver.find_element_by_class_name('next').text.strip().upper()
	except:pass
	if next_button == '':#False:
		try:
			a_tags = driver.find_element_by_class_name('pagination-next')
			childe_class = ''
			if childe_class == '':
				try:
					childe_class = a_tags.find_element_by_class_name('ddc-icon-arrow1-right')
				except:
					childe_class = ''
					pass
			if childe_class == '':
				try:
					childe_class = a_tags.find_element_by_class_name('glyphicon-menu-right')
				except:
					childe_class = ''
					pass
			if  childe_class != '':
				nxt_condition = 4
				# a.send_keys(Keys.RETURN)
				next_button = True
				# print("next-4")
		except:pass
	if next_button == '':#False:
		try:
			if 'NEXT PAGE »' in text:
				nxt_condition = 1
				next_button = True
				# print("next-1")
		except:pass
	if next_button == '':#False:
		try:
			tag = driver.find_element_by_class_name('next')
			if tag and 'NEXT PHOTO' not in text and '' not in text:
				nxt_condition = 2
				next_button = True
				# print("next-2")
		except:pass
	if next_button == '':#False:
		try:
			findAll_ul = driver.find_elements_by_tag_name('a')
			for a in findAll_ul:
				rel = a.get_attribute('rel')
				if rel == 'next':
					nxt_condition =3
					next_button = True
					# print("next-3")
					break;
		except:pass
	
		
	
	# print(next_button,'--------',nxt_condition)
	return next_button,nxt_condition


def vehicle_url(soup,driver):

	

	# driver.refresh()

	# time.sleep(5)

	html = driver.page_source
	soup = BeautifulSoup(html,'html.parser')


	url =[]
	if url ==[]:
		try:
			find_url = soup.find_all('div','vehicle-overview')
			for a in find_url:
				urls = a.find('div','vehicle-title').find('a')
				# ~ print(urls['href'],'-------------------------------------AJAx')
				url.append(urls['href'])
				print('url-1')
		except:pass
	if url ==[]:
		try:
			i = 1
			find_url = soup.find_all('div','vehicle-wrap')
			for a in find_url:
				urls = a.find('div','vehicle-image').find('a')
				# print(urls['href'])
				url.append(urls['href'])
				print(urls['href'])
				i+=1
		except:pass
	if url ==[]:
		try:
			find_url = soup.find_all('li','resultItem')
			for a in find_url:
				urls = a['data-detailurl']
				# print(urls['href'])
				url.append(urls)
				#print('url-3')
		except:pass
	if url ==[]:
		try:
			findAll_a = soup.find_all('a','url')
			for a in findAll_a:
				urls = a['href']
				# ~ if urls != '/':
				if len(urls) > 10:
					url.append(urls)
					#print('url-4')
		except:pass
	if url ==[]:
		try:	
			v_urls = soup.find_all('a','more-details-link')
			for v in v_urls:
				urls = v['href']
				url.append(urls)
				#print('url-5')
		except:pass
	if url ==[]:
		try:
			find_url = soup.find_all('div','vehicle-title')
			for a in find_url:
				urls = a.find('a')
				# ~ print(urls['href'],'-------------------------------------AJAx')
				url.append(urls['href'])
				#print('url-2')
		except:pass
	if url ==[]:
		try:
			find_url = soup.find_all('a','view-vehicle pull-left vlp-item-title pdtm-vlp-vehicle-name')
			#print('99999',find_url)
			for a in find_url:
				url.append(set(a['href']))
				#print('url-1',url)
		except:pass
	return url



def Ajax_DataProcess(MakeId,DealerId,WebSite,start_url,vehicle_type, selenium_driver_path):
	safe = page_index = 0 
	VehicleUrls=[]
	check = 500
	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")

	# options.add_argument("--disable-javascript")
	driver = webdriver.Chrome(executable_path= "C:\\Users\\Dell\\.wdm\\drivers\\chromedriver\\win32\\91.0.4472.101\\chromedriver.exe",chrome_options=options)
	# ~ driver = webdriver.Chrome(executable_path='/var/WWW/chromedriver/chromedriver',chrome_options=options)

	driver.get(start_url)
	time.sleep(5)
	# ~ driver.refresh() ### don't delet this, due to this driver will not hang
	# ~ time.sleep(3)
	
	try:

		#################### start of page 1 only ###################
		### popup always get on 1 page
		try:## We found similar vehicles you may like at our other locations
			driver.find_element_by_class_name('offsite-button').send_keys(Keys.ENTER)
		except:	pass
		try:
			# to cancel the popup window
			driver.find_element_by_class_name('wdpu-close').click()
		except:pass
		try:
			# to cancel the popup window
			driver.find_element_by_class_name('cookie-agree-btn').click()
		except:pass
		try:
			# to cancel the popup window
			driver.find_element_by_xpath('//*[@id="squeeze-header__close_desktop"]').click()
		except:pass

		time.sleep(2) #dont delet it
		# getting vehicle_url of first page
		html = driver.page_source
		soup = BeautifulSoup(html,'html.parser')

		vehicle_count, soup = GetCount(MakeId,DealerId,start_url,soup, driver)
		VehicleUrls += vehicle_url(soup,driver)
		
		print('Extracted Vehicle URLs... '+ str(len(list(set(VehicleUrls)))) + ', MakeId--> '+ str(MakeId) +' from DealerId--> '+str(DealerId))

		#################### end of page 1 only ###################
		# getting vehicle_url of next page
		while Next(driver)[0] == True:
			# print(Next(driver),'-----Next(driver)')
			nxt_condition = Next(driver)[1]
			if nxt_condition == 4:
				# print('......................dddddd')
				try:
					a_tags = driver.find_element_by_class_name('pagination-next')
					childe_class = ''
					if childe_class == '':
						try:
							childe_class = a_tags.find_element_by_tag_name('a')
						except:
							childe_class =''
							# print('except----------------childe_class')
							pass
					# print(childe_class,'---------------childe_class')
					if childe_class != '':
						try:
							childe_class.send_keys(Keys.RETURN)
							# childe_class.click()
						except:
							childe_class.click()
							# childe_class.send_keys(Keys.RETURN)
					else:
						try:

							try:
								a_tags.click()
							except:
								a_tags.send_keys(Keys.RETURN)
						except:pass
						

				except:pass
				
			if nxt_condition == (1 or 2):
				try:
					driver.find_element_by_class_name('next').send_keys(Keys.RETURN)
					# print('2--------1')
				except:
					# print("Next nhi mila")
					pass

			if nxt_condition == 3:
				try:
					findAll_a = driver.find_elements_by_tag_name('a')
					# print('3--------1')
					for a in findAll_a:
						rel = a.get_attribute('rel')
						# print('3--------2')
						if rel == 'next':
							a.send_keys(Keys.RETURN)
							# print('3--------3')
				except:pass

			time.sleep(5)
			action = ActionChains(driver)
			# getting soup of next_page			
			html = driver.page_source
			soup = BeautifulSoup(html,'html.parser')
			VehicleUrls += vehicle_url(soup,driver)
			VehicleUrls += vehicle_url(MakeId,DealerId,start_url,driver)
			
			## refresh the driver after getting above 500 VehicleUrls
			if len(VehicleUrls) > check:
				driver.refresh()
				print('refreshing driver ********')
				time.sleep(5)
				check = check+500
		

			if page_index < len(list(set(VehicleUrls))):
				page_index = len(list(set(VehicleUrls)))
			else:
				safe +=1

			# print('safe----->', safe, ' page_index-->',page_index, ' len(VehicleUrls)-->',len(VehicleUrls))

			print('Extracted Vehicle URLs... '+ str(len(list(set(VehicleUrls)))) + ', MakeId--> '+ str(MakeId) +' from DealerId--> '+str(DealerId))

			# refresh the driver after getting same VehicleUrls
			if (safe % 3 == 0) and safe > 0 and len(list(set(VehicleUrls))) > 0:
				driver.refresh()
				safe += 1
				print('refreshing driver------>')

			if safe > 12: 
				break
	except:pass

	driver.close()	
	print(len(VehicleUrls),'====',vehicle_count)
	return VehicleUrls, vehicle_count

###for testing-------
MakeId = 79
DealerId = 144
WebSite = 'https://www.sandschryslerjeepdodge.net/'
start_url ='https://www.sandschryslerjeepdodge.net/inventory/new/'
vehicle_type = 'New'
selenium_driver_path ="C:\\Users\\Dell\\.wdm\\drivers\\chromedriver\\win32\\91.0.4472.101\\chromedriver.exe"





Ajax_DataProcess(MakeId,DealerId,WebSite,start_url,vehicle_type, selenium_driver_path)
