# # import main
# # print(main.menu)
# menu = {'pizza1':'100', 'pizza2':'200'}
# import json
# # from main import menu
# f= open('test.json','w')
# a= json.dump(menu,f)
# f.close()
# # print(type(a))
# # b = json.loads(a)
# # print(type(b))
# f= open('test.json','r')
# a= json.load(f)
# print(type(a))
# f.close()


import sys
sys.setrecursionlimit(10000)
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

print(factorial(2130))
#
# a=5
# b=4
#
#
# c= 6 if a>b else 5
# print(c)