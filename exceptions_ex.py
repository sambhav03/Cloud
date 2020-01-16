a=10
#b=0
try:
    r=a/b
    print('r=',r)
except:
    print('Some error')

try:
    r=a/b
    print('r=',r)
except ZeroDivisionError:
    print('In ZDE ')
except NameError as n:
    print('NE=',n)
except (KeyError,IndexError):
    print('KE or IE')
'''
In case of exceptions it is reverse of inheritance. Super class inherits exceptions
of sub class however vis a vis is not possible. 
'''
l=[]
try:
    print(l[1])
except Exception as e:
    print('e=',e)
    print('type=',type(e))

c=10
d=10
try:
    r=c/d
except:
    print('in except')
else:
    r=c/c
    print('in else')

try:
    r=c/0
except:
    print('In except')
finally:
    print('In finally')

'''
try-finally
try-except-finally
try-except-else-finally
'''
e=10
f=0
try:
    print('stmt-100')
    r=e/f
except ZeroDivisionError:
    print('From raise')

e=10
f=0
try:
    if f==0:
        raise ZeroDivisionError
    print('stmt-100')
    r=e/f
except ZeroDivisionError:
    print('From raise')

result='Test case failed'
try:
    assert 'Success' in result,'Some test failed'
    print('Test case success')
except AssertionError as ae:
    print('ae=',ae)

class MyError(Exception):
    def __init__(self,m):
        self.msg=m
    def  __str__(self):
        return 'ERROR DETAILS:'+self.msg
try:
    if 'success' not in result:
        raise MyError('Test Failed')
    else:
        print('Execution Success')
except MyError as me:
    print(me)