import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import *
import csv
import requests
import json

class Pokedex(tk.Tk):
    def __init__(self):
        super().__init__()
        self.is_dark_mode = False
        self.geometry('1920x1080')

        #Light And Dark Mode
        self.light_mode = {
            'bg': 'white',
            'fg': 'black',
            'entry_bg': '#eee',
            'entry_fg': 'black',
            'button_bg': '#ddd',
            'button_fg': 'black'
        }

        self.dark_mode = {
            'bg': '#333',
            'fg': 'white',
            'entry_bg': '#555',
            'entry_fg': 'white',
            'button_bg': '#444',
            'button_fg': 'white'
        }

        #Welcome To Pokedex Label/Position
        self.PokedexW_Label = tk.Label(self, text="Welcome To The Pokedex!", font=("Arial",26))
        self.PokedexW_Label.grid(row=2, column=1, sticky=EW)

        #Button To Get Up The Pokedex Page/Position
        self.Pokedex_Button = tk.Button(self, text="Pokedex", height=8, width=10, command=self.Pokedex)
        self.Pokedex_Button.grid(row=0, column=0)

        #Button To Get Up Pokemon Team Page/Position
        self.Team_Button = tk.Button(self, text="Team", height=8, width=10, command=self.Team)
        self.Team_Button.grid(row=1,column=0)

        #Button To Get Up Login Page/Position
        self.Log_Button = tk.Button(self, text="Login", height=8, width=10, command=self.login)
        self.Log_Button.grid(row=2, column=0)

        #Dark Mode Button/Position
        self.DarkM_Button = tk.Button(self, text="Toggle\n Dark Mode", height=8, width=10, command=self.toggle_theme)
        self.DarkM_Button.grid(row=3, column=0)

        #Exit Button/Position
        self.Exit_Button = tk.Button(self, text="Exit Program", height=8, width=10, command=self.Exit_Program)
        self.Exit_Button.grid(row=4, column=0)

        #Makes Sure The Label Is On The Right Colour Mode
        if self.is_dark_mode:
            self.apply_theme(self.dark_mode) 
        else:
            self.apply_theme(self.light_mode)

    #Admin Console
    def Admin_Console(self):

        self.Admin_Mode = {
            'bg': '#333',
            'fg': 'white',
            'entry_bg': '#568259',
            'entry_fg': 'white',
            'button_bg': '#568259',
            'button_fg': 'white'
        }
    
        self.apply_theme(self.Admin_Mode)

    #Logged Out Menu
    def menu(self):

        #Button To Get Up The Pokedex Page/Position
        self.Pokedex_Button = tk.Button(self, text="Pokedex", height=8, width=10, command=self.Pokedex)
        self.Pokedex_Button.grid(row=0, column=0)

        #Button To Get Up Pokemon Team Page/Position
        self.Team_Button = tk.Button(self, text="Team", height=8, width=10, command=self.Team)
        self.Team_Button.grid(row=1,column=0)

        #Button To Get Up Login Page/Position
        self.Log_Button = tk.Button(self, text="Login", height=8, width=10, command=self.login)
        self.Log_Button.grid(row=2, column=0)

        #Dark Mode Button/Position
        self.DarkM_Button = tk.Button(self, text="Toggle\n Dark Mode", height=8, width=10, command=self.toggle_theme)
        self.DarkM_Button.grid(row=3, column=0)

        #Exit Button/Position
        self.Exit_Button = tk.Button(self, text="Exit Program", height=8, width=10, command=self.Exit_Program)
        self.Exit_Button.grid(row=4, column=0)

        #Makes Sure The Label Is On The Right Colour Mode
        if self.is_dark_mode:
            self.apply_theme(self.dark_mode) 
        else:
            self.apply_theme(self.light_mode)

        #Admin Colours :)
        #self.admin_button = tk.Button(self, text="Admin", command=self.Admin_Console)
        #self.admin_button.grid(row=7, column=3, columnspan=2, pady=10)

    #Logged Out Team
    def Team(self):
        self.clear_window()
        self.menu()
        self.Team_Label = tk.Label(self, text="Not Logged In No Team Available", font=('Arial',21),)
        self.Team_Label.grid(row=2,column=1,) 
        
        #Makes Sure The Label Is On The Right Colour Mode
        if self.is_dark_mode:
            self.apply_theme(self.dark_mode) 
        else:
            self.apply_theme(self.light_mode)
        
    #Logged In Team
    def TeamL(self):
        self.clear_window()
        self.Logged_Menu()

        #Your Team Label/Position
        self.UserTeam_Label = tk.Label(self, text="                Your Team", font=("Arial",20))
        self.UserTeam_Label.grid(row=0,column=2,)

        #Pokemon 1 Label/Position
        self.Pokemon1_Label = tk.Label(self, text="Pokemon 1")
        self.Pokemon1_Label.grid(row=1,column=1)

        #Change Slot 1 Button/position
        self.Pokemon1_Switch_Button = tk.Button(self, text="Switch")
        self.Pokemon1_Switch_Button.grid(row=3,column=1)

        #Pokemon 2 Label/Position
        self.Pokemon1_Label = tk.Label(self, text="Pokemon 2")
        self.Pokemon1_Label.grid(row=1,column=2)

        #Change Slot 2 Button/position
        self.Pokemon1_Switch_Button = tk.Button(self, text="Switch")
        self.Pokemon1_Switch_Button.grid(row=3,column=2)
        
        #Pokemon 3 Label/Position
        self.Pokemon3_Label = tk.Label(self, text="Pokemon 3")
        self.Pokemon3_Label.grid(row=1,column=3)

        #Change Slot 3 Button/position
        self.Pokemon3_Switch_Button = tk.Button(self, text="Switch")
        self.Pokemon3_Switch_Button.grid(row=3,column=3)

        #Pokemon 4 Label/Position
        self.Pokemon4_Label = tk.Label(self, text="Pokemon 4")
        self.Pokemon4_Label.grid(row=1,column=4)

        #Change Slot 4 Button/position
        self.Pokemon4_Switch_Button = tk.Button(self, text="Switch")
        self.Pokemon4_Switch_Button.grid(row=3,column=4)

        #Pokemon 5 Label/Position
        self.Pokemon4_Label = tk.Label(self, text="Pokemon 5")
        self.Pokemon4_Label.grid(row=1,column=5)

        #Change Slot 5 Button/position
        self.Pokemon5_Switch_Button = tk.Button(self, text="Switch")
        self.Pokemon5_Switch_Button.grid(row=3,column=5)

        #Pokemon 6 Label/Position
        self.Pokemon4_Label = tk.Label(self, text="Pokemon 6")
        self.Pokemon4_Label.grid(row=1,column=6)

        #Change Slot 6 Button/position
        self.Pokemon6_Switch_Button = tk.Button(self, text="Switch")
        self.Pokemon6_Switch_Button.grid(row=3,column=6)

        #Makes Sure The Label Is On The Right Colour Mode
        if self.is_dark_mode:
            self.apply_theme(self.dark_mode) 
        else:
            self.apply_theme(self.light_mode)

    #Logged Out pokedex
    def Pokedex(self):
        self.clear_window()
        self.menu()

        #Search Pokemon Label/Position
        self.PokedexS_Label = tk.Label(self, text="Search A Pokemon")
        self.PokedexS_Label.grid(row=0, column=1)

        #Pokemon Entry/Position
        self.PokedexS_Entry = tk.Entry(self)
        self.PokedexS_Entry.grid(row=0,column=2)

        #Search Pokemon Buttton/Position
        self.PokedexS_Button = tk.Button(self, text="Search")
        self.PokedexS_Button.grid(row=0, column=3)

        #Makes Sure The Label Is On The Right Colour Mode
        if self.is_dark_mode:
            self.apply_theme(self.dark_mode) 
        else:
            self.apply_theme(self.light_mode)


    #Logged In pokedex
    def PokedexL(self):
        self.clear_window()
        self.Logged_Menu()

        #Search Pokemon Label/Position
        self.PokedexS_Label = tk.Label(self, text="Search A Pokemon")
        self.PokedexS_Label.grid(row=0, column=1)

        #Pokemon Entry/Position
        self.PokedexS_Entry = tk.Entry(self)
        self.PokedexS_Entry.grid(row=0,column=2)

        #Search Pokemon Buttton/Position
        self.PokedexS_Button = tk.Button(self, text="Search", command=self.pokeL)
        self.PokedexS_Button.grid(row=0, column=3)

        #Makes Sure The Label Is On The Right Colour Mode
        if self.is_dark_mode:
            self.apply_theme(self.dark_mode) 
        else:
            self.apply_theme(self.light_mode)

    def pokeL(self):
        pokemans = self.PokedexS_Entry.get()
        pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/'+pokemans) #Accesses The Url And Find Specific pokemon User Asks For (Stores It As Variable selfmon)
        Info = json.loads(pokemon.text) #Turns pokemon Text Into Json, Can Be Used Like A Dictionary
        self.pokemon_label = tk.Label(self, text=Info)

    #Logged In Menu
    def Logged_Menu(self):
        self.clear_window()

        #Button To Get Up The Pokedex Page/Position
        self.selfdex_Button = tk.Button(self, text="Pokedex", height=8, width=10, command=self.PokedexL)
        self.selfdex_Button.grid(row=0, column=0)

        #Button To Get Up Pokemon Team Page/Position
        self.Team_Button = tk.Button(self, text="Team", height=8, width=10, command=self.TeamL)
        self.Team_Button.grid(row=1,column=0)

        #Button To Logout
        self.Logout_Button = tk.Button(self, text="Logout", height=8, width=10, command=self.__init__)
        self.Logout_Button.grid(row=2, column=0)

        #Dark Mode Button/Position
        self.DarkM_Button = tk.Button(self, text="Toggle\n Dark Mode", height=8, width=10, command=self.toggle_theme)
        self.DarkM_Button.grid(row=3, column=0)

        #Exit Button/Position
        self.Exit_Button = tk.Button(self, text="Exit Program", height=8, width=10, command=self.Exit_Program)
        self.Exit_Button.grid(row=4, column=0)

        #Makes Sure The Label Is On The Right Colour Mode
        if self.is_dark_mode:
            self.apply_theme(self.dark_mode) 
        else:
            self.apply_theme(self.light_mode)

    #Login Widgets
    def login(self):
        self.clear_window()
        self.menu()
        self.user = "User" #temporary Until Register System Is Set Up 
        self.admin = "admin"
        
        #Username Label/Positon
        self.Username_Label = tk.Label(self, text="Username") 
        self.Username_Label.grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
        
        #Username Entry/Position
        self.Username_Entry = tk.Entry(self)
        self.Username_Entry.grid(row=0, column=3,sticky=tk.E, padx=5, pady=5)
        
        #Password Label/Position
        self.Password_Label = tk.Label(self, text="Password")
        self.Password_Label.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
        
        #Password Entry/Position
        self.Password_Entry = tk.Entry(self, show="*")
        self.Password_Entry.grid(row=1, column=3,sticky=tk.E, padx=5, pady=5)
        
        #Register Button/Position
        self.register_Button = tk.Button(self, text="Sign Up", command=self.register)
        self.register_Button.grid(row=2, column=3, sticky=tk.E, padx=5, pady=5)

        #Login Button/Position
        self.Login_Button = tk.Button(self, text="Login", command=self.Log)
        self.Login_Button.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)

        #Makes Sure The Label Is On The Right Colour Mode
        if self.is_dark_mode:
            self.apply_theme(self.dark_mode) 
        else:
            self.apply_theme(self.light_mode)
        
    #Log In Code
    def Log(self):
        username = self.Username_Entry.get()
        password = self.Password_Entry.get()
        user = self.user
        admin = self.admin

        with open("UserData.csv", mode="r") as f: #opens the csv file
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                if row == [username,password,user]:
                    self.Login_Label = tk.Label(self, text="Logged In Successfully!\n "f"Welcome Back {username}!\n")
                    self.Login_Label.grid(row=4, column=3)
                    #Makes Sure The Label Is On The Right Colour Mode
                    if self.is_dark_mode:
                        self.apply_theme(self.dark_mode) 
                    else:
                        self.apply_theme(self.light_mode)
                    self.after(1000, self.Logged_Menu)
                    return True
        self.LoginNo_Label = tk.Label(self, text="Login Failed! Please Try Again Or Sign Up.")
        self.LoginNo_Label.grid(row=4, column=3,)
        self.after(2000, self.clear_label)
                    
                    
        #Makes Sure The Label Is On The Right Colour Mode
        if self.is_dark_mode:
            self.apply_theme(self.dark_mode) 
        else:
            self.apply_theme(self.light_mode)

    #Register Widgets
    def register(self):
        self.clear_window()
        self.menu()
        self.user = "User"
        
        #Username Label/Positon
        self.Username_Label = tk.Label(self, text="Username") 
        self.Username_Label.grid(row=0, column=2)
        
        #Username Entry/Position
        self.Username_Entry = tk.Entry(self)
        self.Username_Entry.grid(row=0, column=3)
        
        #Password Label/Position
        self.Password_Label = tk.Label(self, text="Password")
        self.Password_Label.grid(row=1, column=2)
        
        #Password Entry/Position
        self.Password_Entry = tk.Entry(self)
        self.Password_Entry.grid(row=1, column=3)

        #Re-Enter Password Label/Position
        self.PasswordR_Label = tk.Label(self, text="Re-Enter Password")
        self.PasswordR_Label.grid(row=2, column=2)

        #Re-Enter Password Entry/Position
        self.PasswordR_Entry = tk.Entry(self)
        self.PasswordR_Entry.grid(row=2,column=3)

        #Register Button/Position
        self.reg_Button = tk.Button(self, text="Register", command=self.reg)
        self.reg_Button.grid(row=3, column=2)

        #Button To Get Up Login Page/Position
        self.Log_Button = tk.Button(self, text="Login", command=self.login)
        self.Log_Button.grid(row=3, column=3)

        #Makes Sure The Label Is On The Right Colour Mode
        if self.is_dark_mode:
            self.apply_theme(self.dark_mode) 
        else:
            self.apply_theme(self.light_mode)
    
    #Register
    def reg(self):
        username = self.Username_Entry.get()
        password = self.Password_Entry.get()
        password_2 = self.PasswordR_Entry.get()
        user = self.user

        with open("UserData.csv",mode="a", newline="") as f:
            writer = csv.writer(f,delimiter=",")
            if password == password_2: #Makes Sure The Password Entered Is Correct
                writer.writerow([username,password,user]) #Enters Users Username And Password Into Csv File
                self.Register_Label = tk.Label(self, text="New User Registered!")
                self.Register_Label.grid(row=4, column=3)
                self.after(2000, self.clear_label)
            else:
                self.RegisterNo_Label = tk.Label(self, text="Registration Failed Please Try Again!")
                self.RegisterNo_Label.grid(row=4, column=3)
                self.after(2000,self.clear_window)
        #Makes Sure The Label Is On The Right Colour Mode
        if self.is_dark_mode:
            self.apply_theme(self.dark_mode) 
        else:
            self.apply_theme(self.light_mode)
        
    def backing(self):
        self.Img = tk.PhotoImage(file="images/Pokeball.png")
        self.ImgLabel = ttk.Label(self, image=self.Img)

    #Clears Window Of Everything
    def clear_window(self):
        for widgets in self.winfo_children():  
            widgets.destroy()

    def clear_label(self):
        self.clear = tk.Label(self, text="                                                                                                                                       ") # clears text
        self.clear.grid(row=4, column=1, columnspan=2)

        if self.is_dark_mode:
            self.apply_theme(self.dark_mode) 
        else:
            self.apply_theme(self.light_mode)

    #Exits Program
    def Exit_Program(self):
        exit()

    #Applies Themes To The Different Components
    def apply_theme(self, theme):
        self.config(bg=theme['bg'])

        for widget in self.winfo_children():
            widget_type = widget.winfo_class()

            if widget_type == 'Label': #Applies Themes To Label Components
                widget.config(bg=theme['bg'], fg=theme['fg'])
            elif widget_type =='Entry': #Applues Theme To Entry Components
                widget.config(bg=theme['entry_bg'], fg=theme['entry_fg'], insertbackground=theme['fg'])
            elif widget_type == 'Button': #Applies Theme To Button Components
                widget.config(bg=theme['button_bg'], fg=theme['button_fg'])

    #Toggles Theme
    def toggle_theme(self):
        if self.is_dark_mode:
            self.apply_theme(self.light_mode)
        else:
            self.apply_theme(self.dark_mode)

        self.is_dark_mode = not self.is_dark_mode

#Login Code
def login(self):
    username = self.Username_Entry.get()
    password = self.Password_Entry.get()

    with open("usernames.txt", 'r') as f: #opens the usernames text file
        info = f.read().splitlines() #reads the files info (turns the info in the file Into A Variable)
        if username in info: #searches file for the username Entered
            with open("passwords.txt", 'r') as f: #Opens The Password Text File
                info1 = f.read().splitlines() #Reads The Files Info (turns the info in the file Into A Variable)
                if password in info1:
                    self.Login_Label = tk.Label(self, text="Logged In Successfully!\n "f"Welcome Back {username}!\n")
                    self.Login_Label.grid(row=4, column=1, columnspan=2)
                    self.menu()
                self.LoginNo_Label = tk.Label(self, text="Login Failed! Please Try Again.")
                self.LoginNo_Label.grid(row=4, column=1, columnspan=2)
                self.login()
                    
                    #Makes Sure The Label Is On The Right Colour Mode
                if self.is_dark_mode:
                    self.apply_theme(self.dark_mode) 
                else:
                    self.apply_theme(self.light_mode)
        else:
            self.NuhUh_Label = tk.Label(self, text="Your Username Is Either Incorrect Or Nonexistent. You Can Either Try Again Or Create A New Account.")
            self.NuhUh_Label.grid(row=4, column=1, columnspan=2) 
            self.Retry_Entry = tk.Entry(self)
            self.Retry_Entry.grid(row=4, column=1, columnspan=2)
            Retry = self.Retry_Entry.get()
            if Retry.lower() == 'yes':
                self.login()
            else:
                self.menu()
    
    #Makes Sure The Label Is On The Right Colour Mode
        if self.is_dark_mode:
            self.apply_theme(self.dark_mode) 
        else:
            self.apply_theme(self.light_mode)
    
#Admin Console
def Admin_Console(self):

    self.Admin_Mode = {
        'bg': '#333',
        'fg': 'white',
        'entry_bg': '#568259',
        'entry_fg': 'white',
        'button_bg': '#568259',
        'button_fg': 'white'
    }
    
    self.apply_theme(self.Admin_Mode)

    #Admin Colours :)
    self.admin_button = tk.Button(self, text="Admin", height=5, width=10, command=self.Admin_Console)
    self.admin_button.grid(row=5, column=0)


App = Pokedex()
App.title('Pokedex')
App.mainloop()