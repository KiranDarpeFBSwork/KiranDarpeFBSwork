import random

correct_userid = "admin"
correct_password = "1234"
userid = input("Enter User ID: ")
password = input("Enter Password: ")
if userid == correct_userid and password == correct_password:
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)
    user_input = int(input("Enter the captcha shown above: "))
    if user_input == captcha:
        print("Success")
    else:
        print("Failed")
else:
    print("Invalid User ID or Password")

