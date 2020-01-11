s='abc123XYZ456ABC'
line='*'*40
r1=s.split('123')
print(r1)
print(line)
import re
r2=re.split('\d\d\d',s)
print(r2)
print(line)
r3=s.find('123')
if r3!=-1:
    print('sub string found')
print(line)
r4=re.search('\d\d',s)
if r4!=None:
    print('digit found')
print(line)
f=open(r'C:\Users\lab365\Desktop\PythonTraining\log\serverlog.txt')
data=f.read()
ips=re.findall('\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d',data)
print('IPS:',ips)
print(line)
