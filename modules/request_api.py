import requests
# Ми імпортуємо з файлу read_json функцію read_json() яка дозволяє читати файли з розширенням json
from .read_json import read_json
# Імпортуємо додуль json який допоможе нам у роботі з файлами json
import json
# У цьому файлі ми використовуємо власну функцію read_json() для читання файлу config_api.json
data_api = read_json(name_file= 'config_api.json')
# Записуемо дані ключа api_key у константу
API_KEY = data_api['api_key']
# Записуемо дані ключа data_api у константу
CITY_NAME = data_api['city_name']
# Додаємо у константу посилання 
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
# Отримуємо необхідні данні з посилання
response = requests.get(URL)
# Умова яка говорить що при успішному підключенні повинно виконуватись:
if response.status_code == 200:
    # Завантажити данні
    data_dict = json.loads(response.content)
    # Вивести правильно у термінал 
    print(json.dumps(data_dict, indent= 4))