 # Законы логики:

# Коммутативность: К
# A or B == B or A
# A and B == B and A

# Дистрибутивность: Д
# A and (B or C) == (A and B) or (A and C) #Скобки для наглядности, по законам лоогики строгий оператор выполняется первым,
 # нестрогий вторым. Поэтому скобки чисто для понимания.
# A or (B and C) == (A or B) and (A or C)

# Ассоциативность: А
# A or (B or C) == (A or B) or C == A or B or C
# A and (B and C) == (A and B) and C == A and B and C

# Теорема де Моргана: М
# not (A or B) == not A and not B
# not (A and B) == not A or not B
# not (A < B) == not A >= B
# not(not (A)) == A


def help_bool(letter=None):
    if letter == "К":
        return "A or B == B or A\nA and B == B and A"
    elif letter == "А":
        return "A or (B or C) == (A or B) or C == A or B or C\nA and (B and C) == (A and B) and C == A and B and C"
    elif letter == "Д":
        return "A and (B or C) == (A and B) or (A and C)\nA or (B and C) == (A or B) and (A or C)"
    elif letter == "М":
        return ("not (A or B) == not A and not B\nnot (A and B) == not A or not B"
                "\nnot (A < B) ==  not A >= B\nnot(not (A)) == A")
    else:
        return ("Неверный аргумент.\nПопробуйте:\nК - Коммунитивность,\nА - Ассоциативность,"
                "\nД - Дистрибутивность,\nМ - законы Де Моргана")
print(help_bool('А'))

def divider(a, b):
    return b and (a / b)**3 or "На ноль делить - нельзя!"
print(divider(10, 2))
print(divider(10, 0))

def num_sum(a):
    if isinstance(a, int) and not isinstance(a, bool):
        a_to_str = str(abs(a))
        s = 0
        for i in a_to_str:
            s += int(i)
        return s
    return "Это не целое число"
print(num_sum(55))
