print(5) # напиши  "5"
print (type(5)) # выведи тип: 'Int' - Integer - целое число.
print(5.5)
print(type(5.5)) #покажи тип: float - - плавающая точка (дробное число)
print(5+5) #покажи сумму 5+5, '-' - вычитание, * - умножение, / - деление, // - целочисленное деление, % - остаток при делении, дает понять четное или нечетное число
print(5//5)
print(5 * 5)
print(5/5)
print(5//5)
print(5**3) # возведение в степень: '**'
print('Hello world!') # для работы с текстом выделяй его в кавычки '' или ""
print(type('Hello world!')) # тип 'str' - string (строка)
print('Hello, ' + 'world!') # concateтate - сложение строк
print(True, False) # Boolean - логический тип данных
print(type(True), type(False))
print(5>11, 4<20) # равенство ==, >= больше либо равно, <= меньше либо равно, != неравенство
print(5<4 and 5!=10) # and строгий оператор, все условия должны быть правдивы чтобы получить True
print(5<4 or 5!=10) # or напишет правда при хотя бы одном верном условии - нестрогий оператор
print(type(str(5))) # чтобы заменить тип данных после принт пишем тот тип данных, который хотим получить
# Здравствуйте!
# Почти все верно, так держать!
# Но один недочет в 4 задании.
# print(int(13.42) == int(42.13%1*100) or print(int(42.13)) == int(13.42%1*100+int(13.42//10)))
# Зачем вам тут print внутри print?
# Так делать не надо.
# int(13.42%1*100+int(13.42//10))
# Если у вас тут возникает погрешность, используйте round(число), она округляет число до целого или до количества чисел после запятой round(1.3) -> 1, round(1.9) -> 2
# С уважением, Владислав










