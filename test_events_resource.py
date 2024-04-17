import datetime
from requests import get, post, delete, put


# выводит словарь всех мероприятий из БД
print(get('http://localhost:5000/api/v2/events').json())

# выводит мероприятие с id = 1
print(get('http://localhost:5000/api/v2/events/1').json())

# мероприятия с id = 999 нет в базе
print(get('http://localhost:5000/api/v2/events/999').json())

# ошибка (type(id) = int, а не str)
print(get('http://localhost:5000/api/v2/events/q').json())

# ошибка (передан пустой словарь)
print(post('http://localhost:5000/api/v2/events', json={}).json())

# ошибка (переданы не все поля в словаре)
print(post('http://localhost:5000/api/v2/events',
           json={'community': 'Иди на ужастик в Мадагаскар'}).json())

# добавит новое мероприятие в БД
print(post('http://localhost:5000/api/v2/events',
           json={'topic': 'Кино', 'community': 'Иду на ужастик в Мадагаскар', 'organizer': 'Елизавета Матвеева',
                 'age_limit': 16, 'area': 'Кинотеатр Мадагаскар', 'is_finished': False}).json())

# выводит словарь всех мероприятий из БД
print(get('http://localhost:5000/api/v2/events').json())

# мероприятия с id = 999 нет в базе
print(delete('http://localhost:5000/api/v2/events/999').json())

# ошибка (type(id) = int, а не str)
print(delete('http://localhost:5000/api/v2/events/q').json())

# удаляет мероприятие из БД
print(delete('http://localhost:5000/api/v2/events/2').json())

# выводит словарь всех мероприятий из БД
print(get('http://localhost:5000/api/v2/events').json())