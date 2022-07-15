import requests
url = 'https://api.openweathermap.org/data/2.5/weather?zip=46582,us&appid=588bfdcfa93e713cd2753c82805a3cde&units=imperial'
api_key = '588bfdcfa93e713cd2753c82805a3cde'
response = requests.request('GET', url, headers={})
data = response.json()
feelslike=int(data['main']['feels_like'])
print(feelslike)