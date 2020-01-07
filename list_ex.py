#LISTS

l1=list([10,20,30])
l2=[10,12.5,'python',['a','b']]

print(l2)
print(l2[1])
print(l2[2][1])#this will print 'y' from 'python'
print(l2[-1:1:-1])

#Add an element in the list

l2.append(200)
print('appended=',l2)

l2.insert(2,300) #inserts at index 2
print(l2)

l3=[10,20]
l4=['a','b']
l5=l3+l4
l6=l3*10
print(l5,l6,sep='\n')

l3.extend(l4)
print('Extended is:',l3)

#To remove from the list

r1=l5.pop()
print(r1,l5,sep='\n')

r2=l5.pop(2)#remove at 2nd index
print(r2,l5,sep='\n')

#pop() function returns the popped value but remove doesnt.
r3=l5.remove(20)
print(r3,l5,sep='\n')

del l5[0]
print('after deletion',l5)

#Updation in the List

print (l3)
l3[1]='java'
print(l3)

#Some Other methods

l6=[10,30,20]
l6.sort() #ascending
print('sorted asc:',l6)
l7=['z','a','b']
l7.sort(reverse=True)
print(l7)

l8=[10,'a',20,'b']
l8.reverse()
print(l8)

l8.clear()
print(l8)

#Copy
l=[10,['a','b']]
M=l #reference copy
N=l.copy() # Shallow copy

#copy module library->copy(),deepcopy()

import copy
p=copy.deepcopy(l)
print (p)

print(id(l[0]),id(p[0]))
print(id(l[1]),id(p[1]))

#Purpose of Reference Copy

cp=copy.deepcopy
q=cp(l)

