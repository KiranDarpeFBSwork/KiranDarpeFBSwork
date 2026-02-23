#WAPto print armstrong number
num=int(input("enter the number"))
temp=num
sum=0
order=len(str(num))
while(temp>0):
    digit=temp%10
    sum+=digit**order
    temp//=10
if(num==sum):
    print(f"{sum}: is armstrong number")