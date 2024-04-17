import datetime
from requests import get, post, delete, put

# выводит словарь всех пользователей из БД
print(get('http://localhost:5000/api/v2/users').json())

# выводит пользователя с id = 1
print(get('http://localhost:5000/api/v2/users/1').json())

# пользователи с id = 999 нет в базе
print(get('http://localhost:5000/api/v2/users/999').json())

# ошибка (type(id) = int, а не str)
print(get('http://localhost:5000/api/v2/users/q').json())

# ошибка (передан пустой словарь)
print(post('http://localhost:5000/api/v2/users', json={}).json())

# ошибка (переданы не все поля в словаре)
print(post('http://localhost:5000/api/v2/users',
           json={'hobbies': 'Плавание'}).json())

# добавит нового пользователя в БД
print(post('http://localhost:5000/api/v2/users',
           json={'surname': 'Бобров', 'name': 'Андрей', 'age': 24, 'about_me': 'Люблю программировать',
                 'hobbies': 'Плавание', 'city_from': 'Бугульма', 'phone': '+7-925-323-75-98'}).json())

# выводит словарь всех пользователей из БД
print(get('http://localhost:5000/api/v2/users').json())

# пользователя с id = 999 нет в базе
print(delete('http://localhost:5000/api/v2/users/999').json())

# ошибка (type(id) = int, а не str)
print(delete('http://localhost:5000/api/v2/users/q').json())

# удаляет пользователя из БД
print(delete('http://localhost:5000/api/v2/users/1').json())

# выводит словарь всех пользователей из БД
print(get('http://localhost:5000/api/v2/users').json())