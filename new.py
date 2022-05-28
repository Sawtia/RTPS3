# a = [1,6,3,6,4,90,13]
#
# for j in range(len(a)-1):
#     for i in range(len(a)-1):
#         if a[i] > a[i+1]:
#             a[i], a[i+1] = a[i+1],a[i]
#
#
# print(a)
#
#
#

# a = [5,1,8,3,6,21,5,1]
# b = []
#
# def found(a):
#     min = a[0]
#     for i in range(1, len(a)):
#         if a[i] < min:
#             min = a[i]
#     return min
#
#
# def sort():
#     while len(a) != 0:
#         c = found(a)
#         b.append(c)
#         a.remove(c)
#     return b
#
# print(sort())



def factorial(n):
    return 1 if n == 0 else n*factorial(n-1)


print(factorial(3))




