#WAP to print intiger tilln which is divdisble by 2 and 3
num=int(input("Enter the number:"))
for i in range(1,num+1):
    if(i%2==0 and i%3==0):
        print(i)