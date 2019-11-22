# name = "Roma"
# num = float(input("Enter first num:"))
# num2 = int(input("Enter second num :"))
# print(num + num2)
# age = 10
# age += 10
# print(age)
#
# if age > 11:
#     print("\nPassed")
# elif age == 0:
#     print()
#
# for row in range(1, 10):
#     if row == 2:
#         assert 2 == 2
#     else:
#         print(row," number != 2", '\n')
#
#
# i = 100
# while i > 10:
#     print((i))
#     i -=10

# lis = [23, 45, 6.45, "s", ["h", "g"]]
# lis[1] = 25 # заменили 45 на 25
# lis.append(5)
# lis.remove(25)
# lis.insert(1, 9) # заменяем по 1 индексу число на 9
# print(lis.index(23)) # выводит индекс по значению
# print(lis)
#

#
# a = [i for i in range(1, 15)]
# print(a)
# print(a[::2]) # шаг
# print(a[::-1]) # заркальный список
# print(a[2:-2])  # начало:конец
#
# print(a[1:-1:2]) # от до последнего с шагом 2

class Person1:
    name = "Ivan"
    age = 10
    def set(self, name, age):
        self.name = name
        self.age = age
vlad = Person1()
vlad.set("Vlad", 25)
print(vlad.name, vlad.age)

# Наследование, т.е. мы создаем новый класс, который наследует все функции и методы другого класса

class Student(Person1): # наследование
    course = 1

Igor = Student()
Igor.set("Igor", 19)
print(Igor.name)
Igor.course =3
print(Igor.name, Igor.age, Igor.course)
print('2' + '2' ) # 22
print(2 + 2 ) # 4

# Инкапсуляция - защита данных, ограничение доступа к данным

