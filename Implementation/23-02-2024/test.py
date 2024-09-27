import tkinter as tk

root = tk.Tk() #Creates An Empty Window
root.geometry('350x480') #Can Be Used To Change The Width & Height Of The Window
root.title("Pokedex") #Changes The Windows Title
label = tk.Label(root, text="Pokedex Project!", font=('Bitter', 18)) #Adds Text To The Window
label.pack()

textbox = tk.Text(root, height = '3', font=('Bitter', 16)) #Creates A Box Around The Text
textbox.pack() #Allows Box To Be Seen

myentry = tk.Entry(root)
myentry.pack()

root.mainloop() #Runs The Created Window
