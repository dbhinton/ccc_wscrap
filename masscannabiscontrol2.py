import requests
import pandas as pd
import json

keywords = ''  # you can search querys
total_data = 0 # you can add number of products you want to scrape 
					  # ex totaldata = 500


url = "https://catalog.metrc.com/v1/searchApi/items/search"
body = '{"query":"'+keywords+'","sort":"relevancy","skip":0,"itemNames":[],\
	"itemCategories":[],"states":[],"licenseNumbers":[],"quantityTypes":[]}'
headers = {
			'Connection': 'keep-alive',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
			'Accept': 'application/json, text/plain, */*',
			'sec-ch-ua-mobile': '?0',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
			'Content-Type': 'application/json;charset=UTF-8',
			'Origin': 'https://catalog.metrc.com',
			'Sec-Fetch-Site': 'same-origin',
			'Sec-Fetch-Mode': 'cors',
			'Sec-Fetch-Dest': 'empty',
			'Accept-Language': 'en-US,en;q=0.9'
			}
# calling request
response = requests.request("POST", url, headers=headers, data=body)
json_data = json.loads(response.text) #get response
if not total_data:
	total_data = int(json_data.get('meta').get('total')) # finding total data of products


skip = 0 # skip product data
json_data = json.loads(response.text)
product_data = []
while skip < total_data: # while product data not more than total_data loop is running continuously
	body = '{"query":"'+keywords+'","sort":"relevancy","skip":'+str(skip)+',"itemNames":[],\
			"itemCategories":[],"states":[],"licenseNumbers":[],"quantityTypes":[]}'
	response = requests.request("POST", url, headers=headers, data=body) # after finding page call request again
	json_data = json.loads(response.text) # get response
	for data in json_data['items']:
		item = {}
		item['Category'] = data.get('category')
		item['facilityName'] = data.get('facilityName')
		imageUrl = data.get('imageUrl')
		if imageUrl:
			item['imageUrl'] = f'https://catalog.metrc.com{imageUrl}'
		else:
			imageUrl = None
		item['ingredients'] = data.get('ingredients')
		item['license'] = data.get('license')
		item['name'] = data.get('name')
		item['quantityType'] = data.get('quantityType')
		item['state'] = data.get('state')
		item['cbd'] = data.get('cbdContent')
		item['cbd_Unit'] = data.get('cbdContentUnitOfMeasure')
		item['cbd_Dose'] = data.get('cbdContentDose')
		item['cbd_Dose_Unit'] = data.get('cbdContentDoseUnitOfMeasure')
		item['cbdPotency'] = data.get('cbdPotency')
		item['thc'] = data.get('thcContent')
		item['thc_Unit'] = data.get('thcContentUnitOfMeasure')
		item['thc_Dose'] = data.get('thcContentDose')
		item['thc_Dose_Unit'] = data.get('thcContentDoseUnitOfMeasure')
		item['thcPotency'] = data.get('thcPotency')
		if len(product_data) == total_data:
			break
		else:
			product_data.append(item) # append each product data into product_data
	skip+=24

df = pd.DataFrame(product_data) # create a dataframe
df.to_excel('metrc_productdata.xlsx',index=False) # saved data into excel
print('Data Saved Successfully')