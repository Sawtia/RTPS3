#
#
# def factorial(n):
#     return 1 if n == 0 else n*factorial(n-1)
#
# print(factorial(5))
#
#
#
# class Classic:
#
#     def __enter__(self):
#         print('enter')
#         return 1
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exit')
#
# with Classic() as number:
#      print(number)



a = [5,6,7,8,9,10,11]

def recorsive_binary_search(a, find):
    left_index = 0
    right_index = len(a) - 1
    median_index = (len(a)) // 2

    if find < a[median_index]:
        right_index = median_index
        a = a[:right_index]
        recorsive_binary_search(a,find)
    elif find > a[median_index]:
        left_index = median_index
        a = a[left_index:]
        recorsive_binary_search(a, find)
    elif find == a[median_index]:
        print(a[median_index])
        print('find')


try:
    recorsive_binary_search(a=a, find=7)
except:
    print('no')




