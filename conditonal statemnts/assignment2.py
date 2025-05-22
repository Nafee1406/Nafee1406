correct_user_name = "shaiknafeesagmail.com"
correct_password= "sceret123"
user_name= input("enter your user name :")
password = input("Enter your password: ")
if user_name == correct_user_name:
    if password == correct_password:
        print("login successfull")
else:
    print("invalid login credentials")