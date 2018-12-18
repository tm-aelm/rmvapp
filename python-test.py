import requests

accessId = "c4a7a6b0-fec2-4f0f-9bac-d76fb1058bca"
dietzenbachId = 3011520
rtMode = "FULL"
lines = "S2"
formatResponse = "json"

msg = "hello world!"
print(msg)


payload = {'accessId': accessId, 'id': dietzenbachId, 'format': "json", 'lines': lines, 'rtMode': rtMode}
r = requests.get('https://www.rmv.de/hapi/departureBoard', params=payload)

print (r.url)


print (r.json())