temp = int(input("enter your temperature:"))
a = input("specify temperature :" )
if a =="celsius":
    print(f"{(temp*9/5)+32}fahrenheit")
else:
    print(f"{(temp-32)*5/9}celsius")
    25