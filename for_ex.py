s = 'python'
for a in s:
    print('a=', a)

b = 'java'
l = [10, 20, 30]
for b in l:
    print('b=', b)
print('Now a and b=', a, b)
# for loop variables have full scope even after the for loop ends

d = {'a': 10, 'b': 20}
for k in d:
    print('k=', k)
line = '-' * 40
print(line)
for k in d.keys():
    print('key=', k, 'value', d[k])
print(line)

for v in d.values():
    print('v=', v)
print(line)

for i in d.items():
    print('item=', i)
    print('item key=', i[0], 'item value', i[1])
    print(line)

for i, j in d.items():
    print(i, j)
    print(line)

hosts = ['h1', 'h2', 'h3']
ips = ['ip1', 'ip2']
z = zip(hosts, ips)
print(z)
#print(list(z))

for h, i in (z):
    print(h, i)

#for(i=2;i<10;i+2)
r1=range(10)
r2=range(1,10)
r3=range(1,10,2)
print(list(r1),list(r2),list(r3),sep='\n')
print(line)

for i in range(2,10,2):
    print('i=',i)

for h in range(0,len(hosts)):
    print(hosts[h])
print(line)

for h in hosts[::2]:
    print(h)

comp=['COMP','DEL1','SAP','DEL2']
for c in comp:
    if c.startswith('DEL'):
        print(c)
        break

f=0
for c in comp:
    if c.startswith('DEL'):
        f=1
        print('FOUND')
        break
if f==0:
    print('Not found')
print(line)

#FOR-ELSE

for c in comp:
    if c.startswith('DEL'):
        print('FOUND')
        break

else:
    print('Not found')
print(line)

for i in comp:
    if not i.startswith('DEL'):
        continue
    if i.startswith('DEL'):
        print('Some logic')
    print('Last statement of for')

