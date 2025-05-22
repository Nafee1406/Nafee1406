location=[(12.9716,77.5946)]
latitude =float(input("enter your latitude :"))
longitude = float(input("Enter your longitude: "))
new_location = (latitude,longitude)
if location in new_location:
    print("Location already exist")
else:
    location.append(latitude)
    location.append(longitude)
    print(location)
    