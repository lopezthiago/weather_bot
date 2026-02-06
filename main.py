import requests
import os

def main():
    rain = rain_check()
    send_message(rain)

def rain_check() -> bool:
    MY_LAT = -34.494028
    MY_LONG = -58.484772

    WEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY")

    weather_params = {
        'lat': MY_LAT,
        'lon': MY_LONG,
        'appid': WEATHER_API_KEY,
        'cnt': 4,
    }
    response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=weather_params)
    response.raise_for_status()
    weather_data = response.json()

    for hour_data in weather_data['list']:
        condition = hour_data['weather'][0]['id']
        if int(condition) < 700:
            return True
    return False

def send_message(rain):
    TELEGRAM_TOKEN = os.environ.get('TELEGRAM_API_KEY')
    CHAT_ID = '8556884992'

    text = 'gonna rain gng. 🫩' if rain else 'no rain today bby. see u tonight 😘'

    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': text
    }

    response = requests.post(url, data=payload)
    response.raise_for_status()
    data = response.json()



if __name__ == '__main__':
    main()
