# 引入 pandas 套件
import pandas as pd
# 引入 pygsheets 套件
import pygsheets
# 引入 tkinter 套件
from tkinter import *
# 引入 tkinter.ttk 套件
import tkinter.ttk as ttk
# 引入 PIL 套件
from PIL import Image, ImageTk
# 引入 messagebox 套件
from tkinter import messagebox
# 引入 requests 套件
import requests
# 建立主視窗 Frame
root = Tk()
gc = pygsheets.authorize(service_file = "C:/Users/Lucas/Documents/Python_2023Spring/class7/double-zenith-383613-e7b227ae03b3.json")
sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/1LZPZ0QDtbQR8_r5Un3BGbn5jwSclXUIA11D_arPsrv4/edit#gid=0")
ws = sht.worksheet_by_title("homework2")
ws.update_value("A1", "國家")
ws.update_value("A2", "美國")
ws.update_value("A3", "日本")
ws.update_value("A4", "香港")
ws.update_value("B1", "匯率 (以台幣為基準)")
url = "https://api.exchangerate-api.com/v4/latest/TWD"
res = requests.get(url)
data = res.json()
print("日幣對台幣的匯率為" + str(data["rates"]["JPY"]))
ws.update_value("B2", str(data["rates"]["USD"]))
ws.update_value("B3", str(data["rates"]["JPY"]))
ws.update_value("B4", str(data["rates"]["HKD"]))