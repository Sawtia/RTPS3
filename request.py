import requests
# #
# menu = requests.get('http://127.0.0.1:5000/pizzeria/menu')
# print(menu.json())
#
# menu = requests.get('http://127.0.0.1:5000/pizzeria/menu', params={'pizza_name': 'pizza1'})
#
#
# if menu.status_code != 404:
#     print(menu.json())
# else:
#     print('NO EXIST')
#
#
# r = requests.post('http://127.0.0.1:5000/pizzeria/menu/pizza', data={'name': 'clone', 'cost': 600})
# print(r.status_code)

# r = requests.delete('http://127.0.0.1:5000/pizzeria/menu/pizza', params={'pizza_name': 'clone'})
# print(r.status_code)
#
# menu = requests.get('http://127.0.0.1:5000/pizzeria/menu')
# print(menu.json())


cost = requests.post('http://127.0.0.1:5000/pizzeria/order', data={'order': ['pizza1', 'pizza0']})
print(cost.json())

