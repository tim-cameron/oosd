import urllib2
import sys
import json
import pprint
import threading
MET_BASE = 'http://metservice.com/publicData/'


API_OPTIONS = {
    'LOCAL_FORECAST': 'localForecast',
    'SUN_PROTECTION_URL': 'sunProtectionAlert',
    'ONE_MIN_OBS': 'oneMinObs_',
    'HOURLY_OBS_AND_FORCAST': 'hourlyObsAndForecast_',
    'LOCAL_OBS': 'localObs_',
    'TIDES': 'tides_',
    'WARNINGS': 'warningsForRegion3_urban.',
    'RISE_TIMES': 'riseSet_',
    'POLLEN_LEVELS': 'pollen_town_',
    'DAILY_FORECAST': 'climateDataDailyTown_{0}_32',
}

class Weather(threading.Thread):
    def __init__ (self, city):
        threading.Thread.__init__(self);
        self.city = city;

    def get_response(self, url):
        try:
            response = urllib2.urlopen(url)
        except urllib2.HTTPError:
            return None
        return json.loads(response.read())
    def run(self):
        for key in API_OPTIONS.iterkeys():
            if key == 'DAILY_FORECAST':
                url = ''.join([MET_BASE, API_OPTIONS[key].format(self.city)])
            else:
                url = ''.join([MET_BASE, API_OPTIONS[key], self.city])
            print url
            pprint.pprint(self.get_response(url))
