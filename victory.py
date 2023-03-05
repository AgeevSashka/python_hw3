import random

write_dates = {
    'Двадцать шестое ноября 1799 года': '26.11.1799',
    'Двадцать третье ноября 1803 года': '23.11.1803',
    'Двадцатое марта 1807 года': '20.03.1807',
    'Третье октября 1814 года': '03.10.1814',
    'Десятое декабря 1821 года': '10.12.1821',
    'Двадцать восьмое августа 1828 года': '28.08.1828',
    'Двадцать второе октября 1870 года': '22.10.1870',
    'Одиндцатое июля 1889 года': '11.07.1889',
    'Двадцать шестое апреля 1564 года': '26.04.1564',
    'Одинадцатое ноября 1821 года': '11.11.1821',
}
writers = {
    'Пушкин': '26.11.1799',
    'Тютчев': '23.11.1803',
    'Гоголь': '20.03.1807',
    'Лермонтов': '03.10.1814',
    'Некрасов': '10.12.1821',
    'Толстой': '28.08.1828',
    'Бу́нин': '22.10.1870',
    'Ахма́това': '11.07.1889',
    'Шекспир': '26.04.1564',
    'Достоевский': '11.11.1821',
}
new_list = []
for key in writers.keys():
    new_list.append(key)

answers_writers = random.sample(new_list, 5)
entered_correctly = 0
entered_incorrectly = 0

i = 0
while i < len(answers_writers):
    answer = input(f'В каком году родился {answers_writers[i]} ? , Введите в формате dd.mm.yyyy  ')
    for item in writers.items():  # Перебор Словаря на ключ и значение
        if item[1] == answer and answers_writers[i] == item[0]:  # Условие отрабатывается если введенные данные верны
            print("Это правильно")
            entered_correctly += 1
        else:
            for itm in write_dates.items():  # Перебор текстового Словаря
                if answers_writers[i] == item[0] and item[1] == itm[1]:  # Условие если пользователь ввел не правильно
                    print(itm[0])
                    entered_incorrectly += 1


    i += 1

    if i == len(answers_writers):
        print(f'Введено правильно {entered_correctly}')
        print(f'Введено правильно {entered_incorrectly}')
        answer = input('Хотите начать игру заново ?')
        if answer == 'да':
            i -= len(answers_writers)
        else:
            print('Конец игры')
            break