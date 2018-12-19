import requests

#ENDPOINTS
RMV_URI = 'https://www.rmv.de/hapi/departureBoard'
OW_FORECAST = 'https://api.openweathermap.org/data/2.5/forecast'

# Access ID für RMV API
ACCESS_ID = "c4a7a6b0-fec2-4f0f-9bac-d76fb1058bca"

#Access ID für OpenWeather API
APP_ID = "5181ee03d917c82a38079af6dc21a540"

#STATIONSCODES
DIETZENBACH_ID = 3011520
HAUPTWACHE_ID = 3000001
#NIEDERNHAUSEN_ID =
#OF_OST_ID = 
#OSTENDSTR_ID =

#OPEN WEATHER LOCATION IDs
DIETZENBACH_LOC_ID = 2937040

#LINIEN
LINES = "S2"

#FORMATE & REAL-TIME MODUS
FORMAT = "json"
RT_MODE = "FULL"
UNIT = "metric"

#Standard Print function to console
def printme(str):
    print(str)
    return

#PAYLOAD TESTS
payload_rmv = {'accessId': ACCESS_ID, 'id': DIETZENBACH_ID, 'format': FORMAT, 'lines': LINES, 'rtMode': RT_MODE}
payload_ow = {'id': DIETZENBACH_LOC_ID, 'APPID': APP_ID, 'units': UNIT}

r_rmv = requests.get(RMV_URI, params=payload_rmv)
r_ow = requests.get(OW_FORECAST, params=payload_ow)

data_rmv = r_rmv.json()
data_ow = r_ow.json()

#GENERAL API CALL INFOS
print ("Server Version: " + data_rmv['serverVersion'])
print ("Request ID: " + data_rmv['requestId'])
print ("API Call Status Code RMV: " + str(r_rmv.status_code))
print ("API Call Status Code OpenWeather: " + str(r_ow.status_code))
print ("---" '\n' '\n')

#WEATHER INFO
print ("Current Forecast time: " + str(data_ow['list'][0]['dt_txt']))
print ("Current Temperature: " + str(data_ow['list'][0]['main']['temp']))
print ("Current Weather: " + data_ow['list'][0]['weather']['main'])
print ("Current Weather ID: " + str(data_ow['list'][0]['weather']['main']))

print ("Next Forecast time: " + str(data_ow['list'][1]['dt_txt']))
print ("Current Temperature: " + str(data_ow['list'][1]['main']['temp']))
print ("Current Weather: " + str(data_ow['list'][1]['weather']['main']))
print ("Current Weather ID: " + str(data_ow['list'][1]['weather']['main']))
print ("---" '\n' '\n')


for each in data_rmv['Departure']:
    print ("S-Bahn Linie: " + each['Product']['line'])
    print ("Richtung: " + each['direction'])
    print ("Haltestelle: " + each['stop'])
    print ("Datum: " + each['date'])
    print ("Uhrzeit: " + each['time'])
    print ("Status: " + each['prognosisType'])
    print ("---" '\n' '\n')