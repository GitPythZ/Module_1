# Кортеж, как и список - это коллекция. НО он неизменяемый
tuple_ = 1,2,3,4,5
tuplle_2 = (1,2,3,4,5)
tuple_3 = tuple([1,2,3,4,5])
print(tuple_)
print(tuplle_2)
print(tuple_3)
# Кортеж это неизменяемая упорядоченная коллекция. Кортеж содерджит разные типы данных.
# тем не менее внутри он может содержать изменяемые типы (строковый, числовый тип даненых относится к неизменяемым).
# Как в списках, к элементам кортежа можно обратиться
print(tuple_[0])
# Нор заменить данный элемент на что-то другое, как в списке мы не сможем, питон выдаст ошибку.
# если я введу команду - tuple_[0] = 0, то питон заругается 'TypeError: "tuple' object does not support item assignment"
# Кортеж не поддерживает обращение (замену) по элементам!
tuple_4= 6,7,8,9,0
list4 = [6,7,8,9,0]
print(tuple_4.__sizeof__())
print(list4.__sizeof__())
# ортеж занимает меньше места, что полезно, если есть большие библиотеки, котоыре ты не собираешься изменять
# Несмотря на неизменяемость самого кортежа, в себе он может хранить какие-то изменяемые объекты
tuple_5 = [1,2,3, 'четыре', 5], 6,7,8
print(tuple_5)
tuple_5[0][0] = 'one'
print(tuple_5)
tuple_5[0][0:2] = 'one'
print(tuple_5)
print(len(tuple_5))
print(tuple_5)
# Кортежи поддерживают конкатенацию и умножение
cortege_ = 1,3
cortege_2 = 2,4
print(cortege_*3)
print(cortege_+cortege_2)






