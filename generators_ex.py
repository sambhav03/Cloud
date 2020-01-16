t1=(10,20,30)
t2=(i for i in range(10))
print(t1,t2,sep='\n')
print('list(t2)=',list(t2))

L=[1,2,3,4]
def squares(m):
    res=[]
    for j in m:
        r=j*j
        res.append(r)
    return res
r1=squares(L)
for a in r1:
    print(a)


def gen_squares(n):
    for k in n:
        yield k*k
    for l in n:
        yield  l*l*l
r2=gen_squares(L)
for b in r2:
    print(b)
print('r1:',r1)
print('r2:',list(r2))