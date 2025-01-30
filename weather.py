import requests
import json
import statistics

def get_forecast() -> None:
    url = 'https://api.weather.gov/gridpoints/TOP/32,81/forecast'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        periods = data['properties']['periods']
        periods = periods[0:3]
        print('Weather forecast!\n')
    else:
        return
    print_forecast(periods)


def print_forecast(periods) -> None:
    temps = []
    winds = []
    for i in periods:
        print(i['name'])
        temp_in_f = i['temperature']
        temp_in_c = f_to_c(temp_in_f)
        temps.append(temp_in_c)
        print(f'Temperature: {temp_in_f}F; {temp_in_c}C')
        speed_in_mph = int(i['windSpeed'].split()[0])
        speed_in_kph = mph_to_kph(speed_in_mph)
        winds.append(speed_in_kph)
        print(f'Wind Speed: {speed_in_mph}MPH; {speed_in_kph}KPH')
        print()

    avg_temp = statistics.mean(temps)
    avg_wind = statistics.mean(winds)

    if avg_temp > 0 and avg_temp < 10:
        print(f'Average Temperature: {avg_temp}C: button up the jacket!')
    elif avg_temp < 0:
        print(f'Average Temperature: {avg_temp}C: plug in your cars and put on your hats!')
    else:
        print(f'Average Temperature: {avg_temp}C: shorts sound good!')

    if avg_wind < 5:
        print(f'Average Wind: {avg_wind}KPH: you wont blow away today!')
    else:
        print(f'Average Wind: {avg_wind}KPH: hold on to your hats!')


def f_to_c(temp_in_f: float) -> float:
    return round((temp_in_f - 32) / (9/5), 2)

def mph_to_kph(speed_in_mph: float) -> float:
    return round(speed_in_mph * 1.609344, 2)


if __name__ == '__main__':
    get_forecast()
