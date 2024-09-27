import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import *
import csv

ws = Tk()
ws.title('PythonGuides')

def backing(self):
    self.Img = tk.PhotoImage(file="Pokeball.png")
    self.ImgLabel = ttk.Label(self, image=self.Img)
#How to I Put This Into My Pokedex without It Breaking Tho?
#Need To Make Its Own function To Call Upon But Why Does It Break Everytime?