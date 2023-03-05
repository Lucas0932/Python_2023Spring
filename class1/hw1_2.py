# import tkinter 的全部
from tkinter import *
# import PIL.Image
import PIL.Image
# import PIL.ImageTk
import PIL.ImageTk
# import tkinter 的 messagebox
from tkinter import messagebox
# import tkinter.ttk
import tkinter.ttk as ttk
#add function
def add(numlabel, pricelabel):
    numlabel["text"] = int(numlabel["text"])+1
    price = int(pricelabel["text"].split(".")[1].replace(","," ".strip()))
    total = int(totalval.get().split(":")[1].replace("元", " ").strip())
    totalval.set("共消費: "+str(total+price)+" 元")
#minus function
def minus(numlabel, pricelabel):
    if int(numlabel["text"])>0:
        numlabel["text"] = int(numlabel["text"])-1
        price = int(pricelabel["text"].split(".")[1].replace(","," ".strip()))
        total = int(totalval.get().split(":")[1].replace("元", " ").strip())
        totalval.set("共消費: "+str(total-price)+" 元")

    else:
        messagebox.showwarning("showwarning", "The number of products can\'t be below 0.")
root = Tk()
def detailwindow():
    # 建立新視窗Detail Windows
    DetailWindows = Toplevel(root)
    # 建立 Treeview
    table = ttk.Treeview(DetailWindows, columns = ["Product Name", "Unit Price", "Quantity"])
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
    # 建立內容,從 total 行是用淺灰色底
    table.tag_configure("totalcolor", background = "#E7E2E2")
    # 輸入第一列內容
    subtotal1 = int(sofa1pricelabel["text"].split(".")[1].replace(","," ".strip()))*int(sofa1numlabel["text"])
    table.insert( '' , index = "end", text= "Iphone 14 pro", values = (sofa1pricelabel["text"].split(".")[1].replace(","," ".strip()), sofa1numlabel["text"], subtotal1))
    # 輸入第一列內容
    subtotal2 = int(sofa1pricelabel["text"].split(".")[1].replace(","," ".strip()))*int(sofa1numlabel["text"])
    table.insert( '' , index = "end", text= "Iphone 14 pro", values = (sofa1pricelabel["text"].split(".")[1].replace(","," ".strip()), sofa1numlabel["text"], subtotal1))
    # 輸入第一列內容
    subtotal3 = int(sofa1pricelabel["text"].split(".")[1].replace(","," ".strip()))*int(sofa1numlabel["text"])
    table.insert( '' , index = "end", text= "Iphone 14 pro", values = (sofa1pricelabel["text"].split(".")[1].replace(","," ".strip()), sofa1numlabel["text"], subtotal1))
    # 輸入第一列內容
    subtotal4 = int(sofa1pricelabel["text"].split(".")[1].replace(","," ".strip()))*int(sofa1numlabel["text"])
    table.insert( '' , index = "end", text= "Iphone 14 pro", values = (sofa1pricelabel["text"].split(".")[1].replace(","," ".strip()), sofa1numlabel["text"], subtotal1))
    # 輸入 total 內容
    table.insert( '' , index = "end", text= "total", values = ("", "", subtotal1+subtotal2+subtotal3+subtotal4), tags = ("totalcolor"))
    # 加入視窗
    table.pack()
    # 重複執行 root 物件
    DetailWindows.mainloop()
def createNewWindow():
    #建立新視窗New Windows
    newWindow = Toplevel(root)
    newWindow.geometry("200x100")
    #建立新label在New Windows裡
    mylabel = Label(newWindow, text = "已結帳完成!")
    mylabel.pack()
    #執行新視窗城市
    newWindow.mainloop()
def openone():
    #建立新視窗New Windows
    newWindow = Toplevel(root)
    newWindow.geometry("200x100")
    #建立新label在New Windows裡
    mylabel = Label(newWindow, text = "目前仍在製作中，敬請期待!")
    mylabel.pack()
    #執行新視窗城市
    newWindow.mainloop()
root.title("KubeTech Shop")
root.geometry("870x640+0+0")
img =PIL.Image.open("C:/Users/Lucas/Documents/Python_2022Autumn/class10/image/applelogo1.jpg")
resized_image = img.resize((32, 32))
tk_img = PIL.ImageTk.PhotoImage(resized_image)

#upper Label & Nutton of window
titleimg = PIL.Image.open("C:/Users/Lucas/Documents/Python_2022Autumn/class10/image/applelogo1.jpg")
titleimg = titleimg.resize((32, 32))
titleimg = PIL.ImageTk.PhotoImage(titleimg)
titlelabel = Label(root, image = titleimg, width = 32, height = 32)
phonebutton = Button(root, text = "手機", font = ("Inter", 10), fg = "#1E1E1E", bg = "#ECE8E7", width = 5, pady = 2)
padbutton = Button(root, text = "平板", font = ("Inter", 10), fg = "#1E1E1E", bg = "#ECE8E7", width = 5, pady = 2, command = openone)
earphonebutton = Button(root, text = "耳機", font = ("Inter", 10), fg = "#1E1E1E", bg = "#ECE8E7", width = 5, pady = 2, command = openone)
loginbutton = Button(root, text = "會員登入/註冊", font = ("Inter", 10), fg = "#1E1E1E", bg = "#ECE8E7", width = 12, pady = 2)
bannerimg = PIL.Image.open("C:/Users/Lucas/Documents/Python_2022Autumn/class10/image/2022-12-18.png")
bannerimg = bannerimg.resize((852, 298))
bannerimg = PIL.ImageTk.PhotoImage(bannerimg)
bannerlabel = Label(root, image = bannerimg, width = 852, height = 298)
#upper layout
titlelabel.grid(column = 0, row = 0, sticky = W)
phonebutton.grid(row = 0, column = 1, sticky = E+W)
earphonebutton.grid(row = 0, column = 3, sticky = E+W)
loginbutton.grid(row = 0, column = 7, sticky = E, padx = 5)
bannerlabel.grid(column = 0, row = 1, columnspan = 8, padx = 5)
padbutton.grid(row = 0, column = 2, sticky = E+W)
#product1 Label & Button 元件
phone1img = PIL.Image.open("C:/Users/Lucas/Documents/Python_2022Autumn/class10/image/Iphone14.jpg")
phone1img = phone1img.resize((202,200))
phone1img = PIL.ImageTk.PhotoImage(phone1img)
phone1piclabel = Label(root, image = phone1img, width = 202, height = 200)
phone1piclabel.grid(row = 2, column = 0, columnspan = 2, sticky = W, padx = 5)
#product2 Label & Button 元件
sofa2img = PIL.Image.open("C:/Users/Lucas/Documents/Python_2022Autumn/class10/image/Iphone13.jpg")
sofa2img = sofa2img.resize((202,200))
sofa2img = PIL.ImageTk.PhotoImage(sofa2img)
sofa2piclabel = Label(root, image = sofa2img, width = 202, height = 200)
sofa2piclabel.grid(row = 2, column = 2, columnspan = 2, sticky = W, padx = 5)
#product3 Label & Button 元件
sofa3img = PIL.Image.open("C:/Users/Lucas/Documents/Python_2022Autumn/class10/image/Iphone12.jpg")
sofa3img = sofa3img.resize((202,200))
sofa3img = PIL.ImageTk.PhotoImage(sofa3img)
sofa3piclabel = Label(root, image = sofa3img, width = 202, height = 200)
sofa3piclabel.grid(row = 2, column = 4, columnspan = 2, sticky = W, padx = 5)
#product4 Label & Button 元件
sofa4img = PIL.Image.open("C:/Users/Lucas/Documents/Python_2022Autumn/class10/image/Iphone11.jpg")
sofa4img = sofa4img.resize((202,200))
sofa4img = PIL.ImageTk.PhotoImage(sofa4img)
sofa4piclabel = Label(root, image = sofa4img, width = 202, height = 200)
sofa4piclabel.grid(row = 2, column = 6, columnspan = 2, sticky = W, padx = 5)

sofa1namelabel = Label(root, text = "Iphone 14 pro", font = ("Inter", 9), fg = "#000000")
sofa1namelabel.grid(row = 3, column = 0, columnspan = 2, sticky = W, padx = 5)
sofa2namelabel = Label(root, text = "Iphone 13 pro", font = ("Inter", 9), fg = "#000000")
sofa2namelabel.grid(row = 3, column = 2, columnspan = 2, sticky = W, padx = 5)
sofa3namelabel = Label(root, text = "Iphone 12 pro", font = ("Inter", 9), fg = "#000000")
sofa3namelabel.grid(row = 3, column = 4, columnspan = 2, sticky = W, padx = 5)
sofa4namelabel = Label(root, text = "Iphone 11 pro", font = ("Inter", 9), fg = "#000000")
sofa4namelabel.grid(row = 3, column = 6, columnspan = 2, sticky = W, padx = 5)

sofa1pricelabel = Label(root, text = "NT.1,000,000", font = ("Inter", 10), fg = "#000000")
sofa1pricelabel.grid(row = 4, column = 0, sticky = W, padx = 5)
sofa2pricelabel = Label(root, text = "NT.850,000", font = ("Inter", 10), fg = "#000000")
sofa2pricelabel.grid(row = 4, column = 2, sticky = W, padx = 5)
sofa3pricelabel = Label(root, text = "NT.600,000", font = ("Inter", 10), fg = "#000000")
sofa3pricelabel.grid(row = 4, column = 4, sticky = W, padx = 5)
sofa4pricelabel = Label(root, text = "NT.300,000", font = ("Inter", 10), fg = "#000000")
sofa4pricelabel.grid(row = 4, column = 6, sticky = W, padx = 5)

sofa1numlabel = Label(root, text = "0", font = ("Inter", 12, "bold"), fg = "#000000")
sofa1addbutton = Button(root, text = "+", font = ("Inter", 10), fg = "#1E1E1E", bg = "#E7E2E2", command = lambda: add(sofa1numlabel, sofa1pricelabel))
sofa1minusbutton = Button(root, text = "-", font = ("Inter", 10), fg = "#1E1E1E", bg = "#E7E2E2", command = lambda: minus(sofa1numlabel, sofa1pricelabel))
sofa2numlabel = Label(root, text = "0", font = ("Inter", 12, "bold"), fg = "#000000")
sofa2addbutton = Button(root, text = "+", font = ("Inter", 10), fg = "#1E1E1E", bg = "#E7E2E2", command = lambda: add(sofa2numlabel, sofa2pricelabel))
sofa2minusbutton = Button(root, text = "-", font = ("Inter", 10), fg = "#1E1E1E", bg = "#E7E2E2", command = lambda: minus(sofa2numlabel, sofa2pricelabel))
sofa3numlabel = Label(root, text = "0", font = ("Inter", 12, "bold"), fg = "#000000")
sofa3addbutton = Button(root, text = "+", font = ("Inter", 10), fg = "#1E1E1E", bg = "#E7E2E2", command = lambda: add(sofa3numlabel, sofa3pricelabel))
sofa3minusbutton = Button(root, text = "-", font = ("Inter", 10), fg = "#1E1E1E", bg = "#E7E2E2", command = lambda: minus(sofa3numlabel, sofa3pricelabel))
sofa4numlabel = Label(root, text = "0", font = ("Inter", 12, "bold"), fg = "#000000")
sofa4addbutton = Button(root, text = "+", font = ("Inter", 10), fg = "#1E1E1E", bg = "#E7E2E2", command = lambda: add(sofa4numlabel, sofa4pricelabel))
sofa4minusbutton = Button(root, text = "-", font = ("Inter", 10), fg = "#1E1E1E", bg = "#E7E2E2", command = lambda: minus(sofa4numlabel, sofa4pricelabel))



sofa1minusbutton.grid(row = 4, column = 1, sticky = W)
sofa1numlabel.grid(row = 4, column = 1)
sofa1addbutton.grid(row = 4, column = 1, sticky = E)
sofa2minusbutton.grid(row = 4, column = 3, sticky = W)
sofa2numlabel.grid(row = 4, column = 3)
sofa2addbutton.grid(row = 4, column = 3, sticky = E)
sofa3minusbutton.grid(row = 4, column = 5, sticky = W)
sofa3numlabel.grid(row = 4, column = 5)
sofa3addbutton.grid(row = 4, column = 5, sticky = E)
sofa4minusbutton.grid(row = 4, column = 7, sticky = W)
sofa4numlabel.grid(row = 4, column = 7)
sofa4addbutton.grid(row = 4, column = 7, sticky = E)

#row 5 height 
root.rowconfigure(5, weight = 2)

detaillistbutton = Button(root, text = "詳細清單", font = ("Inter", 10, "bold"), fg = "#1E1E1E", bg = "#ECEDE7", command = detailwindow)
detaillistbutton.grid(row=5, column = 0, sticky = W+S, padx = 5, pady = 1)

shoppingcartimg = PIL.Image.open("C:/Users/Lucas/Documents/Python_2022Autumn/class10/image/shopping Cart.png")
shoppingcartimg = shoppingcartimg.resize((30,30))
shoppingcartimg = PIL.ImageTk.PhotoImage(shoppingcartimg)
shoppingcartpiclabel = Label(root, image = shoppingcartimg, width = 30, height = 30)
shoppingcartpiclabel.grid(row = 5, column = 4, sticky = E+S)

totalval = StringVar()
totalval.set("共消費: 0 元")
totallabel = Label(root, textvariable = totalval, font = ("Inter", 12), fg = "#000000")
checkoutbutton = Button(root, text = "結帳", font = ("Inter", 12), fg = "#1E1E1E", bg = "#ECEDE7", command = createNewWindow)
totallabel.grid(row = 5, column = 6, columnspan = 2, sticky = W+S)
checkoutbutton.grid(row = 5, column = 7, sticky = E+S)
root.mainloop()