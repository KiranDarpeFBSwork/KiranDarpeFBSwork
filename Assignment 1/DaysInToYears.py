days=int(input("enter days :- "))
years=days//365
days=days%365
weeks=days//7
days=days%7
print(f"print years:- {years} weeks:- {weeks} days:- {days}")