x=10
def f1():
    x=20 #enclosed scope
    def f2():
        x=30
        print('f2=',x)
    f2()
    print('f1=',x)
f1()
print('global=',x)

def f3():
    x=20 #enclosed scope
    def f4():
        nonlocal x # to access x of f3
        x=200
        print('f4 nonlocal',x)

    f4()
    print('f3=',x)
f3()
print('global=',x)

print(dir(__builtins__))