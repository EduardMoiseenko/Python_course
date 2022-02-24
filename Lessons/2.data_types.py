# 2. Типы данных в python
a = None
print(a)
print(type(a))  # class NoneType - отсутствие данных

a = 1
print(a)
print(type(a))  # class int - целое число

a = 1.0
print(a)
print(type(a))  # class float - число с плавающей точкой

a = 1 + 1j
print(a)
print(type(a))  # class complex - комплексное число

a = 'Hello'
print(a)
print(type(a))  # class str - строка

a = [1, 1, 'a']
print(a)
print(type(a))  # class list - список

a = (1, 1, 'a')
print(a)
print(type(a))  # class tuple - кортеж

a = {1, 1, 'a'}
print(a)
print(type(a))  # class set - множество

a = {'a': 1, 'b': 2}
print(a)
print(type(a))  # class dict - словарь

a = True
print(a)
print(type(a))  # class bool - логичесикй булевый тип

print('_________________________________________________')
x = input("Vvedite chislo:")
r = int(x) + 5
print(r)
r2 = float(r) + 5
print(r2)
print(type(x))
print('_________________________________________________')

x = float(input('Vvedite chislo x:'))
y = float(input('Vvedite chislo y:'))
r3 = x + y
print(r3)
print('_________________________________________________')

x = float(input('Vvedite chislo x:'))
y = float(input('Vvedite chislo y:'))
r4 = x + y
print('Result '+ str(r4))