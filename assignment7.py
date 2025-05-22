categories={
    "clothes":["shirt","jeans"],
    "Electronics":["phone","charger"]
}
name = input("enter your category :")
if name in categories:
    print(categories[name])
else:
    print("Invalid category")