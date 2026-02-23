num=int(input("enter the number :"))
temp=num
sum=0
while(temp>0):
    tem=temp%10
    fact=1
    for i in range (1,tem+1):
        fact*=i
    sum+=fact
    temp//=10
if(num==sum):
    print(f"{sum}: is strong number")
else:
    print("number is not strong number")