import requests


res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
# for i in res.values():
print (str((res['Valute']["USD"]['Name'],res['Valute']["USD"]['Value'])))

print (', '.join(res['Valute'].keys()))
