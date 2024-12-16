password_lookup ={}

while True:
    a = input("enter username: ").lower()
    if a == "z":
        break
    b = input("enter password: ")
    password_lookup[a] = b
print(password_lookup)    
        