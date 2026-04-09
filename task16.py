person = {"name": "Ali", "age": 25, "city": "Tashkent"}

ask = input("kalit : ")

if ask in person:
    person.pop(ask)
    print(person)
else:
    print("bunday kalit yoq")