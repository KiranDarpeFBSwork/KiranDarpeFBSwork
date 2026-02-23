# factorian of any number
num=int(input("enter the number:"))
count=1
for i in range (1,num+1):
    count*=i
print(f"factorial of {num} is:{count}")