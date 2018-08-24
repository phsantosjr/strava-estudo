from stravalib import unithelper
import configparser
from stravalib.client import Client

cfg = configparser.ConfigParser()
cfg._interpolation = configparser.ExtendedInterpolation()

cfg.read("token_id.ini")

cfg.sections()
cfg.items('strava')
token_entry = cfg.get('strava','token_entry')
clientid = cfg.get('strava','clientid')
activity = cfg.get('strava','activity')


client = Client()
authorize_url = client.authorization_url(clientid, redirect_uri='http://127.0.0.0.0:8100/authorized')
# Have the user click the authorization URL, a 'code' param will be added to the redirect_uri

client = Client(access_token=token_entry)


# Currently-authenticated (based on provided token) athlete
curr_athlete = client.get_athlete() # This is now me

# Saying hello
athlete = client.get_athlete()
print("Hello, {}".format(athlete.firstname))

# Showing the friends
athlete = client.get_athlete_clubs()
for a in athlete:
    print("{} is your club.".format(a))


# Testing the activities
# setting the athlete specific activity
activity_1 = client.get_activity(activity)

# method to take more activities and its informations
for activity in client.get_activities(after = "2010-01-01T00:00:00Z",  limit=1):
    print("{0.name} {0.moving_time}".format(activity),
          "type={0.type} distance={1} ".format(activity, unithelper.kilometers(activity.distance)))