#Convert distant given in feet and inches into meter and centimeter.
inche=int(input("Enter inche:"))
feet=int(input("Enter feet:"))
total_cm=(inche*2.54)+(feet*30.48)
meter=int(total_cm//100)
cm=total_cm%100
print(f"inche:{inche} feet:{feet} meter:{meter} cm:{cm}")