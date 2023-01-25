import requests

API_KEY = '02bdb68e82ffeab12c287d8c45f8b48c'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# find out which city
city = input("Please Enter a City Name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

# retrieve request
response = requests.get(request_url)

if response.status_code == 200:  # it means successful
    data = response.json()

    weather = data['weather'][0]['description']
    print(f"The weather in {city} is {weather}")
    temperature = round(1.8 * (data["main"]['temp'] - 273) + 32)
    print(f'and the temperature is {temperature}' + u'\N{DEGREE SIGN}f')
else:
    print("An error has occured!")
