f1 = open('out1.txt', 'w')
#write mode,creates file if not existing,overwrites the file
x=10
s='python\n'
x=str(x)+'\n'
f1.write(x)
#write method takes only string as an argument
f1.write(s)
f1.flush()
# Second Way to write to a file

l=[x,s]
f1.writelines(l)
f1.close()
#READING
f2=open('out1.txt','r')
#no creation of file in read mode
r1=f2.read()
print(r1)

f2.seek(0)
r2=f2.read()
print(r2)

f2.seek(0)
r3=f2.readline()
print(r3)

f2.seek(0)
while True:
    line=f2.readline()
    if line=='':
        break
    else:
        print(line)

print('-------------------------------')
f2.seek(0)
r4=f2.readlines() #reads the entire file and return the contents in a list
print(r4)
r5=[]
for l in r4:
    l=l.strip()
    r5.append(l)
print('r5=',r5)

f2.seek(0)
for x in f2:
    print('line=',x)

f2.seek(0)
r6=list(f2)
print(r6)

l1=['h1','h2']
l2=['ip1','ip2']
d1=dict(zip(l1,l2))
print(d1)

e=enumerate(l1)
print(list(e))

f2.seek(0)
d2=dict(enumerate(f2))
print(d2)
f2.close()

f3=open('out1.txt','a')
f4=open('out2.csv','a')
print(20,'java',sep='\n',file=f3,flush=True)
print(20,'java',sep=',',file=f4)
f3.close()
f4.close()

#File MOdes
"""
w-write only
r-read only
a-append only
w+ wr
r+ rw
a+ ar

wb-write only
rb-read only
ab-append only
w+b wr
r+b rw
a+b ar
"""


