# tuple=(1,2,3,4)
# a = {1,2,3,4}
# list1=[1,2,3,4]

# b=set(list)
# print(type(b))
#
# test = {'login':'123',
#         'ivan': '143',
#         'max': '67'}
# print(test['login'])
# print(test.keys())
# # print(test.values())
# a = {1,2,3,4}
# b=a.keys()
# b = list(b)
# c=b[0]
# print(c)
# print(list(test.values())[2])
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

# #
# menu = {'pizza1':'100', 'pizza2':'200'}


import json
# with open('test.json','r') as f:
#     menu=json.load(f)

def load_menu():
    f = open('test.json', 'r')
    menu = json.load(f)
    f.close
    return(menu)

def save_menu(menu):
    f = open('test.json', 'w')
    json.dump(menu, f)
    f.close()
def add_pizza(name,price):
    menu= load_menu()
    if name in menu.keys():
        print('already there is')
    else:
        menu[name] = price
    save_menu(menu)
# print('before')
# print(menu)
# add_pizza('pizza3',100)
# print('after')
# print(menu)


def remove_pizza(name):
    menu = load_menu()
    if name in menu.keys():
        print('delete')
        del menu[name]
    else:
        print('no pizza')
    save_menu(menu)

# f = open(text.txt, w+)




# list_keys = list(menu.keys())
# list_keys_sting =',',join(list_keys)

def order_pizza():
    menu = load_menu()
    order=[]
    cost=0
    while True:
        q1=input('continue?')
        if q1=='no':
            break
        else:
            print('Our menu:')
            print(menu)
            pizza_name=input('Witch pizza?')
            if pizza_name in menu.keys():
                order.append(pizza_name)
                cost = cost + int(menu[pizza_name])
                print('Pizza added')
                print(cost)
    return (order, cost)
if __name__ == "__main__":
    while True:
        q3 =input('continue?')
        if q3 == 'yes':

            role = input('choose role:')
            if role == 'admin':
                q2 = input('add or delete?')
                if q2 == 'add':
                    name_pizza = input('name pizza:')
                    price_pizza = int(input('price:'))
                    add_pizza(name_pizza, price_pizza)
                elif q2 == 'remove':
                    name_pizza ==input('for deleting:'  )
                    remove_pizza(name_pizza)
            elif role == 'user':
                print(order_pizza())
            else:
                print('wrong')
        elif q3 == 'no':
            break
        else:
            print('mistake')


