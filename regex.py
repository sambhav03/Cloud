import _sqlite3
con=_sqlite3.connect('mydb.sqlite3')
#import pymysql
#con=pymysql.connect(user='',password='',host='',port='',database='')
cur=con.cursor()
query='''create table if not exists 
logdata(
ip varchar(100),
date varchar(100),
pics varchar(100),
url varchar(100))'''
cur.execute(query)
#cur.execute('delete from logdata')
import urllib.request as u
myurl='https://www.jafsoft.com/searchengines/log_sample.html'
f=u.urlopen(myurl)
import re
for line in f:
    #print(line)
    line=line.decode()
    #print(type(line))
    #m=re.match('\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d')
    m = re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[a-zA-Z]{3}/\d{4}).*(?:GET|POST)\s+/(?:pics/(\w+\.\w+))?.*(http[s]?://\S+)</A>.*',line)
    if m!=None:
        ip=m.group(1)
        #print(line)
        date=m.group(2)
        image=m.group(3)
        if image==None:
            image='No Image'
        url=m.group(4)
        #print(ip,date,image,url)
        query=f"insert into logdata values('{ip}','{date}','{image}','{url}')"
        #print(query)
        cur.execute(query)
con.commit()
cur.execute('select * from logdata')
result=cur.fetchall()
#print(result)
import csv
f2=open('dbdump.csv','w',newline='')
wt=csv.writer(f2)
wt.writerow(['IP','DATE','PICS','URL'])
for eachrow in result:
    wt.writerow(eachrow)
f2.close()
f2=open('dbdump.csv')
rdr=csv.reader(f2)
csv_out=list(rdr)
print(csv_out)

import  pandas as pd
df1=pd.DataFrame([[10,20,30],[40,50,60]],index=['r1','r2'],columns=['c1','c2','c3'])
print(df1)

l1=list([[10,20,30],[40,50,60]])
print(l1)

df2=pd.DataFrame(result)
print(df2)
df2.to_csv('out3.csv',index=None,header=['IP','DATE','PICS','URL'])


cur.execute('select * from logdata')
df3=pd.DataFrame(cur)
df3.to_csv('out4.csv')
df3.to_excel('out5.xlsx')
df4=df3.T
df4.to_json('out6.json')

#\w-> word character [a-zA-Z0-9_]
#\W-> non word -> [^a-zA-Z0-9_]
#\s->space
#\S-> non space
#?: -> to not let it capture the group
#[.]->. only
#.->any char
#\d->digit
#\D-> non digit
#*-> 0 or more
#+->1 or more
#?->0 or 1 and also used to make * non greedy
#(abc)* -> abc string 0 or more times
#[abc] -> a or b or c
