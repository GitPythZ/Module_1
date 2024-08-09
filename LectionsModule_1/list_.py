food = ['apple', 'banana', 'bread'] #список
print(food)
print(food[1]) # выбор элемента списка
food[0] = 'coconut' #замена элемента списка
print(food)
food.append(True) # добавляет объект в конец списка
# So you can use list.append() to append a single value, and list.extend() to append multiple values.
print(food)
food.extend('cucucmber') #перебирает каждый символ элемента и добавляет побуквенно в список
print(food)
food.extend(['string', 'pear'])
print(food)
food.remove('banana') #убрать элемент списка
print(food)
print('coconut' in food) # проверка наличия элемента в списке
print('coconut' not in food) # проверка отсутствия элемента в списке
print(food[0:9])
lst = [1, 2]
lst.append(3)
lst.append(4)
print(lst) #[1, 2, 3, 4]

lst.extend([5, 6, 7])
lst.extend((8, 9, 10))
print(lst) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst.extend(range(11, 14))
print(lst) #1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Если нужно вставить элемент в середину списка, то .insert(item) — это наш выбор:









