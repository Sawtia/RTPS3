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



# a = [5,6,7,8,9,10,11]
#
# def recorsive_binary_search(a, find):
#     left_index = 0
#     right_index = len(a) - 1
#     median_index = (len(a)) // 2
#
#     if find < a[median_index]:
#         right_index = median_index
#         a = a[:right_index]
#         recorsive_binary_search(a,find)
#     elif find > a[median_index]:
#         left_index = median_index
#         a = a[left_index:]
#         recorsive_binary_search(a, find)
#     elif find == a[median_index]:
#         print(a[median_index])
#         print('find')
#
#
# try:
#     recorsive_binary_search(a=a, find=7)
# except:
#     print('no')
#
#
#
#



# a = [3,6,4,7,43,1]
#
# for j in range(len(a)-1):
#     for i in range(len(a)-1):
#         if a[i] > a[i+1]:
#             b = a[i]
#             a[i]=a[i+1]
#             a[i+1]=b
# print(a)


#
# a = [3,6,4,7,43,1]
# b = []
#
# def find(a):
#     min = a[0]
#     for i in range(1, len(a)):
#         if min > a[i]:
#             min = a[i]
#     return min
#
# while len(a) != 0:
#     c = find(a)
#     b.append(c)
#     a.remove(c)
#
# print(a)
# print(b)

unsorted_list = [3,6,4,7,43,1]
def merge_sort(unsorted_list):
    if len(unsorted_list) < 2:
        return unsorted_list

    medium = len(unsorted_list)//2
    left_list = merge_sort(unsorted_list[:medium])
    right_list = merge_sort(unsorted_list[medium:])
    return merge(left_list, right_list)



def merge(left_list, right_list):
    result = []
    i , j = 0, 0

    # while len(left_list) > i and len(right_list) > j:
    for _ in range(len(left_list+right_list)):
       if len(left_list) > i and len(right_list) > j:
        if left_list[i] < right_list[j]:
            result.append(left_list[i])
            i += 1
        else:
            result.append(right_list[j])
            j += 1
    while len(left_list) > i:
            result.append(left_list[i])
            i += 1
    while len(right_list) > j:
            result.append(right_list[j])
            j += 1

    return result

print(merge_sort(unsorted_list))





