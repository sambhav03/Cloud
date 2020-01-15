#multiple objects
#Inheritance
#operator overloading
class Account1:
    def addUser(self,n):  #instance method
        self.name=n    #instance variable
    def viewUser(self):
        return self.name
    bank='ICICI' #it will be stored in class Object and is more like static and is a class variable
    @classmethod
    def bankrules(cls,area):    #class method
        return 'Bank Rules:'+area
    @staticmethod
    def bankinfo():  #Zero Arguments static method
        return 'Bank Info'
    def __init__(self): #like a constructor
        print('SB LOGIC HERE')
cust1=Account1()
cust2=Account1()
cust1.addUser('Sambhav')
name=cust1.viewUser()
print(name)
print(cust1.bank)
print(Account1.bank)
print(Account1.bankinfo())
#local,enclosed,global,class.instance
#instance methods i.e. methods using self
#name is an instance variable
#Account i.e. the class name is a class object however cust1 and cust2 are instance objects
#Class object is only one
print(cust1.bankrules('Pune'))
class Account2(Account1):
    def addaadhar(self,a):
        self.aadhar=a
    def viewaadhar(self):
        return self.aadhar
    def viewUser(self):
        return 'Welcome '+self.name
    def __init__(self):
        print('CA LOGIC HERE')
        super().__init__()
        Account1.__init__(self)
cust3=Account2()
cust3.addUser('XYZ')
print(cust3.viewUser())
print(Account2.bank)
print(Account2.bankrules('Delhi'))
print(cust3.addaadhar('A1'))
print(cust3.viewaadhar())
class RBI:
    def viewrules(self):
        return 'RBI RULES'
class Account3(Account2,RBI):
    pass
cust4=Account3()
print(cust4.viewrules())
cust4.addUser('ABC')

class Govt:
    def viewrules(self):
        return 'Govt rules'
class Account4(Account3,Govt):
    pass
cust5=Account4()
print(cust5.viewrules())
print(Govt.viewrules(cust5))
'''
class Account5(Account3):
    def __init__(self):
        self.gov=Govt()
cust6=Account5()
print(cust6.viewrules())
print(cust6.gov.viewrules())
'''
class Account6:
    def __init__(self,n):
        self.name=n
    def __add__(self, x):
        return self.name+x.name
    def __str__(self):
        return self.name
    def __len__(self):
        return len(self.name)
    def __iter__(self):
        self.count=0
        return self
    def __next__(self):
        c=self.count
        if c<len(self.name):
            self.count+=1
            return self.name[c]
        else:
            raise StopIteration
from abc import ABC,abstractmethod
class Account(ABC):
    def adduser(self,a):
        self.name=a
    @abstractmethod
    def viewuser(self):
       pass

cust7=Account6('abc')
cust8=Account6('xyz')
result=cust7+cust8
print('result',result)
print(cust7)
print('length',len(cust7))
for i in cust7:
    print('i=',i)

#a=Account()
class myaccount(Account):
    def viewuser(self):
        return 'hello'+self.name
mac=myaccount()
mac.adduser('b')
print(mac.viewuser())