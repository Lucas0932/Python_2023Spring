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
ws = sht.worksheet_by_title("homework1")
# 讀取全部，寫入 google sheets
"""
# 讀取成 df
df = pd.DataFrame(ws.get_all_records())
# 寫資料進去
ws.set_dataframe(df, "A1")
print(df)
# 清除 sheet 內所有值
ws.clear()
print(df)
"""
# 利用 dataframe 來傳送資料(dict)
"""
d = {"Custormer Name":["Lucas", "Louie", "Halston"], "Weight":[39, 49, 59]}
df = pd.DataFrame(d)
# 寫資料進去
ws.set_dataframe(df, "A1")
print(df)
"""
# 範本
"""
# 不帶條件
r = requests.get("{你想要要求服務的網站 url}")
# 有帶條件
payload = {"key1": "value1", "key2": "value2"}
r = requests.get("{你想要要求服務的網站 url}", params = payload)
r = requests.post("{你想要要求服務的網站 url}", data = {"key": "value"})
"""
# Google 首頁 status code
"""
# 不帶條件
r = requests.get("http://www.google.com/")
# 列出 HTTP 狀態碼
print(r.status_code)
"""
# 利用網站找出匯率
"""
# 不帶條件
url = "https://api.exchangerate-api.com/v4/latest/TWD"
res = requests.get(url)
data = res.json()
print("日幣對台幣的匯率為" + str(data["rates"]["JPY"]))
"""