from faker import Faker
import requests
import json

fake = Faker(['uk_UA'])

url = 'http://127.0.0.1:8000/person'
count = 1000

for _ in range(count):
    firstname = fake.first_name_male()
    surname = fake.last_name_male()
    patronymic = fake.middle_name_male()
    dateOfBirth = fake.date()
    rnokpp = str(fake.random_number(digits=10, fix_len=True))
    unzr = str(fake.random_number(digits=14, fix_len=True))
    pasportNumber = str(fake.random_number(digits=9, fix_len=True))
    sex = "male"
    lineitems = []
    # Дані, які будуть надіслані у запиті
    data = {
        'name': firstname,
        'surname': surname,
        'patronym': patronymic,
        'dateOfBirth' : dateOfBirth,
        'rnokpp' : rnokpp,
        'unzr': unzr,
        'passportNumber': pasportNumber,
        'gender' : "male"
    }

    print("data=", data)
    print(type(data))
    json_data = json.dumps(data, ensure_ascii=False, indent=4)
    print(json_data)
    try:
        json_object = json.loads(str(json_data))
        print("JSON is valid")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")

    headers = {
        'Content-Type': 'application/json',  # Вказуємо тип контенту як JSON
    }

    # Надсилання POST-запиту

    print("json_send_data = " ,json_data)
    response = requests.post(url, json=data, headers=headers)

    # Перевірка статусу відповіді
    if response.status_code == 200:
        print('Запит успішно виконаний')
        print('Відповідь:', response.json())  # Якщо відповідь у форматі JSON
    else:
        print('Помилка виконання запиту')
        print('Статус код:', response.status_code)
        print('Текст відповіді:', response.text)





