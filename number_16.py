import random
import string


members_table = {'rajmalla10@gmail.com':'month',
                 'luffyraj10@gmail.com' : 'name',
                 'hero10@gmail.com':'hero'}


def generate_password():
    num_pass = 8
    random_string = string.ascii_letters + string.digits
    temp_pass = "".join(random.choice(random_string) for _ in range(num_pass))
    return temp_pass

def reset_password(email,hint):
    while True:
        if email in members_table:
            if members_table[email] == hint:
                new_password = generate_password()
                print(f'New password is : {new_password}')
                return new_password
            else:
                print('Hint doesnt exit on email')
        else:
            break
                    
email = input("Enter your Email: ") 
hint = input("enter your hint: ")                
result = reset_password(email, hint)                               
print(result)

