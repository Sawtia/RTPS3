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




# class Queue:
#     def __init__(self, data):
#         self.queue_data = data
#
#     def add(self, element):
#         self.queue_data.append(element)
#
#     def get(self):
#         return self.queue_data.pop(0)
#
# queue = Queue([])
# graph = {
#     'A':['B','E'],
#     'B':['D','C','A'],
#     'C':['D','B','K'],
#     'D':['B','C'],
#     'E':['A','K'],
#     'K':['C','E']
#
# }
#
# def width_search(graph, start,find):
#     visited = []
#     visited.append(start)
#     queue.add(start)
#     while queue.queue_data:
#         top = queue.get()
#         tops = graph[top]
#         for i in tops:
#             if i == find:
#                 break
#             if i not in visited:
#                 visited.append(i)
#                 queue.add(i)
#
#     for i in visited:
#         if find in graph[i] and start in graph[i]:
#             path = i
#     return path
#
#
# print(width_search(graph, 'A','K'))

# from abc import abstractmethod
#
# class Singleton:
#     @abstractmethod
#     def func(self):
#         pass
#
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super().__new__(cls)
#         return cls.instance
#
# s = Singleton()
# print(s)






a = [3,5,6,3,67,43]
for j in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            b = a[i]
            a[i] = a[i+1]
            a[i+1] = b
print(a)





