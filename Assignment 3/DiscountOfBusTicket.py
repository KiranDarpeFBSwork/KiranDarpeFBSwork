#discount on bus ticket
age1=int(input("enter the age1:"))
age2=int(input("enter the age2:"))
age3=int(input("enter the age3:"))
age4=int(input("enter the age4:"))
age5=int(input("enter the age5:"))
Ticket=int(input("Enter the ticket:"))
a=Ticket*0.3
c=Ticket*0.5
if(age1<12):
    print(f"ticket of children is:{Ticket-a}")
elif(age1>59):
    print(f"Ticket of senior citizen:{Ticket-c}")
else:
    print(f"Ticket travels:{Ticket}")
    # age of second person
if(age2<12):
    print(f"ticket of children is:{Ticket-a}")
elif(age2>59):
    print(f"Ticket of senior citizen:{Ticket-c}")
else:
    print(f"Ticket travels:{Ticket}")
    #age of third person
if(age3<12):
    print(f"ticket of children is:{Ticket-a}")
elif(age3>59):
    print(f"Ticket of senior citizen:{Ticket-c}")
else:
    print(f"Ticket travels:{Ticket}")
    #age of fourth person
if(age4<12):
    print(f"ticket of children is:{Ticket-a}")
elif(age4>59):
    print(f"Ticket of senior citizen:{Ticket-c}")
else:
    print(f"Ticket travels:{Ticket}")
    #age of 5 person
if(age5<12):
    print(f"ticket of children is:{Ticket-a}")
elif(age5>59):
    print(f"Ticket of senior citizen:{Ticket-c}")
else:
    print(f"Ticket travels:{Ticket}")