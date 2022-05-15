#
# class Animal:
#
#     def __init__(self, name, health):
#         self.name = name
#         self. health = health
#     def make_noise(self):
#         pass
#     def __inner_method(self):
#         print('!!!')
#
#     def get_name(self):
#         self.inner_method()
#         return self.name
# class Cat(Animal):
#     def make_noise(self):
#         print('meow')
#     pass
# class Dogs(Animal):
#     def make_noise(self):
#         print('gav')
#
#
# cat1 = Cat(name='bars',health=100)
# dog1 = Cat(name='sharik',health=200)
#
#
#
# # animal = Animal('bars', 100)
# # animal.__inner_method()
# MONTHS = 12
# class Salary:
#
#     def __init__(self, pay):
#         self.pay = pay
#     def get_year_salary(self):
#         return self.pay * MONTHS
# class Employee:
#
#     def __init__(self, pay, bonus):
#         self.bonus = bonus
#         self.salary = Salary(pay)
#     def annual_salary(self):
#         return self.salary.get_year_salary()+self.bonus
#
# employee = Employee(pay=23232, bonus=3232)
# annual_salary =employee.annual_salary()
# print(annual_salary)
#
#
#



# class Point:
#      def __enter__(self):
#          print('2432')
#      def __init__(self,x,y):
#          self.x = x
#          self.y = y
#
#
#
#      def __exit__(self, exc_type, exc_val, exc_tb):
#          print('dfsf')
#
#      def distanse(self):
#          return (self.x ** 2 + self.y ** 2) ** (1/2)
# point = Point(x=5,y=7)
# print(point.distanse())
# with Point() as f:
#     print('dsf')


# try:
#     print(100/0)
#     m= int('string')
#
# except (ValueError, ZeroDivisionError) as e:
#     print(e)
# a = int(input('number'))
#
# if a == 0:
#     try:
#         raise Exception
#     except:
#         print('3')

# finally:
#     a = 5
#     b = 2
#     print('000')
#     print(a)

# class MyOwnException(Exception):
#     pass
# try:
#     raise MyOwnException
# except MyOwnException:
#     print('sfasd')
from main import factorial


class Uu:
    def __init__(self, n):
        self.n = n
    def factorial(self):
        if self.n == 0:
            return 1
        return self.n*factorial(self.n-1)
    def __enter__(self):
        print('enter')
        return self.factorial()
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

with Uu() as number:
    print(number)



