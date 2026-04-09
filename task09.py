users = [
  {"id": 1, "active": True},
  {"id": 2, "active": True},
]

for user in users:
    user.update({"active": False})

print(users)