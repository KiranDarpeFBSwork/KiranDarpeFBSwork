#WAP to print the number which is divisable by 7 and multiple by 5
num=int(input("enter the number"))
for i in range (1,num+1):
    if(i%7==0 and i%5==0):
        print(i)
