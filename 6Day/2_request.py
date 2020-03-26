import requests

response = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
json_data = response.json()
print(json_data)

result = json_data['RealtimeCityAir']
row = result['row']

for gu in row:
    if gu['IDEX_MVL'] < 70.0:
        print (gu['MSRSTE_NM'], gu['IDEX_MVL'])
