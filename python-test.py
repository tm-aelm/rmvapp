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

#CONSOLE TEST OUTPUT
msg = "hello world!"
printme(msg)

#PAYLOAD TESTS
payload_rmv = {'accessId': ACCESS_ID, 'id': DIETZENBACH_ID, 'format': FORMAT, 'lines': LINES, 'rtMode': RT_MODE}
payload_ow = {'id': DIETZENBACH_LOC_ID, 'APPID': APP_ID, 'units': UNIT}

r_rmv = requests.get(RMV_URI, params=payload_rmv)
r_ow = requests.get(OW_FORECAST, params=payload_ow)

printme(r_rmv.url)
printme(r_rmv.json())

printme(r_ow.url)
printme(r_ow.json())


