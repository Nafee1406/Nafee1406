secret = 123
user = int(input("enter your guess :"))
if user > secret:
    print("Too high")
elif user < secret:
    print("Too low")
elif user == secret:
    print("correct")