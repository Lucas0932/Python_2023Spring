# 引入 tkinter module
from tkinter import *
# 引入 tkinter.ttk module
import tkinter.ttk as ttk
# 引入 Pillow module
from PIL import Image, ImageTk
# 引入 tkscrolledframe 的 scrolledframe
from tkscrolledframe import ScrolledFrame
# 建立主視窗 Frame
root = Tk()
# 建立 ScrolledFrame 元件
sframe1 = ScrolledFrame(root, width = 300, height = 300)
sframe1.grid()
# 設定視窗大小
root.geometry("320x100")
# 創建一個含有 ScrolledFrame 元件的 Frame
inner_frame = sframe1.display_widget(Frame)
# 綁定鼠標及滾輪
sframe1.bind_arrow_keys(root)
sframe1.bind_scroll_wheel(root)
# 建立def
def press():
    text = (group1.get())+ " "+ (group2.get())+ " "+ (group3.get()+" "+group4.get()+" "+group5.get()+" "+group6.get())
    StatusBar["text"] = text
# 建立stringvar
group = StringVar()
# 建立stringvar1
group1 = StringVar()
# 建立stringvar2
group2 = StringVar()
# 製作stringvar3
group3 = StringVar()
# 製作stringvar4
group4 = StringVar()
# 製作stringvar5
group5 = StringVar()
# 製作stringvar6
group6 = StringVar()
# 建立主餐label
label1 = Label(inner_frame, text = "請選擇主餐種類:")
# 加入視窗
label1.grid(row = 0, column = 0)
# 建立第一個選項
Checkbutton1 = Checkbutton(inner_frame, text = "和牛", variable = group1, onvalue = "和牛", offvalue = "", command = press)
# 加入視窗
Checkbutton1.grid(row = 1, column = 0)
# 建立第二個選項
Checkbutton2 = Checkbutton(inner_frame, text = "伊比利豬", variable = group2, onvalue = "伊比利豬", offvalue = "", command = press)
# 加入視窗
Checkbutton2.grid(row = 1, column = 1)
# 建立第三個選項
Checkbutton3 = Checkbutton(inner_frame, text = "海鮮", variable = group3, onvalue = "海鮮", offvalue = "", command = press)
# 加入視窗
Checkbutton3.grid(row = 1, column = 2)
# 建立飲料label
label2 = Label(inner_frame, text = "請選擇飲料種類:")
# 加入視窗
label2.grid(row = 2, column = 0)
# 建立第四個選項
Checkbutton4 = Checkbutton(inner_frame, text = "莊園咖啡", variable = group4, onvalue = "莊園咖啡", offvalue = "", command = press)
# 加入視窗
Checkbutton4.grid(row = 3, column = 0)
# 建立第五個選項
Checkbutton5 = Checkbutton(inner_frame, text = "日月潭蜜香紅茶", variable = group5, onvalue = "日月潭蜜香紅茶", offvalue = "", command = press)
# 加入視窗
Checkbutton5.grid(row = 3, column = 1)
# 建立第六個選項
Checkbutton6 = Checkbutton(inner_frame, text = "伯爵奶茶", variable = group6, onvalue = "伯爵奶茶", offvalue = "", command = press)
# 加入視窗
Checkbutton6.grid(row = 3, column = 2)
# 建立 StatusBar
StatusBar = Label(inner_frame, text = "")
# 加入視窗
StatusBar.grid(row = 4, column = 0, columnspan = 3, sticky = N+W+E)
# 重複執行 root 物件
root.mainloop()