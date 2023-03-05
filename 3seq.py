new_list = []
new_sec_list = []

i = 1
#Первый список
while i < 6:
   new_item = int(input(f'Введите {i} элемент первого списка:  '))
   new_list.append(new_item)
   i += 1
new_list.sort()
#Второй список

t = 1
while t < 3:
   new_item = int(input(f'Введите {t} элемент второго списка:  '))
   new_sec_list.append(new_item)
   t += 1
new_sec_list.sort()

for item in new_sec_list:
    if item in new_list:
        new_list.remove(item)

print('Результат:  ', new_list)
