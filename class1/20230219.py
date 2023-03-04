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
# Label 上各種relief
"""
# 建立 label
Label1 = Label(root, text = "flat", relief = "flat")
# 加入視窗
Label1.pack()
Label2 = Label(root, text = "flat", relief = "groove")
Label2.pack()
Label3 = Label(root, text = "flat", relief = "raised")
Label3.pack()
Label4 = Label(root, text = "flat", relief = "ridge")
Label4.pack()
Label5 = Label(root, text = "flat", relief = "solid")
Label5.pack()
Label6 = Label(root, text = "flat", relief = "sunken")
Label6.pack()
# 重複執行 root 物件
root.mainloop()
"""
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
# 建立 StatusBar
StatusBar = Label(root, text = "Initialiation", relief = "sunken", anchor = W)
# 加入視窗
StatusBar.pack(side = BOTTOM, fill = X)
# 建立StringVar
mystringvar = StringVar()
mystringvar.set("")
# 建立 start按鈕
start = Button(root, text = "start", command = start)
start.pack()
# 建立 stop按鈕
stop = Button(root, text = "stop", command = stop)
stop.pack()
# get mylabel的文字內容
Label(root, text = mystringvar.get()).pack()
# 重複執行 root 物件
root.mainloop()
"""
# 建立清單
"""
# 建立 Treeview
table = ttk.Treeview(root, columns = ["Product Name", "Unit Price", "Quantity"])
# 建立 columns 名稱
table.heading("#0", text = "Product Name")
table.heading("#1", text = "Unit Price")
table.heading("#2", text = "Quantity")
table.heading("#3", text = "Subtotal")
# 設定 column 樣式
table.column("#0", width = 250, anchor = CENTER)
table.column("#1", width = 250,anchor = CENTER)
table.column("#2", width = 250,anchor = CENTER)
table.column("#3", width = 250,anchor = CENTER)
#建立內容,從 total 行是用淺灰色底
table.tag_configure("totalcolor", background = "#E7E2E2")
#輸入每列內容
table.insert( '' , index = "end", text= "Sofa", values = ("20000", "2", "40000"))
#輸入 total 內容
table.insert( '' , index = "end", text= "total", values = ("20000", "2", "40000"), tags = ("totalcolor"))
# 加入視窗
table.pack()
# 重複執行 root 物件
root.mainloop()
"""
