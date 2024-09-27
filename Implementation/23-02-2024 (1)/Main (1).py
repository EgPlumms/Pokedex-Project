import requests
import pandas as pd 
import matplotlib
import hashlib
import json


#Pokemans = input("Enter A Pokemon\n")

#Pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{Pokemans}") #Accesses The URL For The Pokemons Information 

#print(Pokemon.status_code) #Tells The API Status (If Its Working Or Not)

#Pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/'+Pokemans) #Accesses The Url And Find Specific Pokemon User Asks For (Stores It As Variable Pokemon)
#Info = json.loads(Pokemon.text) #Turns Pokemon Text Into Json, Can Be Used Like A Dictionary
#print(Info)

def Login(): #login to existing account
    print("Please Provide")
    username = input("Username: ") #Gets username To Search For 
    with open("usernames.txt", 'r') as f: #opens the usernames text file
        info = f.read().splitlines() #reads the files info (turns the info in the file Into A Variable)
        if username in info: #searches file for the username Entered 
            password = input("Password: ") #Gets Password To Search For 
            with open("passwords.txt", 'r') as f: #Opens The Password Text File
                info1 = f.read().splitlines() #Reads The Files Info (turns the info in the file Into A Variable)
                if password in info1: #Looks to see if entered Username Is In The File
                    print(f"Welcome Back {username}!\n") #If The Password And Username Are Correct It Welcomes The User Back
                    logged_menu() #Opens Menu 
                print("Your password is incorrect. Please try again.") # If Password Is Incorrect This Shows Up 
                Login()
        else:
            print("Your username is either incorrect or nonexistent. You can either try again or create a new account.") #If Username Is Wrong Or Doesn't Exist This Appears 
            Retry = input("Would You Like To Try Again?\n")
            if Retry.lower() == 'yes':
                Login()
            else:
                menu()
  

def create(): #create an account
    print("Please Provide")
    username = input("Username: ") # Creates Username 
    with open("usernames.txt", 'r') as f: #Opens Text File 
        info = f.read() # Turn Info In The File Into A Variable And Reads The File
        if username in info: #Searcges If Username Already Exists
            print("Username unavailable. Please Try Again.") #If Username Exists Already This Appears
            create() #Sends User Back To The Start Of This Function
        password = input("Password: ") #Creates Password 
        with open("passwords.txt", 'r') as f: #Opens Password Text File 
            info1 = f.read() # Turns Info In The File Into A Variable 
        with open("usernames.txt", 'w') as f: #Opens Username Text File 
            info = f'{info}\n{username}' #If Username Isn't Taken Puts It Into The Usernames Text File 
            f.write(info) #Writes The Username In
        with open("passwords.txt", 'w') as f: #Opens Password Text File 
            info1 = f"{info1}\n{password}" # Saves Password Into Password Text File 
            f.write(info1) #Writes Password Into File 
        print("Congratulations! You have successfully created an account. You may now login in.") #Tells User They Can Go Login 
    login = input("Would You Like To Login?\n") #Gives User Choice To Go To Login Function
    if login.lower() == 'yes': #Sends Them To The Login Function
        Login()
    else: #Sends Them Back To The Menu 
        menu()

def add(): #adds a pokemon to the team
    print("BBBBBBBBBB\n")
    logged_menu()
    #if  pokiman == True:
   #     print("Is "pokemans,"The Pokemon You Want To Add?")
    #else:
    #    print("What Pokemon Would You Like To Add To Your Team?")

def find(): #find a pokemon in the system 
    Pokemans = input("What Pokemon Would You Like To Find?\n") #Allows User To Input Pokemon They Want To Find.
    Pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/'+Pokemans) #Accesses The Url And Find Specific Pokemon User Asks For (Stores It As Variable Pokemon)
    PokeInfo = json.loads(Pokemon.text) #Turns Pokemon Text Into Json, Can Be Used Like A Dictionary
    start_over = input("Would You Like To Look At A Different Pokemon?\n") #Look At Different Pokemon If They Wish To. 
    if start_over.lower() == 'yes': #Sends The User Back To The Start Of This Function.
        find()
    else:
        Back = input("Would You Like To Go Back To The Menu?\n") #Allows User To Return To The Menu 
        if Back.lower() == 'yes':
            menu()
        else: #Exits Program If User Is Finished 
            print("Thanks For Viewing The Pokedex!")
            exit()

def L_find() : #Finds Pokemon When Logged In 
    pokemans = input("What Pokemon Would You Like To Find?\n") #Allows User To Input Pokemon They Want To Find.
    T_add = input("Would You Like To Add This Pokemon To Your Team?\n") #User Can Input If They Want To Add This To Their Team Or Not.
    if T_add.lower() == 'yes':
        add()
    elif T_add.lower() == 'no':
        start_over = input("Would You Like To Look At A Different Pokemon?\n") #Look At Different Pokemon If They Wish To. 
    if start_over.lower() == 'yes': #Sends The User Back To The Start Of This Function.
        find()
    else:
        Go_Back = input("Would You Like To Go Back To The Menu?\n") #Allows User To Return To Menu 
        if Go_Back.lower() == 'yes':
            logged_menu()
        else: #Exits Program If User Is Done 
            print("Thanks For Viewing The Pokedex!")
            exit()
    
def team(): #lets you view your team
    print("AHHHHHHH")
    exit()

def logged_menu(): #menu Once Logged In
    print("""▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
▐______     _            _           ▌
▐| ___ \   | |          | |          ▌
▐| |_/ /__ | | _____  __| | _____  __▌
▐|  __/ _ \| |/ / _ \/ _` |/ _ \ \/ /▌
▐| | | (_) |   <  __/ (_| |  __/>  < ▌
▐\_|  \___/|_|\_\___|\__,_|\___/_/\_\▌
▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌""")
    L_ch = input("What Would You Like To Do?\n1.Find A Pokemon\n2.Add Pokemon To Team\n3.View Team\n4.Logout\n5.Exit\n") #Allows User To Choose What They Want To Do.
    if L_ch == '1' : #Sends Them To The Pokedex Function
        pokiman = True
        L_find()
    elif L_ch == '2' : #Sends To The Add Function
        add()
    elif L_ch == '3' : #Sends To The Team Function
        team()
    elif L_ch == '4' : #Logs User Out               
        print("You've Logged Out.")
        menu()
    elif L_ch =='5' : #Exits Program 
        print("Have A Good Day!")
        exit()
    else:
        print("This Option Doens't Exist.") #Tells User The Option They Entered Is Wrong And Gets The Menu Back Up To Try Again.
        Menu_Attempts = input("Do You Wish To Try Again?\n") #Allows User To Try To Choose An Actual Option
        if Menu_Attempts == 'yes': #Sends The User Back To The Menu If They Put Yes
            logged_menu()
        else: #Exits Program If User Doesn't Want To Try Again
            print("Thanks For Visiting The Pokedex. Have A Good Day!")
            exit()


def menu():
    print("""▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
▐______     _            _           ▌
▐| ___ \   | |          | |          ▌
▐| |_/ /__ | | _____  __| | _____  __▌
▐|  __/ _ \| |/ / _ \/ _` |/ _ \ \/ /▌
▐| | | (_) |   <  __/ (_| |  __/>  < ▌
▐\_|  \___/|_|\_\___|\__,_|\___/_/\_\▌
▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌""")
    ch = input("What Would You Like To Do?\n1.Signup\n2.Login\n3.Find A Pokemon\n4.Exit\n") #Allows User To Choose What They Want To Do.
    if ch == '1' : #Sends Them To The User Creation Function
        create()
    elif ch == '2' : #Sends Them To The Login Function
        Login()
    elif ch == '3' : #Sends Them To The Pokedex Function 
        pokiman = True
        find()
    elif ch == '4' :
        print("Have A Good Day!") #Exits Program
        exit() 
    else:
        print("This Option Doens't Exist.") #Tells User The Option They Entered Is Wrong And Gets The Menu Back Up To Try Again.
        Menu_Attempts = input("Do You Wish To Try Again?\n") #Allows User To Try To Choose An Actual Option
        if Menu_Attempts == 'yes': #Sends Back To Menu If User Puts Yes 
            menu()
        else: #Exits Program If User Doesn't Want To Try Again    
            print("Thanks For Visiting The Pokedex. Have A Good Day!") 
            exit()
     

menu() 

