import assignment1_func as af
list1=[1,3,5,16,8]
list2=[6,5,9,4,13,12]
temp=list1+list2
temp2=set(temp)
temp3=list(temp2)
while True:
    a=int(input("Enter Number to be searched:"))
    af.searchin(temp3,a)
    inp = input("Want to continue(y/n):")
    if inp == 'y':
        continue
    break

