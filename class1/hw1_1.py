# 引入 tkinter module
from tkinter import *
# 引入 tkinter.ttk module
import tkinter.ttk as ttk
# 引入 Pillow module
from PIL import Image, ImageTk
# 建立主視窗 Frame
root = Tk()
# 設定視窗大小
root.geometry("1000x500+500+150")
# 開啟圖片
img = Image.open('C:/Users/Lucas/Documents/Python_2023Spring/class1/logo_tree.png')
# 轉換為 tk 圖片物件
tk_img = ImageTk.PhotoImage(img)
# 設定程式 icon
root.iconphoto(True, tk_img)
# 點按鈕跑出status(靜態方法)(processing, done)
"""
# 建立 StatusBar
StatusBar = Label(root, text = "Initialiation", relief = "sunken", anchor = W)
# 加入視窗
StatusBar.pack(side = BOTTOM, fill = X)
# 建立 start function
def start():
    StatusBar["text"] = (str("processing..."))
# 建立 stop function
def stop():
    StatusBar["text"] = (str("done"))
# 建立 button1
mybutton1 = Button(root, text = "Start", command = start).pack()
# 建立 button2
mybutton2 = Button(root, text = "stop", command = stop).pack()
# 重複執行 root 物件
root.mainloop()
"""
# 點按鈕跑出status(動態方法)(processing, done)
"""
# 建立StringVar
mystringvar = StringVar()
mystringvar.set("Initialiation")
# 建立 StatusBar
StatusBar = Label(root, textvariable = mystringvar, relief = "sunken", anchor = W)
# 加入視窗
StatusBar.pack(side = BOTTOM, fill = X)
# 建立 start function
def go():
    # 建立StringVar
    mystringvar.set("start")
# 建立 stop function
def no():
    mystringvar.set("stop")
# 建立 start按鈕
start = Button(root, text = "start", command = go)
start.pack()
# 建立 stop按鈕
stop = Button(root, text = "stop", command = no)
stop.pack()
# 重複執行 root 物件
root.mainloop()
"""