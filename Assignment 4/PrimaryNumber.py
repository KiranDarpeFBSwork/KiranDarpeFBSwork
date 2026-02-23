num=int(input("enter the number:"))
for i in range (2,(num//2)+1):
    if(num%i==0):
        print(f"{num}:is not prime number")
        break
else:
    print(f"{num}: is the prime number")