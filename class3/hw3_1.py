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
# 建立主視窗 Frame
root = Tk()
# 建立 StatusBar1
StatusBar1 = Label(root, text = "")
# 加入視窗
StatusBar1.pack(fill = X)
def press():
    num = box.current()+1
    text1 = ("廠牌:")+str(num)+". "+(box.get())
    StatusBar1["text"] = text1
    ans = box.current()+1
    if box.current() == 0:
        listVar.set(BMW)
    elif box.current() == 1:
        listVar.set(Mercedes)
    elif box.current() == 2:
        listVar.set(Audi)
# 宣告用於 ListBox 的文字變數
listVar = StringVar()
# 建立 listBMW
BMW=["1 Series (F40)","1 Series (F52)","2 Series Gran Coupé","2 Series","3 Series","4 Series","5 Series","6 Series","7 Series","8 Series","X1","X2","X3","X4","X5","X6","X7","Z4","2 Series Active Tourer","i3 (G28)","i4","i7","iX1","iX3","iX"]
# 建立 listMercedes
Mercedes=["A-Class(Hatchbacks)","A-Class(Sedans)","C-Class","CLA","CLS","E-Class","EQE","EQS","S-Class","C-Class","CLA","E-Class","E-Class","EQA","EQB","EQC","G-Class","GLA","GLB","GLC","GLE","GLS","AMG GT","AMG GT 4-Door Coupé","AMG SL","AMG One","B-Class","Citan Van","Viano","EQV"]
# 建立 listAudi
Audi=["A1","A3","A4","A5","A6","A7","A8","e-tron GT","TT","R8","Q2","Q3","2019","Q4 e-tron","2021","Q5","Q5 e-tron","Q6","Q7","Q8","e-tron"]
# 建立下拉式選單 Combobox
box = ttk.Combobox(root, values = ["BMW", "Mercedes Benz", "Audi"])
# 加入視窗
box.pack()
# 建立按鈕 Choose
Choose = Button(root, text = "OK", command = press)
# 加入視窗
Choose.pack()
text2 = StringVar()
# 建立 StatusBar2
StatusBar2 = Label(root, textvariable = text2, bg = "white")
# 加入視窗
StatusBar2.pack(fill = X)
# 建立清單列表 ListBox
listbox = Listbox(root, selectmode = "extended", listvariable = listVar)
# 加入視窗
listbox.pack()
# 重複執行 root 物件
root.mainloop()