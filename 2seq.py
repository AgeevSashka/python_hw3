new_items = input('Введите элементы списка через запятую: ')

new_list = new_items.split(',')
new_items_list =list(set(new_list))

new_items_list.sort()

print('Результат', new_items_list)

# Не понял как сделать дополнительный вариант , точнее как правильно записать условие