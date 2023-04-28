import pygsheets
from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
root = Tk()
root.title("Google Sheets API")
gc = pygsheets.authorize(service_file = "C:/Users/Lucas/Documents/Python_2023Spring/class7/double-zenith-383613-e7b227ae03b3.json")
sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/1LZPZ0QDtbQR8_r5Un3BGbn5jwSclXUIA11D_arPsrv4/edit#gid=0")
ws = sht.worksheet_by_title("homework")
ws.update_value("A1", "Name")
ws.update_value("B1", "Email")
ws.update_value("C1", "password")
ws.update_value("D1", "Phone Number")
n = 1
def press():
    global n
    n += 1
    name = name_entrybox.get()
    email = email_entrybox.get()
    password = password_entrybox.get()
    phone_number = phone_number_entrybox.get()
    name_box = ("A" + str(n))
    email_box = ("B" + str(n))
    password_box = ("C" + str(n))
    phone_number_box = ("D" + str(n))
    ws.update_value(name_box, name)
    ws.update_value(email_box, email)
    ws.update_value(password_box, password)
    ws.update_value(phone_number_box, phone_number)
name_label = Label(root, text = "Name:", fg = "black", font = ("Arial", 18, "bold"))
name_label.grid(row = 0, column = 0)
name_entrybox = Entry(root, width = 30, font = ("Arial", 18, "bold"))
name_entrybox.grid(row = 1, column = 0)

email_label = Label(root, text = "Email:", fg = "black", font = ("Arial", 18, "bold"))
email_label.grid(row = 2, column = 0)
email_entrybox = Entry(root, width = 30, font = ("Arial", 18, "bold"))
email_entrybox.grid(row = 3, column = 0)

password_label = Label(root, text = "Password:", fg = "black", font = ("Arial", 18, "bold"))
password_label.grid(row = 4, column = 0)
password_entrybox = Entry(root, width = 30, font = ("Arial", 18, "bold"))
password_entrybox.grid(row = 5, column = 0)

phone_number = Label(root, text = "Phone Number:", fg = "black", font = ("Arial", 18, "bold"))
phone_number.grid(row = 6, column = 0)
phone_number_entrybox = Entry(root, width = 30, font = ("Arial", 18, "bold"))
phone_number_entrybox.grid(row = 7, column = 0)

sign_up = Button(root, text = "Sign Up", fg = "black", command = press)
sign_up.grid(row = 8, column = 0)

root.mainloop()