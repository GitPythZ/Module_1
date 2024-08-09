name = 'Uraban'
print(name, type(name))
name = 10
print(name, type(name))
name = 10,5
print(name, type(name))
name = [1, 2, 3, 4, 5]
print(name, type(name))
# Как мы помним, переменная является частью памяти, в которую мы помещаем объект, чтобы использовать позже.
# В Python работать напрямую с адресами памяти не представляется возможным.
# Однако, есть одно исключение – функция id, которая в определенных реализациях может показать нам адрес памяти объекта.
# Тем не менее ее основная и, пожалуй, единственная цель, это проверить ссылаются ли два имени на один и тот же объект,
# т. к. обратиться по этому адресу средствами Python невозможно.
# В каждом из этих случаев мы видим, что одна и та же переменная «name» ссылается на объекты разных типов.
# Если совсем углубляться, то можно сказать, что Python не совсем воспринимает такое понятие как переменная.
# Чтобы полностью передать смысл, правильнее будет сказать, что это имя или же идентификатор, ссылающийся на объект.
print(id(name))
x = 50
y = x
z = 50
v = 42
print(id(x))
print(id(y))
print(id(z))
print(id(v))
print(id(x) == id(y))
# ПРИМЕРЫ ФУНКЦИИ PYTHON ID
# PYTHON ID() для встроенных типов данных
str1 = 'Python'
print(id(str1))
str2 = 'Python'
print(id(str2))
print(id(str1) == id(str2))
list1 = ['лебедь', 'рак', 'и', 'щука']
print(id(list1[0]))
print(id(list1[1]))
print(id(list1[2]))
print(id(list1[3]))
print(id(list1[2]) == id(list1[3]))
# PYTHON ID() для пользовательского объекта Python id() for custom object
# В этом примере мы создаем класс Python и мы создаем два объекта класса Python и проверяем их идентификаторы,
# чтобы получить идентификатор объекта в Python.
class MyClass:
	pass
# Create two instances of MyClass
obj1 = MyClass ()
obj2 = MyClass()
print(type(MyClass))
# Print the id of each object
print(id(obj1))
print(id(obj2))
print('space')
# Python id() with Sets (наборы, списки)
set1 = {1, 2, 3}
set2 = {3, 2, 1}
set3 = {1, 2, 3}
print(id(set1)) # Output: <id1>
print(id(set2)) # Output: <id2>
print(id(set3)) # Output: <id3>
print('space')
# PYTHON ID() with tuples (кортежи?!)
tuple1 = (1, 2, 3)
tuple2 = (3, 2, 1)
tuple3 = (1, 2, 3)
print(id(tuple1)) # Output: <id1>
print(id(tuple2)) # Output: <id2>
print(id(tuple3)) # Output: <id3>



