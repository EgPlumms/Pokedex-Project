import tkinter as tk
from tkinter import messagebox as mb
from tkinter import *
import csv

class LoginApp:
    def __init__(self, poke):
        self.poke = poke
        self.is_dark_mode = False
        self.poke.geometry('460x430')

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

        #Button To Get Up The Pokedex Page/Position
        self.Pokedex_Button = tk.Button(poke, text="Pokedex", height=5, width=10, command=self.Pokedex)
        self.Pokedex_Button.grid(row=0, column=0)

        #Button To Get Up Pokemon Team Page/Position
        self.Team_Button = tk.Button(poke, text="Team", height=5, width=10, command=self.Team)
        self.Team_Button.grid(row=1,column=0)

        #Button To Get Up Login Page/Position
        self.Log_Button = tk.Button(poke, text="Login", height=5, width=10, command=self.login)
        self.Log_Button.grid(row=2, column=0)

        #Dark Mode Button/Position
        self.DarkM_Button = tk.Button(poke, text="Toggle\n Dark Mode", height=5, width=10, command=self.toggle_theme)
        self.DarkM_Button.grid(row=3, column=0)

        #Exit Button/Position
        self.Exit_Button = tk.Button(poke, text="Exit Program", height=5, width=10, command=self.Exit_Program)
        self.Exit_Button.grid(row=4, column=0)

        self.apply_theme(self.light_mode)


    #Logged Out Menu
    def menu(self):
        #Button To Get Up The Pokedex Page/Position
        self.Pokedex_Button = tk.Button(poke, text="Pokedex", height=5, width=10)
        self.Pokedex_Button.grid(row=0, column=0)

        #Button To Get Up Pokemon Team Page/Position
        self.Team_Button = tk.Button(poke, text="Team", height=5, width=10)
        self.Team_Button.grid(row=1,column=0)

        #Button To Get Up Login Page/Position
        self.Log_Button = tk.Button(poke, text="Login", height=5, width=10, command=self.login)
        self.Log_Button.grid(row=2, column=0)

        #Dark Mode Button/Position
        self.DarkM_Button = tk.Button(poke, text="Toggle\n Dark Mode", height=5, width=10, command=self.toggle_theme)
        self.DarkM_Button.grid(row=3, column=0)

        #Exit Button/Position
        self.Exit_Button = tk.Button(poke, text="Exit Program", height=5, width=10, command=self.Exit_Program)
        self.Exit_Button.grid(row=4, column=0)

        #Makes Sure The Label Is On The Right Colour Mode
        if self.is_dark_mode:
            self.apply_theme(self.dark_mode) 
        else:
            self.apply_theme(self.light_mode)

        #Admin Colours :)
        #self.admin_button = tk.Button(poke, text="Admin", command=self.Admin_Console)
        #self.admin_button.grid(row=7, column=3, columnspan=2, pady=10)

    #Logged Out Team
    def Team(self):
        self.Team_Label = tk.Label(poke, text="Not Logged In No Team Available", font=('Arial',19),)
        self.Team_Label.grid(row=2,column=1, columnspan=2)
        #Makes Sure The Label Is On The Right Colour Mode
        if self.is_dark_mode:
            self.apply_theme(self.dark_mode) 
        else:
            self.apply_theme(self.light_mode)

    #Logged In Team
    def TeamL(self):
        pass

    #Logged Out Pokedex
    def Pokedex(self):
        pass

    #Logged In Pokedex
    def PokedexL(self):
        pass

    #Logged In Menu
    def Logged_Menu(self):

        #Button To Get Up The Pokedex Page/Position
        self.Pokedex_Button = tk.Button(poke, text="Pokedex", height=5, width=10)
        self.Pokedex_Button.grid(row=0, column=0)

        #Button To Get Up Pokemon Team Page/Position
        self.Team_Button = tk.Button(poke, text="Team", height=5, width=10)
        self.Team_Button.grid(row=1,column=0)

        #Button To Logout
        self.Logout_Button = tk.Button(poke, text="Logout", height=5, width=10, command=self.menu)
        self.Logout_Button.grid(row=2, column=0)

        #Dark Mode Button/Position
        self.DarkM_Button = tk.Button(poke, text="Toggle\n Dark Mode", height=5, width=10, command=self.toggle_theme)
        self.DarkM_Button.grid(row=3, column=0)

        #Exit Button/Position
        self.Exit_Button = tk.Button(poke, text="Exit Program", height=5, width=10, command=self.Exit_Program)
        self.Exit_Button.grid(row=4, column=0)

        #Makes Sure The Label Is On The Right Colour Mode
        if self.is_dark_mode:
            self.apply_theme(self.dark_mode) 
        else:
            self.apply_theme(self.light_mode)

    #Login Widgets
    def login(self):
        
        #Username Label/Positon
        self.Username_Label = tk.Label(poke, text="Username") 
        self.Username_Label.grid(row=0, column=2)
        
        #Username Entry/Position
        self.Username_Entry = tk.Entry(poke)
        self.Username_Entry.grid(row=0, column=3)
        
        #Password Label/Position
        self.Password_Label = tk.Label(poke, text="Password")
        self.Password_Label.grid(row=1, column=2)
        
        #Password Entry/Position
        self.Password_Entry = tk.Entry(poke, show="*")
        self.Password_Entry.grid(row=1, column=3)
        
        #Login Button/Position
        self.Login_Button = tk.Button(poke, text="Login", command=self.Log)
        self.Login_Button.grid(row=2, column=3, columnspan=2,)

        #Makes Sure The Label Is On The Right Colour Mode
        if self.is_dark_mode:
            self.apply_theme(self.dark_mode) 
        else:
            self.apply_theme(self.light_mode)
        
    #Log In Code
    def Log(self):
        username = self.Username_Entry.get()
        password = self.Password_Entry.get()

        with open("usernames.txt", 'r') as f: #opens the usernames text file
            info = f.read().splitlines() #reads the files info (turns the info in the file Into A Variable)
            if username in info: #searches file for the username Entered
                with open("passwords.txt", 'r') as f: #Opens The Password Text File
                    info1 = f.read().splitlines() #Reads The Files Info (turns the info in the file Into A Variable)
                    if password in info1:
                        self.Login_Label = tk.Label(poke, text="Logged In Successfully!\n "f"Welcome Back {username}!\n")
                        self.Login_Label.grid(row=4, column=3, columnspan=2)
                    self.Logged_Menu()
            else:
                self.LoginNo_Label = tk.Label(poke, text="Login Failed! Please Try Again.")
                self.LoginNo_Label.grid(row=4, column=3, columnspan=2)
                    
            #Makes Sure The Label Is On The Right Colour Mode
            if self.is_dark_mode:
                self.apply_theme(self.dark_mode) 
            else:
                self.apply_theme(self.light_mode)

    #Exits Program
    def Exit_Program(self):
        exit()

    #Applies Themes To The Different Components
    def apply_theme(self, theme):
        self.poke.config(bg=theme['bg'])

        for widget in self.poke.winfo_children():
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

poke = tk.Tk()
poke.title('Login App')
App = LoginApp(poke)
poke.mainloop()


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
                    self.Login_Label = tk.Label(poke, text="Logged In Successfully!\n "f"Welcome Back {username}!\n")
                    self.Login_Label.grid(row=4, column=1, columnspan=2)
                    self.menu()
                self.LoginNo_Label = tk.Label(poke, text="Login Failed! Please Try Again.")
                self.LoginNo_Label.grid(row=4, column=1, columnspan=2)
                self.login()
                    
                    #Makes Sure The Label Is On The Right Colour Mode
                if self.is_dark_mode:
                        self.apply_theme(self.dark_mode) 
                else:
                        self.apply_theme(self.light_mode)
        else:
            self.NuhUh_Label = tk.Label(poke, text="Your Username Is Either Incorrect Or Nonexistent. You Can Either Try Again Or Create A New Account.")
            self.NuhUh_Label.grid(row=4, column=1, columnspan=2) 
            self.Retry_Entry = tk.Entry(poke)
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
    
    filename = "UserData.csv"

    fields = []
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader('UserData.csv')

        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)

