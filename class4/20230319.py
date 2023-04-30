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