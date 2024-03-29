import requests
import json
api_key = 'vMKpoC6SfA4g21zw0PzlkPCTQ2IeCHGR'
url = f'http://dataservice.accuweather.com/currentconditions/v1/210841?apikey={api_key}&details=truea'
response = requests.get(url)

if response.ok:
    data = json.loads(response.text)
    print(data)
    # پردازش داده‌های JSON در اینجا
else:
    print('Error: ', response.status_code)