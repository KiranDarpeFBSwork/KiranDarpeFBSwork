#program to input all sides of a triangle and check whether triangle is valid or not
side1=int(input("enter side1:"))
side2=int(input("enter side2:"))
side3=int(input("enter side3:"))

if((side1+side2) >side3 ):
    print("the triangle is valid")
else:
    print("triangle is invalid")
