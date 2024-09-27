import requests
import pandas as pd 
import matplotlib 
import hashlib


#Pokemans = input("Enter A Pokemon\n")

#Pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{Pokemans}").json() #Accesses The URL For The Pokemons Information 

# print(Pokemon.status_code) #Tells The API Status (If Its Working Or Not)

def Login(): #login to existing account
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
         menu()


def create(): #create an account
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
        menu()
    


def find(): #find a pokemon in the system 
    pokemans = input("What Pokemon Would You Like To Find?\n")
    add = input("Would You Like To Add This Pokemon To Your Team?\n")
    if add == 'yes':
        add()
    else:
        print("Thanks For Viewing The Pokedex!")
    


def add(): #adds a pokemon to the team
    print("BBBBBBBBBB")
    #if  pokiman == True:
   #     print("Is "pokemans,"The Pokemon You Want To Add?")
    #else:
    #    print("What Pokemon Would You Like To Add To Your Team?")


def team(): #lets you view your team
    print("AHHHHHHH")


def menu():
    print("""▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
▐______     _            _           ▌
▐| ___ \   | |          | |          ▌
▐| |_/ /__ | | _____  __| | _____  __▌
▐|  __/ _ \| |/ / _ \/ _` |/ _ \ \/ /▌
▐| | | (_) |   <  __/ (_| |  __/>  < ▌
▐\_|  \___/|_|\_\___|\__,_|\___/_/\_\▌
▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌""")
    ch = input("What Would You Like To Do?\n 1.Signup\n 2.Login\n 3.Find A Pokemon\n 4.Add Pokemon To Team\n 5.View Team\n")
    if ch == '1' :
        create()
    elif ch == '2' :
        Login()
    elif ch == '3' :
        pokiman = True
        find()
    elif ch == '4' :
        add()
    elif ch == '5' :
        team()
    else:
        print("This Option Doens't Exist.")
        menu()
     

menu() 

