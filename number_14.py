password_lookup = {}

a = 5

for i in range(1, a + 1):
    key = {}
    user_name = input("enter username: ")
    password = input("enter a password")
    password_lookup[user_name] = password
print(password_lookup)    