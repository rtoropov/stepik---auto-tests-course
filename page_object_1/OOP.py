
class MyClass:
    a = 10             # атрибут класса

    def func(self):    # атрибут класса
        print("Hello")
# Атрибут, всё то, к чему можно обратиться через точку
print(MyClass.a) # MyClass.a - т.е. мы хотим взять атрибут "а" у объекта MyClass
print(MyClass.func)


x = MyClass() # создает новый объект x
print(type(x)) # <class '__main__.MyClass'>
print(type(MyClass)) # <class 'type'>


class Counter:
    pass

Counter
x = Counter() # instance Object  - экземпляр класса имеют тип нашего класса
x.count = 0  # есть имя count и оно ссылается на 0
x.count += 1