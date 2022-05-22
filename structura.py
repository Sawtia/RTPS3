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
#
# queue = Queue([1,2,3])
# queue.add(7)
#
# print(queue.get())
#
# print(queue.queue_data)

#
# class Stack:
#     def __init__(self, data):
#         self.queue_data = data
#     def add(self, element):
#         self.queue_data.append(element)
#
#     def get(self):
#         return self.queue_data.pop(-1)
#
# stack = Stack([1,2,3])
# stack.add(7)
#
#
#
# print(stack.queue_data)
# print(stack.get())
# print(stack.queue_data)

class Queue:
    def __init__(self, data):
        self.queue_data = data

    def add(self, element):
        self.queue_data.append(element)

    def get(self):
        return self.queue_data.pop(0)

queue = Queue([])
graph = {
    'A':['B','E'],
    'B':['D','C','A'],
    'C':['D','B','K'],
    'D':['B','C'],
    'E':['A','K'],
    'K':['C','E']
}

def width_search(graph, start,find):
    visited = []
    visited.append(start)
    queue.add(start)
    while queue.queue_data:
        top = queue.get()
        tops = graph[top]
        for i in tops:
            if i == find:
                break
            if i not in visited:
                visited.append(i)
                queue.add(i)
    return visited


print(width_search(graph, 'A','D'))
