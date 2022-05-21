a = [1,2,3,4,5,6,7,45,58,57657,435453453]

# def  function(a, b):
#     left = 0
#     right = (len(a)) - 1
#     median = (len(a))//2
#     while True :
#         if b < a[median]:
#             right = median
#             a = a[:right]
#             function(a ,b)
#         elif b > a[median]:
#             left = median
#             a = a[left:]
#             function(a , b)
#
#     print('find')
#     print(b)
#
#
# function(a, 7)
# find = 435453453
#
# left = 0
# right = len(a) - 1
# counter = 0
# while left <= right:
#     counter += 1
#     median = ((left+right) // 2)
#     if a[median]== find:
#         print(a[median])
#         break
#     elif find < a[median]:
#         right = median - 1
#     elif find > a[median]:
#         left = median + 1
# print(counter)


# a = [3,1,5,2,43,3,17,2]
#
# for j in range(len(a)-1):
#     for i in range(len(a)-1-j):
#         if a[i] > a[i + 1]:
#             b = a[i]
#             a[i] = a[i + 1]
#             a[i + 1] = b
#
# print(a)

# a = [2,1,6,3,17,1,5,2]
# b = []
# c = a[0]
# def find(a):
#     c = a[0]
#     for i in range(len(a)):
#         if c > a[i]:
#             c = a[i]
#     return c
# while (len(a)) != 0:
#     c = find(a)
#     b.append(c)
#     a.remove(c)
#
#
#
#
# print(a)
# print(b)



a = [2,1,6,3,17,1,5,2]
sorted(a)
print(a)






