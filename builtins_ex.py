#map
l=[100,200,300,400]
def sub(i):
    return i-50
r1=map(sub,l)
print(list(r1))

#filter
def filt(j):
    return j>100
r2=filter(filt,l)
print(list(r2))

#reduce
import functools as ft
def red(p,q):
    return p+q
r3=ft.reduce(red,l)
m=['w','e','l']
r4=ft.reduce(red,m)
print(r3,r4,sep='\n')

#lambda functions
# no name, single line functions
r5=map(lambda i:i-10,l)
r6=filter(lambda  j : j>100,l)
r7=ft.reduce(lambda p,q: p+q,l)
print(list(r5),list(r6),r7)

f=lambda a,b:a+b
r8=f(10,20)
print(r8)

l=[(lambda i:i*i)(a) for a in range(10)]
print('L=',l)

keys=['A','B']
values=[10,20]
d={k:(lambda i:i+i)(v) for k,v in zip(keys,values)}
print(d)

