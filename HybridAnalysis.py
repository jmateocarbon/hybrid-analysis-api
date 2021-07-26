#Just a Simple code to use hybrid analysis as a security tool instead of visiting the website.

#Part of a central IRA project I am working on
import requests
import json
import config

class Hybrid_Analysis():

#Hybrid Analysis
	def url_Scanning(self):
		#Hybrid Analysis API Key
		HA_Key = config.HA_Key
		input_url = input("Please enter URL: ")
		scan_url = 'https://www.hybrid-analysis.com/api/v2/quick-scan/url'

		#API HEADERS AND DATA
		headers = {
			'Accept': 'application/json', 
			'User-Agent': 'Falcon Sandbox', 
			'api-key': HA_Key, 
			'Content-Type': 'application/x-www-form-urlencoded'
 		}
		payload={'url': input_url, 'scan_type': 'all'}

		# POST METHOD
		response = requests.post(scan_url, headers=headers, data=payload)

		# JSON Parsing	
		json_data = response.json()
		json_string = json.dumps(json_data)
		final_respoonse = json.loads(json_string)
		scan_id = final_respoonse['id']

		# GET Result Of Scan to import to JSON
		report_url = 'https://www.hybrid-analysis.com/api/v2/quick-scan/' + scan_id
		response_r = requests.get(report_url, headers=headers)
		final_report = json.dumps(response_r.json(), indent=4)
		print(final_report)


		with open('hybrid-analysis.json', 'w') as json_file:
			json.dump(response_r.json(), json_file, sort_keys = True, indent = 4,
               ensure_ascii = False)

	def file_hash_scanning(self):
		HA_Key = config.HA_Key
			

Hybrid_Analysis_init=Hybrid_Analysis()
Hybrid_Analysis_init.url_Scanning()			


