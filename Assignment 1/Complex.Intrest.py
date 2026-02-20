principle=int(input("enter principle:- "))
rate=int(input("enter rate:- "))
time=int(input("enter time:- "))
complex_intrest=principle*(1+rate/100)**time-principle
print(f"complex intrest is:- {complex_intrest}")