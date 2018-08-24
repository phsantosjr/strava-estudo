import json
import requests
import configparser
from data_from_http import token_entry
from data_from_lib import cfg

fg = configparser.ConfigParser()
cfg._interpolation = configparser.ExtendedInterpolation()

cfg.read("token_id.ini")
clientid = cfg.get('strava','clientid')
print(clientid)
activity = "1726741296" #(https://www.strava.com/activities/1726741296)

activity = 1726741296  # (https://www.strava.com/activities/1726741296)

response = requests.get("https://www.strava.com/api/v3/athlete"  "Authorization:Bearer "+token_entry)  # athlete
response1 = requests.get("https://www.strava.com/api/v3/activities/1726741296"+token_entry)  # activity
response2 = requests.get("https://www.strava.com/api/v3/athlete/activities/"+token_entry)  # activities

api_instance = response.json()
api_instance1 = response1.json()
api_instance2 = response2.json()

print(api_instance)
print(api_instance1)
#print(api_instance2)

#print(json.dumps(api_instance, indent=4, sort_keys=True))
