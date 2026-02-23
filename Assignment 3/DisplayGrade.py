subject1=int(input("Enter the subject1 markes:"))
subject2=int(input("Enter the subject2 markes:"))
subject3=int(input("Enter the subject3 markes:"))
subject4=int(input("Enter the subject4 markes:"))
subject5=int(input("Enter the subject5 markes:"))
markes=subject1+subject2+subject3+subject4+subject5
persentage=(markes/500)*100
if(persentage>35):
    if(persentage>75):
        if(persentage>90):
            print("first class")
        else:
            print("second class")
    else:
        print("pass")
else:
    print("fail")