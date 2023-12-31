import requests
import datetime
from key import API_KEY

api_key = API_KEY



# Запит на сайт openweathermap.org
# Request to openweathermap.org for today's weather
def weather_request(city):
    today_weather_req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
    return today_weather_req



# Виводимо результат на екран
# Display the result on the screen
def print_weather_on_screen(json_text):
    titels = [
    "Температура повітря:",
    "Відчувається як:",    
    "Схід сонця:",   
    "Захід сонця:",  
    "Повітряний тиск:",
    "Напрямок вітру:" ,
    "Швідкість вітру:"]

    result = [
    f"{json_text['main']['temp']} C°  {translate_weather(json_text['weather'][0]['main'])}\n",
    f"{json_text['main']['feels_like']} C°\n",
    f"{datetime.datetime.fromtimestamp(json_text['sys']['sunrise']).strftime('%H:%M')}\n",
    f"{datetime.datetime.fromtimestamp(json_text['sys']['sunset']).strftime('%H:%M')}\n",
    f"{round(json_text['main']['pressure'] * 0.7500637555419211, 2)} мм.рт.ст\n",
    f"{convert_to_wind_direction(json_text['wind']['deg'])}\n",
    f"{json_text['wind']['speed']} м\\с"
    ]
     
    return dict(zip(titels, result))
           
    
# Конвертуємо напрям вітру
# Convert the wind direction
def convert_to_wind_direction(degrees):
    # Список вітрохідних напрямків та їх відповідних діапазонів градусів
    # List of wind directions and their respective degree ranges
    wind_directions = {
        'Північний': (348.75, 11.25),
        'Північно-східний': (11.25, 78.75),
        'Східний': (78.75, 101.25),
        'Південно-східний': (101.25, 168.75),
        'Південний': (168.75, 191.25),
        'Південно-західний': (191.25, 258.75),
        'Західний': (258.75, 281.25),
        'Північно-західний': (281.25, 348.75),
    }

    # Перевірка, щоб кут був у діапазоні [0, 360)
    # Checking that the angle is in the range [0, 360)
    degrees = degrees % 360

    # Пошук відповідного напрямку
    # Finding the right direction
    for direction, (start, end) in wind_directions.items():
        if start <= degrees < end:
            return direction

    
    return 'Помилка'

# Перекладаємо погоду з англійської
# Translate weather from English
def translate_weather(weather):
    weather_dict = {
        'Thunderstorm': 'Гроза',
        'Drizzle': 'Мряка',
        'Rain': 'Дощ',
        'Snow': 'Сніг',
        'Mist': 'Туман',
        'Smoke': 'Дим',
        'Haze': 'Легкий туман',
        'Dust': 'Пил',
        'Fog': 'Туман',
        'Sand': 'Пісок',
        'Ash': 'Попіл',
        'Squall': 'Шквал',
        'Tornado': 'Торнадо',
        'Clear': 'Ясне небо',
        'Clouds': 'Хмарно'
    }
    
    
    for eng, ukr in weather_dict.items():
        if eng == weather:
            return ukr

    return 'Помилка'

#Перевіряємо правільність вводу індекса
#Check if the index is entered correctly
def check_index(len_dict:int):
    try:
        index = int(input('Введіть номер міста: '))
        print('')
    
        if 0 < index <= len_dict:

            return index
        else:
            print('Такого номера нема у списку')
            return check_index(len_dict)
    except:
        print('Введіть числове значення')
        return check_index(len_dict)


def main():
    cities_dict = {
    "Київ": "Kyiv",
    "Харків": "Kharkiv",
    "Одеса": "Odessa",
    "Дніпро": "Dnipro",
    "Донецьк": "Donetsk",
    "Запоріжжя": "Zaporizhzhia",
    "Львів": "Lviv",
    "Кривий Ріг": "Kryvyi Rih",
    "Миколаїв": "Mykolaiv",
    "Маріуполь": "Mariupol",
    "Вінниця": "Vinnytsia",
    "Херсон": "Kherson",
    "Полтава": "Poltava",
    "Чернігів": "Chernihiv",
    "Черкаси": "Cherkasy",
    "Житомир": "Zhytomyr",
    "Суми": "Sumy",
    "Івано-Франківськ": "Ivano-Frankivsk",
    "Тернопіль": "Ternopil",
    "Кропивницький": "Kropyvnytskyi",
    "Ужгород": "Uzhhorod",
    "Луцьк": "Lutsk",
    "Мелітополь": "Melitopol",
    "Кам'янець-Подільський": "Kamianets-Podilskyi",
    "Хмельницький": "Khmelnytskyi",
    "Рівне": "Rivne",
    "Севастополь": "Sevastopol",
    "Сімферополь": "Simferopol"}

    screen_list = dict(enumerate(cities_dict,1))

    for index, city in screen_list.items():
        print (index, city)

    selected_index = screen_list[check_index(len(screen_list))]
  
    selected_city = cities_dict[selected_index]
    text = 'Ви вибрали місто'
    print (f"{text.ljust(20)}   {selected_index}\n")

    today_weather_req = weather_request(selected_city)
    json_text = today_weather_req.json()
    for k,v in print_weather_on_screen(json_text).items():
        print (f"{k.ljust(20)}   {v}")

if __name__ == '__main__':
    main()
