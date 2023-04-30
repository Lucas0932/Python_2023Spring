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
# 建立 ScrolledFrame 元件
"""
sframe1 = ScrolledFrame(root, width = 300, height = 300, bg = "black")
sframe1.grid()
# 創建一個含有 ScrolledFrame 元件的 Frame
inner_frame = sframe1.display_widget(Frame)
# 綁定鼠標及滾輪
sframe1.bind_arrow_keys(root)
sframe1.bind_scroll_wheel(root)
# 創建 button1
button1 = Button(inner_frame, text = 1, height = 5)
# 加入視窗
button1.grid()
# 創建 button2
button2 = Button(inner_frame, text = 2, height = 5)
# 加入視窗
button2.grid()
# 創建 button3
button3 = Button(inner_frame, text = 3, height = 5)
# 加入視窗
button3.grid()
# 創建 button4
button4 = Button(inner_frame, text = 4, height = 5)
# 加入視窗
button4.grid()
# 創建 button5
button5 = Button(inner_frame, text = 5, height = 5)
# 加入視窗
button5.grid()
# 重複執行 root 物件
root.mainloop()
"""
# 建立 Combobox
"""
def press():
    text = listbox.get(listbox.curselection())
    StatusBar["text"] = text
# 宣告用於 ListBox 的文字變數
listVar = StringVar()
# 建立 listBMW
BMW=["1 Series (F40)","1 Series (F52)","2 Series Gran Coupé","2 Series","3 Series","4 Series","5 Series","6 Series","7 Series","8 Series","X1","X2","X3","X4","X5","X6","X7","Z4","2 Series Active Tourer","i3 (G28)","i4","i7","iX1","iX3","iX"]
# 將多個選項內容存入 listVar
listVar.set(BMW)
# 建立清單列表 ListBox
listbox = Listbox(root, selectmode = "extended", listvariable = listVar)
# 加入視窗
listbox.pack()
# 建立按鈕 Choose
Choose = Button(root, text = "Choose", command = press)
# 加入視窗
Choose.pack()
# 建立 StatusBar
StatusBar = Label(root, text = "")
# 加入視窗
StatusBar.pack()
# 重複執行 root 物件
root.mainloop()
"""
# 建立清單列表 ListBox
"""
# 建立清單列表 ListBox
listbox = Listbox(root, selectmode = "extended")
# 加入列表選項
listbox.insert(1, "A1")
listbox.insert(2, "A3")
listbox.insert(3, "A4")
# 加入視窗
listbox.pack()
# 重複執行 root 物件
root.mainloop()
"""
# 建立下拉式選單
"""
def press():
    text = ("廠牌:")+(str(box.current()))+". "+(box.get())
    StatusBar["text"] = text
# 建立下拉式選單 Combobox
box = ttk.Combobox(root, values = ["BMW", "Mercedes Benz", "Audi"])
# 加入視窗
box.pack()
# 建立按鈕 OK
OK = Button(root, text = "Ok", command = press)
# 加入視窗
OK.pack()
# 建立 StatusBar
StatusBar = Label(root, text = "廠牌:")
# 加入視窗
StatusBar.pack()
# 重複執行 root 物件
root.mainloop()
"""
#建立可以打開檔案的模組, openfile
""""""
# 建立 def openfile
def openfile():
    # 單選檔案，並以 String 回傳路徑
    filePath = filedialog.askopenfilename(title = "選取照片", initialdir = "C:/Users/Lucas/OneDrive/Pictures/Screenshots", multiple = False, filetypes = [("All Files", "*.*"), ("PNG", "*.png"), ("JPG", "*.jpg")])
    # 開啟圖片
    img =PIL.Image.open(filePath)
    # 讓上面 import 的函式庫可以參照到 tk_img
    global tk_img
    # 轉換為 tk 圖片物件
    tk_img = PIL.ImageTk.PhotoImage(img)
    # 在 label 中放入圖片
    imagelabel["image"] = tk_img
# 建立 Button 觸發 openfile function
openBtn = Button(root, text = "Choose", command = openfile)
# 加入視窗
openBtn.pack()
# 在 Lable 中放入圖片
imagelabel = Label(root)
# 加入視窗
imagelabel.pack()
# 重複執行 root 物件
root.mainloop()
