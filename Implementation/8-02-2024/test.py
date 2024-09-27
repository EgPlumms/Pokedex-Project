import hashlib

def signup():
    username = input("Enter Username: ")
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt", "a+") as f:
             f.write(username + "\n")
             f.write(hash1)
        f.close()
        print("You have registered successfully!")
    else:
        print("Password is not same as above! \n")

def login():
    username = input("Enter Username: ")
    pwd = input("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_username, stored_pwd = f.read().split("\n")
    f.close()
    if username == stored_username and auth_hash == stored_pwd:
         print("Logged in Successfully!")
    else:
         print("Login failed! \n")
while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")