f2=open(r'C:\Users\lab365\Desktop\PythonTraining\bin\SSH_log_Sample.txt','r')
countfail=0
while True:
    line=f2.readline()
    if 'Failed password' in line:
        countfail+=1
    elif line=='':
        break
print('Failed attempts',countfail)
f2.seek(0)
while True:
    line=f2.readline()
    if 'sshd version' in line:
        listt=line.split()
        indexx=listt.index('version')
        print(listt[indexx+1])

    elif line=='':
        break
f2.seek(0)
import re
flag=0
while True:
    line=f2.readline()
    if 'private host key' in line:
        m = re.match('.*([a-z]{3}-[a-z]{3})\s+(.*?):.*',line)
        if m != None and flag==0:
            enc = m.group(2)
            flag+=1
            print(enc)

    elif line=='':
        break
f2.seek(0)
while True:
    line=f2.readline()
    if 'Accepted' in line:
        listt=line.split()
        indexx=listt.index('for')
        print(listt[indexx+1])
        indexx = listt.index('from')
        print(listt[indexx + 1])
        indexx = listt.index('port')
        print(listt[indexx + 1])

    elif line=='':
        break
f2.close()