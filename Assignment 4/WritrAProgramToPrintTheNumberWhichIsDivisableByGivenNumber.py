# WAP to print the number which is divisable to given number
num=int(input("enter the number"))
num1=int(input("enter the number "))
count=0
for i in range(1,num):
    if(i%num1==0):
        print(i)

