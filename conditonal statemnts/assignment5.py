days=int(input("enter your number: "))
number = {1:"Monday",2:"Tuesday",3:"wednesday",4:"thursday",5:"friday",6:"saturday",7:"Sunday"}
if days in number:
    print(number[days])
else:
    print("invalid  input")