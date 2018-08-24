from stravalib import unithelper
from stravalib.client import Client
import configparser
from data_from_http import token_entry
from data_from_lib import cfg

fg = configparser.ConfigParser()
cfg._interpolation = configparser.ExtendedInterpolation()

cfg.read("token_id.ini")
clientid = cfg.get('strava','clientid')
print(clientid)


client = Client()
authorize_url = client.authorization_url(clientid, redirect_uri='http://127.0.0.0.0:8100/authorized')
# Have the user click the authorization URL, a 'code' param will be added to the redirect_uri

client = Client(token_entry) #inserting the token

# Currently-authenticated (based on provided token) athlete

# setting the athlete specific activity
curr_athlete = client.get_athlete()
activity = client.get_activity(1726741296) # method to take specific activity
print("type={0.type} distance={1} km".format(activity,
                                         unithelper.kilometers(activity.distance)))


# method to take more activities and its informations
for activity in client.get_activities(after = "2010-01-01T00:00:00Z",  limit=10):
    print("{0.name} {0.moving_time}".format(activity),"type={0.type} distance={1} ".format(activity,
                                         unithelper.kilometers(activity.distance)))