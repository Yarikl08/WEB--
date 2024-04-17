from requests import get, post, delete, put


# выводит словарь всех сообществ из БД
print(get('http://localhost:5000/api/v2/communities').json())

# выводит сообщество с id = 1
print(get('http://localhost:5000/api/v2/communities/1').json())

# сообщества с id = 999 нет в базе
print(get('http://localhost:5000/api/v2/communities/999').json())

# ошибка (type(id) = int, а не str)
print(get('http://localhost:5000/api/v2/communities/q').json())

# ошибка (передан пустой словарь)
print(post('http://localhost:5000/api/v2/communities', json={}).json())

# ошибка (переданы не все поля в словаре)
print(post('http://localhost:5000/api/v2/communities',
           json={'topic': 'Спорт'}).json())

# добавит новое сообщество в БД
print(post('http://localhost:5000/api/v2/communities',
           json={'topic': 'Игры',
                 'title': 'Шахматы',
                 'in_detail': 'Шахматы в парке Культуры и отдыха', 'organizer': 2, 'members': '4, 5',
                 'contacts': 'artem_k@mail.ru'}).json())

# выводит словарь всех сообществ из БД
print(get('http://localhost:5000/api/v2/communities').json())

# сообщества с id = 999 нет в базе
print(delete('http://localhost:5000/api/v2/communities/999').json())

# ошибка (type(id) = int, а не str)
print(delete('http://localhost:5000/api/v2/communities/q').json())

# удаляет сообщество из БД
print(delete('http://localhost:5000/api/v2/communities/2').json())

# выводит словарь всех сообществ из БД
print(get('http://localhost:5000/api/v2/communities').json())