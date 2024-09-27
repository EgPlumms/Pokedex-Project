import csv
import requests
import pandas as pd 
import matplotlib
import hashlib
import json

def register():
    with open("UserData.csv",mode="a", newline="") as f:
        writer = csv.writer(f,delimiter=",") 
        username = input("Please Enter Username:")
        password = input("Please Enter Password:")
        password_2 = input("Re-Enter Password:")
        user = "User" # Sets The User As A User And Not An Admin 
        if password == password_2: #Makes Sure The Password Entered Is Correct
            writer.writerow([username,password,user]) #Enters Users Username And Password Into Csv File
            print("New User Registered!")
        else:
            print("Please Try Again!")


username = input("Enter Username:")
password = input("Enter Password:")
user = "User"
with open("UserData.csv", mode="r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        if row == [username,password,user]:
            print("You've Logged In Welcome", username)

            
