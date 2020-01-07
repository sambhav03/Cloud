a=0
while a<10:
    print('a=',a)
    a+=1

#-----------------------------------
s='python'
b=0
while b<len(s):
    print('b=',s[b])
    b+=1

#---------------------------------------
l=['Rahul','P','ADR','Bangalore','Aditya','B','ADR','Jaipur']
i=0
while i<len(l):
    if l[i]=='ADR':
        i+=1
        print(l[i])
    i+=1

#---------------------------------------
j=0
while j<len(l):
    if l[j].startswith('A'):
        print('Found')
        break
    else:
        j+=1
else:
    print('not found')

#---------------------------------------

k=0
while k<len(l):
    if not l[k].startswith('A'):
        k+=1
        continue
    print(l[k])
    k+=1
    print('last statement of while')

#--------------------------------------
cart=[]
while True:
    i=input('Enter item:')
    cart.append(i)
    ch=input('Quit(y/n?:')
    if ch=='y':
        print('Cart',cart)
        break
    continue
