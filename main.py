import requests
import json
import datetime
import calendar

from config import api_keys

def authenticateBestTimeAPI():
    url = "https://besttime.app/api/v1/keys/" + api_keys.BESTTIME_API_KEY
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode('utf8')) # debug
    return

def getForecast(venueName, venueAddress):
    forecastUrl = "https://besttime.app/api/v1/forecasts"
    params = {
        'api_key_private': api_keys.BESTTIME_API_KEY,
        'venue_name': venueName,
        'venue_address': venueAddress
    }
    response = requests.request("POST", forecastUrl, params=params)
    data = json.loads(response.text)
    print(data)  # debug
    return data

def produceSuggestedTime(data, date):
    hour = date.hour
    dayOfWeek = date.weekday()
    closeTime = data["analysis"][dayOfWeek]["day_info"]["venue_closed"]
    openTime = data["analysis"][dayOfWeek]["day_info"]["venue_open"]
    
    # compile list of closed hours
    busyHours = data["analysis"][dayOfWeek]["busy_hours"]
    closedHours = []
    for x in range(23):
        if (closeTime + x) % 24 != openTime:
            closedHours.append((closeTime + x) % 24)
        else:
            break
    
    # find the first non-busy time
    suggestedDay = dayOfWeek
    suggestedHour = 0
    for x in range(23):
        targetHour = hour + x
        if targetHour >= 24:  # the best time is 'tomorrow'
            suggestedDay = (suggestedDay + 1) % 7
            targetHour = targetHour % 24
        if closedHours.count(targetHour) == 0 and busyHours.count(targetHour) == 0:
            suggestedHour = targetHour
            break
    suggestedDayAndHour = "You should try to arrive at " + calendar.day_name[suggestedDay] + " at " + str(suggestedHour) + "."
    return suggestedDayAndHour
  
# main driver code
def findBestTime(location): 
    locationArr = location.split(", ")
    venueName = locationArr[0]
    locationArr.pop(0)
    separator = ", "
    venueAddress = separator.join(locationArr)
    authenticateBestTimeAPI()
    data = getForecast(venueName, venueAddress) 
    suggestedTime = produceSuggestedTime(data, datetime.datetime.now())
    return suggestedTime
 