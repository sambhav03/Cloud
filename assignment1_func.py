'''
This is a program to find a value in the merged list
 and print the immediate highest val to the inputted value
 from the list.
>>> L=[10,20,30]
>>> searchin(L,40)
[10, 20, 30]
Found at Index: 1
>>>
'''

list1=[1,3,5,16,8]
list2=[6,5,9,4,13,12]
temp=list1+list2
temp2=set(temp)
temp3=list(temp2)
def searchin(temp3,a):
    print(temp3)
    if a in temp3:
        print('Found at Index:',temp3.index(a))
    else:
        inn=len(temp3)
        i=0
        while(i<inn):
            if temp3[i]!=a and temp3[i]<a:
                i+=1
                continue
            else:
                val=temp3.index(temp3[i])
                print('Next Highest Value:',temp3[i],' Index:',temp3.index(temp3[i]))
                break
        if temp3[inn-1]<a:
            print("Unable to process")
def main():
    while True:
        a = int(input("Enter value to search:"))
        searchin(temp3,a)
        inp=input("Want to continue(y/n):")
        if inp=='y':
            continue
        break
if __name__=='__main__':
    # main()
    import doctest
    doctest.testmod()
