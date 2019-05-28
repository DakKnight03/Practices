while True:
    password = input("choose a password: ")
    if len(password) >= 8:
        print("done.")
        break
    else:
        print("password must have 8 or more characters.")

while True:
    enter_password = input("enter your password: ")
    if enter_password == password:
        print("loged in.")
        break
    else:
        print("password incorrect.")