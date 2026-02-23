#WAP to print perfect number
num=int(input("enter the number:"))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum+=i
if(num==sum):
    print(f"{sum} is perfect number")
else:
    print("number is not perfect")
        
