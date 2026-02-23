#odd number from 1 to n
n=int(input("enter the number"))
for num in range (1,n+1):
    if(num%2!=0):
        print(num,end=" ")