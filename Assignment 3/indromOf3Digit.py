num=int(input("Enter the number:"))
temp=num
a=temp//100
temp=num%100
b=temp//10
c=temp%10
number=((c*100)+(b*10)+a)
if(number==num):
    print("The number is palindrom")
else:
    print("Number is not palindrom")
