a = 5
b = 5
print(id(a))
print(id(b))
# id будет одинаковым
a = a + 1
print(id(a))
# здесь ид изменится
text = 'save text'
text = text.replace(" ", "_")
print(text)

# оператор is
lst = [1,2]
lst2 = [1,2]
print(lst is lst2)
lst = lst2
print(lst is lst2)
print(id(lst == lst2))
