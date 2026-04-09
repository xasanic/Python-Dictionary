car = {"brand": "Chevrolet", "model": "Cobalt", "color": "white"}

kalit = input("Kalit nomini kiriting: ")

if kalit in car:
    print(car[kalit])
else:
    print("Topilmadi")