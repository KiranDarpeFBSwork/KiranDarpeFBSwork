gender=input("Enter gender:")
age=int(input("Enter age"))
if(gender=="mal")and(age>=21) or(gender=="fem")and(age>=18):
    print("eligible for marrage")
else:
    print("not eligible for marrage")