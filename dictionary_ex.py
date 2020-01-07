d={'course':'python','due':10,'loc':'blr'}
print(d)
print(d['course'])

#Dictionaries are unordered

#Add or Update
d['course']=['c++','java']
print(d)

e=d.copy()

#Removing
r1=d.pop('course')
print ('pop=',r1,d)

del d['due']
print(d)

r2=d.popitem()
print(r2)

#Other Methods

k=e.keys()
print(k)

v=e.values()
print(v)

i=e.items()
print(i)

