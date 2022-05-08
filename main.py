# tuple=(1,2,3,4)
# a = {1,2,3,4}
# list=[1,2,3,4]
#
# b=set(list)
# print(type(b))
#
# test = {'login':'123',
#         'ivan': '143',
#         'max': '67'}
# # print(test['login'])
# # print(test.keys())
# # print(test.values())
# a=test.keys()
# b = list(a)
# c=b[0]
# print(c)
# # print(list(test.values())[2])
#
# def logpas():
#     login = input('login:')
#     password = input('password:')
#     return login,password
#
# def login():
#     login,password= logpas()
#     if login in users.keys():
#         if users[login] == password:
#             print('ok')
#             print(secret)
#
# def registration():
#     login,password= logpas()
#     if login in users.keys():
#         print('busy')
#     else:
#         users[login] = password
#         print('susses')
#
# def delete():
#     delete = input('введите:')
#     if delete in users.keys():
#         password = input('password:')
#         if users[delete] == password:
#             del users[delete]
#             print('ok')
#
# def error():
#     print('mistake')
#
#
#
# users={'admin':'123'}
# secret='42'
# while True:
#     q1 = input('Вход или регистрация или удаление?')
#     if q1 == 'Вход':
#         login()
#         break
#     elif q1 == 'Регистрация':
#         registration()
#     elif q1 == 'удаление':
#         delete()
#     else:
#         error()
#


# def summ_two_numb(num1,num2):
#     summ=num1+num2
#     return summ
# summ=summ_two_numb(1,2)
# print(summ)
#


menu = {'pizza1':'100',
        'pizza2':'200'}

def add_pizza(name,price):
    if name in menu.keys():
        print('already there is')
    else:
        menu[name] = price
print('before')
print(menu)
add_pizza('pizza3',100)
print('after')
print(menu)


def remove_pizza(name):
    if name in menu.keys()
        print('delete')
        del menu[name]
    else:
        print('no pizza')


def order


