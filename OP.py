# def factorial(n):
#     if n == 0:
#         return 1
#     return n*factorial(n-1)

# def factorial(n):
#     return 1 if n == 0 else n*factorial(n-1)
#
# print(factorial(2))
# import pickle
#
#
import pickle


class Student:

    def __init__(self, tired, progress,):
        self.tired = tired
        self.progress = progress

    def study(self):
        if self.tired < 85:
            self.tired += 15
        else:
            self.tired = 100

        self.progress += 10

    def relax(self):
        if self.tired > 5:
            self.tired -= 5
        else:
            self.tired = 0

    def is_done(self):
        if self.progress >= 100:
            print('ready')
        else:
            print('not ready')

    def demotivated(self):
        return self.tired > 100


student_ilya = Student(tired=15, progress=10)
student_dima = Student(tired=5, progress=20)

print(student_ilya.tired)
print(student_ilya.tired)
student_ilya.study()
student_ilya.study()
print(student_ilya.tired)
print(student_ilya.progress)

f = open('text.pickle', 'w')
pickle.dump(student_ilya, f)
f.close()

print('?????????????')

print(student_dima.tired)
print(student_dima.tired)
student_dima.study()
print(student_dima.tired)
print(student_dima.progress)

f = open('text.pickle', 'w')
pickle.dump(student_dima, f)
f.close()

