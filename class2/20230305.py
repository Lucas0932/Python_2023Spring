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
# 利用動態 radiobutton製作三選一選項，並出現在下方
"""
# 製作stringvar
group = StringVar()
# 建立目的地label
label1 = Label(text = "目的地", font = 24)
# 加入視窗
label1.grid(row = 0, column = 0)
# 建立第一個選項
Radiobutton1 = Radiobutton(text = "東京", variable = group, value = "東京")
# 加入視窗
Radiobutton1.grid(row = 1, column = 0)
# 建立第二個選項
Radiobutton2 = Radiobutton(text = "德國", variable = group, value = "德國")
# 加入視窗
Radiobutton2.grid(row = 1, column = 1)
# 建立第三個選項
Radiobutton3 = Radiobutton(text = "紐約", variable = group, value = "紐約")
# 加入視窗
Radiobutton3.grid(row = 1, column = 2)
# 建立 StatusBar
StatusBar = Label(root, textvariable = group, relief = "sunken", anchor = W)
# 加入視窗
StatusBar.grid(row = 2, column = 0, columnspan = 3, sticky = N+W+E)
# 重複執行 root 物件
root.mainloop()
"""
# 利用動態 checkbutton製作三選一選項，並出現在下方
"""
# 建立def
def press():
    text = (group1.get())+ " "+ (group2.get())+ " "+ (group3.get())
    StatusBar["text"] = text
# 建立stringvar
group = StringVar()
# 建立stringvar1
group1 = StringVar()
# 建立stringvar2
group2 = StringVar()
# 製作stringvar3
group3 = StringVar()
# 建立目的地label
label1 = Label(text = "目的地", font = 24)
# 加入視窗
label1.grid(row = 0, column = 0)
# 建立第一個選項
Checkbutton1 = Checkbutton(text = "直飛", variable = group1, onvalue = "直飛", offvalue = "", command = press)
# 加入視窗
Checkbutton1.grid(row = 1, column = 0)
# 建立第二個選項
Checkbutton2 = Checkbutton(text = "轉機一次", variable = group2, onvalue = "轉機一次", offvalue = "", command = press)
# 加入視窗
Checkbutton2.grid(row = 1, column = 1)
# 建立第三個選項
Checkbutton3 = Checkbutton(text = "轉機兩次以上", variable = group3, onvalue = "轉機兩次以上", offvalue = "", command = press)
# 加入視窗
Checkbutton3.grid(row = 1, column = 2)
# 建立 StatusBar
StatusBar = Label(root, text = "")
# 加入視窗
StatusBar.grid(row = 2, column = 0, columnspan = 3, sticky = N+W+E)
# 重複執行 root 物件
root.mainloop()
"""
# 建立 ScrolledFrame 元件
sframe1 = ScrolledFrame(root, width = 300, height = 300)
sframe1.pack()
# 創建一個含有 ScrolledFrame 元件的 Frame
inner_frame = sframe1.display_widget(Frame)
# 綁定鼠標及滾輪
sframe1.bind_arrow_keys(root)
sframe1.bind_scroll_wheel(root)
# 創建 button1
button1 = Button(inner_frame, text = 1, height = 5)
# 加入視窗
button1.pack()
# 創建 button2
button2 = Button(inner_frame, text = 2, height = 5)
# 加入視窗
button2.pack()
# 創建 button3
button3 = Button(inner_frame, text = 3, height = 5)
# 加入視窗
button3.pack()
# 創建 button4
button4 = Button(inner_frame, text = 4, height = 5)
# 加入視窗
button4.pack()
# 創建 button5
button5 = Button(inner_frame, text = 5, height = 5)
# 加入視窗
button5.pack()
# 重複執行 root 物件
root.mainloop()