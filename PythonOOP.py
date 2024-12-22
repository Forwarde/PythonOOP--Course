#
# ctrl + /
# class Person:
#     def __init__(self,name):
#         self.name=name
#
#     def display(self):
#         print(self.name)
#
# n=Person('Person') # создание экземпляра
# p=n.__dict__
# print(p)

# class Person:
#     def hello(self):
#         print("Hello world!")
#     @staticmethod # нужно написать декоратор чтобы вызвать функц goodbye
#     def goodbye():
#         print("Goodbue")
#
#
# p=Person()
# p.goodbye()


# Name mangling
class Person:
    def func(self):
        __name = 'Nurim'
        # вы получаете пустой словарь {} при вызове a.__dict__, потому что переменная __name в вашем коде является приватной
        # переменной, но она не была присвоена как атрибут экземпляра класса.
        # Пояснение:
        # Приватные переменные в Python:
        #
        # Переменные, начинающиеся с двойного подчеркивания (__), считаются приватными. Python использует механизм name mangling,
        # чтобы предотвратить случайный доступ к таким переменным.
        # В вашем коде __name не был привязан к экземпляру через self. Вместо этого он является
        # локальной переменной внутри метода func и существует только в его области видимости.


a = Person()
a.func()
p = a.__dict__
print("First name mangling: {p}")  # {}

# 2 name mangling
# class Persons:
#     def func1(self):
#         self.__name='Nurims'
#
#
# s=Persons()
# s.func1()
# n=s.__dict__
# print("Second name mangling: ",n)
