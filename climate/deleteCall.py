import requests
import json 
url = 'http://192.168.1.131:3000/api/climates'
headers = {'Accept': 'application/json'}
response = requests.get('http://192.168.1.131:3000/api/climates?filter={"where":{"or":[{"time":"2016-12-12T23:00:02.000Z"}]}}', headers=headers)

if(response.ok):

    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
	#data = str(response.content)
    #jData = json.loads()
#    print response.text
    #print("The response contains {0} properties".format(len(jData)))
    #print(len(jData))
	json_response = {}
	json_response = json.loads(response.content.decode('utf-8'))
	#print(json_response)
	#print(response.content)
	for i in json_response:
		print(i['id'])
		urlDelete = 'http://192.168.1.131:3000/api/climates/' + i['id']
		print(urlDelete)
		print(urlDelete)
		try:
			r2 = requests.delete(urlDelete)
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			sys.exit(1)
			