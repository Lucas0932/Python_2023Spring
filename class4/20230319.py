# 引入 tkinter module
from tkinter import *
# 引入 tkinter.ttk module
import tkinter.ttk as ttk
# 引入 Pillow module
from PIL import Image, ImageTk
# 引入 tkscrolledframe 的 scrolledframe
from tkscrolledframe import ScrolledFrame
# 從 tkinter 中引入 filedialog
from tkinter import filedialog
# import PIL.Image
import PIL.Image
# import PIL.ImageTk
import PIL.ImageTk
# 建立主視窗 Frame
root = Tk()
# about Scale
"""
# 建立def
def getValue(e):
    value.set("年齡: "+str(year_scale.get()))
# 建立標題 Label
titlelabel = Label(root, text = "請選擇年齡")
titlelabel.grid(row = 0, column = 0, columnspan = 2, sticky = W)
# 建立 Scale 元件
year_scale = Scale(root, from_ = 0, to = 300, orient = "horizontal", resolution = 1, length = 300, showvalue = True, command = getValue)
year_scale.grid(row = 1, column = 0, columnspan = 3)
# 建立字串變數
value = StringVar()
value.set("年齡: 0")
# 建立 Label
statusBar1 = Label(root, textvariable = value, fg = "black", bg = "white", anchor = W, relief = "sunken", bd = 2)
statusBar1.grid(row = 2, column = 0, columnspan = 3, sticky = W+E+S)
# 重複執行 root 物件
root.mainloop()
"""
# about spinbox
"""
# 建立字串變數
value = StringVar()
# 建立標題 Spinbox
height = Spinbox(root, from_ = 99, to = 250, textvariable = value)
height.grid(row = 1, column = 0, columnspan = 3, sticky = W+E+S)
# 建立標題 Label
statusBar1 = Label(root, text = "身高: ")
# 加入視窗
statusBar1.grid(row = 0, column = 0, columnspan = 2, sticky = W)
# 建立標題 Label
statusBar2 = Label(root, textvariable = value)
# 加入視窗
statusBar2.grid(row = 0, column = 1, columnspan = 2, sticky = W)
# 重複執行 root 物件
root.mainloop()
"""

""""""
# 建立def
def getValue(e):
    # 取得RGB
    r = int(year_scale1.get())
    g = int(year_scale2.get())
    b = int(year_scale3.get())
    # 數值轉換為16進位
    hex = "#{:02x}{:02x}{:02x}".format (r, g, b)
    # 分別設定 Label 文字內容
    statusBar1["text"] = "R: "+str(year_scale1.get)
    statusBar2["text"] = "R: "+str(year_scale2.get)
    statusBar3["text"] = "R: "+str(year_scale3.get)
    # 分別設定 statusBar1 背景
    color["bg"] = hex
    color["text"] = hex
# 建立 title label
title = Label(root, text = "選擇顏色(R,G,B)")
# 加入視窗
title.grid(row = 0, column = 0)
# 建立字串變數
value1 = StringVar()
value1.set("R: 0")
# 建立 Label
statusBar1 = Label(root, textvariable = value1, fg = "black", anchor = W, relief = "sunken", bd = 2)
# 加入視窗
statusBar1.grid(row = 1, column = 0, columnspan = 3, sticky = W+E+S)
# 建立 Scale 元件
year_scale1 = Scale(root, from_ = 0, to = 255, orient = "horizontal", resolution = 1, length = 300, showvalue = True, command = getValue)
year_scale1.grid(row = 2, column = 0, columnspan = 3)
# 建立字串變數
value2 = StringVar()
value2.set("G: 0")
# 建立 Label
statusBar2 = Label(root, textvariable = value2, fg = "black", anchor = W, relief = "sunken", bd = 2)
# 加入視窗
statusBar2.grid(row = 3, column = 0, columnspan = 3, sticky = W+E+S)
# 建立 Scale 元件
year_scale2 = Scale(root, from_ = 0, to = 255, orient = "horizontal", resolution = 1, length = 300, showvalue = True, command = getValue)
year_scale2.grid(row = 4, column = 0, columnspan = 3)
# 建立字串變數
value3 = StringVar()
value3.set("B: 0")
# 建立 Label
statusBar3 = Label(root, textvariable = value3, fg = "black", anchor = W, relief = "sunken", bd = 2)
# 加入視窗
statusBar3.grid(row = 5, column = 0, columnspan = 3, sticky = W+E+S)
# 建立 Scale 元件
year_scale3 = Scale(root, from_ = 0, to = 255, orient = "horizontal", resolution = 1, length = 300, showvalue = True, command = getValue)
year_scale3.grid(row = 6, column = 0, columnspan = 3)
color = Label(root, text = "", fg = "white", bg = "white", relief = "sunken", bd = 2, font = (20), anchor = "center")
color.grid(row = 7, column = 0, columnspan = 3, sticky = W+E+S)
# 重複執行 root 物件
root.mainloop()