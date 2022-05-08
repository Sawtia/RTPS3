tuple=(1,2,3,4)
a = {1,2,3,4}
list=[1,2,3,4]

b=set(list)
print(type(b))

a = [1, 2, 8, 3, 21, 102, 55, 89]
max =0
for i in a:
    if i>max:
        max=i
print(max)


a = [1, 2, 8, 3, 21, 102, 55, 89]
i=0
max=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i+=1
print(max)

a=[1,1,2,3,5,8,13,21,21,55,89]
b=[]
for i in a:
       if i not in b:
           b.append(i)
print(b)


a=[3,2,5,3,7,3,6]
print(sorted(a))


a=[3,2,5,3,7,3,6]
i=0
while i<(len(a)-1):
    if a[i]>a[i+1]:
        k = a[i]
        a[i]=a[i+1]
        a[i+1]=k
    i+=1
    for i in a:
        if a[i]<a[i+1]:
            break
print(a)

