total_amount =int(input("enter your total purchased amount :"))
if total_amount >= 100:
    discount = int(total_amount*(10/100))
    print("you got 10% discount")
    print(f"your final price is {discount}")
elif total_amount >= 50:
    discount_1= int(total_amount*(5/100))
    print("you got 5% discount")
    print(f"your final price is {discount_1}")
else:
    print("you got no discount")