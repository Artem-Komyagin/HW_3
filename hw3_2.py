# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.


def inf(name, surname, date, email, phone):
    name=input('write name -')
    surname=input('write surname- ')
    date=input('write date -')
    email=input('write email -')
    phone=input('write phone -')
    print('name-'+ name, 'surname-'+ surname, 'Date-'+ date, 'email-'+ email, 'phone-'+ phone)
    return
inf(name= ' ', surname= ' ', date= ' ', email= ' ', phone= ' ')

