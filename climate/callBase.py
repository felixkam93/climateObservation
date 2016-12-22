import requests
import json
import csv
import datetime
import logging
import sys
logging.basicConfig(filename='/home/pi/climate/climate.log',level=logging.DEBUG)

url = 'http://192.168.1.131:3000/api/climates'
ROOM_ID='581f6102c34ccfe0154577f7'
CSVFILE='/home/pi/climate/file.csv'

with open(CSVFILE, 'rb') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
   for row in csvreader:
         if len(row) > 0:
         	humidity = float(row[0])
         	temperature = float(row[1])
         	time = row[2].strip()
         	time = datetime.datetime.strptime(time, "%a %b %d %H:%M:%S %Y")

data = {}
data['time'] = time.strftime("%Y-%m-%d %H:%M:%S")
data['temperature'] = temperature
data['humidity'] = humidity
data['roomId'] = ROOM_ID
json_data = json.dumps(data)

headers = {'Accept': 'application/json'}
try:
    response = requests.post(url, data=data)
except requests.exceptions.RequestException as e:  # This is the correct syntax
	#print "I/O error({0}): {1}".format(e.error.no, e.error.strerror)
        logging.error(e)
	sys.exit(1)

# For successful API call, response code will be 200 (OK)
if(response.ok):

    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jData = json.loads(response.content)
#    print response.text
    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    print(response.content)
    for key in jData:
        print key + " : " + str(jData[key])    

