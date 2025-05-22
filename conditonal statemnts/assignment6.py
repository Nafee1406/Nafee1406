cart = [{"id": 1,"name":"shirt","quantity":1}]
product_id = int(input("enter your produdct id :"))
product_name = input("Enter product name:")
user_requirement ={product_id,product_name}
if user_requirement in cart:
    print("item already in cart")
else:
    cart.append(product_name)
    print(cart)