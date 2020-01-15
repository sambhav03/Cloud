d={'ROM':'ROM DESCRIPTION','HDD':'HDD DESCRIPTION','FDD':'FDD DESCRIPTION',
   'RAM':'RAM DESCRIPTION','CPU':'CPU DESCRIPTION'}
a=input("enter the device:")
flag=0
l=[]
for i in d.items():
    if i[0]==a:
        print(i[1])
        flag-=1
for i in d.items():
    if (flag==0 or flag>0) and i[0].startswith(a[0]):
       l.append(i[1])
       #print(i[1])
       flag+=1
l.sort()
length=len(l)
if length>0:
   print(l)
if flag==0:
   print("No matches")


