a='PERSON'
print(a)
b="PERSON's"
print(b)
c='''PERSON'S HEIGHT XYZ" '''
print(c)
d="""PERSON"""
print(d)
s1='Hello'
s2='py'
s3=s1+s2
s4=s1*10
print(s3,s4)
line='-'*40
print(line)
e='PERSON\'S'
print(e)
f=r'C:\newfolder\test.py' #prefixed by r to represent raw string
print(f)
g='WEL   COME'
print(g)
print(len(g)) #length of any collection
print(g[1]) #get a particular character
print(g[0:7])
print(g[0:])#till end
print(g[:7])#from begining to 6th index
h=g[:]
print(id(g))
print(id(h))
h="HI"
print(id(h))

#STEP
print(g[1:7:1])
print(g[1:7:2])

#REVERSE
print(g[::-1])
print(g[6:1:-2])

#-VE INDEX
print(g[-1:-10:-1])
print(g[len(g)-4:])
print(g[-4:])

#str class
i=10
j=str(i)
k=str('python')

r1=g.startswith('WEL')
print('r1=',r1)

r2=g.endswith('COME')
print('r2=',r2)

r3=g.islower()
r4=g.upper()
print(r3,r4,sep='\n')

l='abc'
r7=l.isalpha()
r8=l.isdigit()
n='abc123'
r9=n.isalnum()
print(r7,r8,r9,sep=' ')
r10=n[-3:].isdigit()
print(r10)

r11=g.count('E')
print('r11=',r11)

r12=g.index('E')
r13=g.find('E')
print('r12=',r12,' r13=',r13)

r14=g.index('E',3)#find E after 3rd index
r15=g.index('E',3,10)#find E between 3rd and 10th index
print('r14=',r14,' r15=',r15)
#r15=g.find('E',3)

r16=g.rindex('E')
print('r16=',r16)

p=' wel come '
r17=p.strip()#remove spaces on both the sides and not in between
#Similarly we have rstrip,lstrip
print(r17)

q='[wel[come][]'
r20=q.strip(']w[e')
print (r20)
r21=q.strip('w[')
r22=q.strip('][e')
print(r21,r22)

r23=g.replace('E','e')
print (r23)

r24=g.split()
print(r24)

r25=g.split('E')
print(r25)

x=10
y=20
z=x+y
r26='add of x and y is z'
r27='add of {} and {} is {}'.format(x,y,z)
print(r27)

r28='add of {1} and {0} is {2}'.format(x,y,z)
print(r28)

#python version>3.5

r29=f'add of {x} and {y} is {z}'
print(r29)

r30='-'.join(g)
print(r30)

r31='XYZ'.join(r24)
print(r31)

