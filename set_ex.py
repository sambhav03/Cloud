#Unordered Collection
#No Index
#No Key
#Mutable
#hold only immutable objects
#Umique Values only

s={10,10,20,'python'}
print(s)

s.add(30)
s.add(30)
print(s)

r1=s.remove(10)
print('removed=',s,r1)

r2=s.pop()
print(s,r2)

s1={10,20,30,40}
s2={30,40,50,60}
s3=s1.union(s2)
print(s3)

s4=s1.intersection(s2)
print('Intersection=',s4)

s5=s1.difference(s2)
s6=s1-s2
print(s5,s6,sep='\n')

