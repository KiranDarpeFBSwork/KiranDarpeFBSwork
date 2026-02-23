#revers 3 digit numbers
num=int(input("enter the num:"))
temp=num
n1=temp%10
temp=temp//10
n2=temp%10
n3=temp//10
print(f"reverse number is:{n1}{n2}{n3}")