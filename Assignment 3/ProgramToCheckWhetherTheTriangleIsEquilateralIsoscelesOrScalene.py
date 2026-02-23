#program to check whether the triangle is equilateral, isosceles or scalene triangle.

s1=int(input("enter the s1:"))
s2=int(input("enter the s2:"))
s3=int(input("enter the s3:"))
#equilateral
if((s1==s2) and (s1==s3) and (s3==s2)):
    print(" trangle is equliatral")
#isoscalen
elif((s1==s2) or (s1==s3)or(s2==s3)):
    print("trangle is isosceles")
else:
    print("triangle is scalen")