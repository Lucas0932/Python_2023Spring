# 引入 tkinter module
from tkinter import *
# 引入 tkinter.ttk module
import tkinter.ttk as ttk
# 引入 Pillow module
from PIL import Image as PILIMAGE
from PIL import ImageTk as PILImageTK
# 引入 messagebox module
from tkinter import messagebox
# 建立主視窗 Frame
root = Tk()
BestGames = ["project/img/AOV.jpg", "project/img/brawl.png", "project/img/mc.jpg", "project/img/roblox.jpg", 'project/img/Fornite.jpg', "project/img/Valorant.jpg", "project/img/Mech Arena.jpg"]
RecentGames = []
LongestGame = []
print(BestGames[0])
# 創建三個類別的中心點
BestMiddle = 2
RecentMiddle = 2
LongestMiddle = 2
# 登入按鈕
def Login():
    # 驗證
    def verifyUser(LoginWindow, AccountEntry, PasswordEntry):
        if AccountEntry.get() == "Lucas" and PasswordEntry.get() == "Lucas0932_tw":
            # 帳密輸入成功
            LoginWindow.destroy()
            LoginButton.destroy()
            Login["text"] = "Lucas"
            Login["state"] = "disabled"
        else:
            SayWrong = Label(LoginWindow, text = "User Name Or Password Wrong!", fg = "red")
            SayWrong.grid(column = 1, row = 4, columnspan = 2)
    LoginWindow = Toplevel(root)
    LoginWindow.title("Login")
    LoginWindow.geometry("280x200")
    UserLogin = Label(LoginWindow, text = "User Login")
    UserLogin.grid(column = 1, row = 0)
    Account = Label(LoginWindow, text = "Account")
    Account.grid(column = 0, row = 1)
    Password = Label(LoginWindow, text = "Password")
    Password.grid(column = 0, row = 2)
    AccountEntry = Entry(LoginWindow)
    AccountEntry.grid(column = 1, row = 1, columnspan = 2)
    PasswordEntry = Entry(LoginWindow, show = "*")
    PasswordEntry.grid(column = 1, row = 2, columnspan = 2)
    LoginButton = Button(LoginWindow, text = "Login", width = 10, command = lambda:verifyUser(LoginWindow, AccountEntry, PasswordEntry))
    LoginButton.grid(column = 1, row = 3)
# 設定按鈕
def Settings():
    def closethewindow():
        SettingsWindow.destroy()
    SettingsWindow = Toplevel(root)
    SettingsWindow.title("Settings")
    WordColor = Button(SettingsWindow, text = "字幕顏色", command = ChooseColor)
    WordColor.grid(row = 0, column = 0)
    language = Button(SettingsWindow, text = "語言", command = ChooseLanguage)
    language.grid(row = 1, column = 0)
    CloseIt = Button(SettingsWindow, text = "退出", command = closethewindow)
    CloseIt.grid(row = 2, column = 0)
# 設定語言
def ChooseLanguage():
    def ChooseChinese():
        pass
    def ChooseEnglish():
        pass
    ChooseLanguageWindow = Toplevel(root)
    ChooseLanguageWindow.title("選擇語言")
    Chinese = Button(ChooseLanguageWindow, text = "繁體中文", command = ChooseChinese)
    Chinese.pack()
    English = Button(ChooseLanguageWindow, text = "英文", command = ChooseEnglish)
    English.pack()
# 設定字幕顏色
def ChooseColor():
    def changecolor(colorHex):
        Login["fg"] = colorHex
        Settings["fg"] = colorHex
        Storehouse["fg"] = colorHex
        BestGroup["fg"] = colorHex
        LongestGroup["fg"] = colorHex
        RecentGroup["fg"] = colorHex
        Chinese["fg"] = colorHex
        English["fg"] = colorHex
        ChooseColorWindow.destroy()
    def getValue(e):
        # 取得RGB
        R = int(Red.get())
        G = int(Green.get())
        B = int(Blue.get())
        # 數值轉換為16進位
        hex = "#{:02x}{:02x}{:02x}".format (R, G, B)
        # 分別設定 Label 文字內容
        RedColor["text"] = "R: "+str(Red.get)
        GreenColor["text"] = "R: "+str(Green.get)
        BlueColor["text"] = "R: "+str(Blue.get)
        # 分別設定 statusBar1 背景
        color["bg"] = hex
        color["text"] = hex
    global ChooseColor
    global SettingsWindow
    ChooseColorWindow = Toplevel(root)
    ChooseColorWindow.title("選擇顏色")
    # 建立 title label
    title = Label(ChooseColorWindow, text = "選擇顏色(R,G,B)")
    # 加入視窗
    title.grid(row = 0, column = 0)
    # 建立字串變數
    value1 = StringVar()
    value1.set("R: 0")
    # 建立 Label(Red)
    RedColor = Label(ChooseColorWindow, textvariable = value1, fg = "black", anchor = W, relief = "sunken", bd = 2)
    RedColor.grid(row = 1, column = 0, columnspan = 3, sticky = W+E+S)
    # 建立 Scale(Red) 元件
    Red = Scale (ChooseColorWindow, from_ = 0, to = 255, orient = "horizontal", resolution = 1, length = 300, showvalue = True, command = getValue)
    Red.grid(row = 2, column = 0, columnspan = 3)
    # 建立字串變數
    value2 = StringVar()
    value2.set("G: 0")
    # 建立 Label(Green)
    GreenColor = Label(ChooseColorWindow, textvariable = value2, fg = "black", anchor = W, relief = "sunken", bd = 2)
    GreenColor.grid(row = 3, column = 0, columnspan = 3, sticky = W+E+S)
    # 建立 Scale(Green) 元件
    Green = Scale(ChooseColorWindow, from_ = 0, to = 255, orient = "horizontal", resolution = 1, length = 300, showvalue = True, command = getValue)
    Green.grid(row = 4, column = 0, columnspan = 3)
    # 建立字串變數
    value3 = StringVar()
    value3.set("B: 0")
    # 建立 Label(Blue)
    BlueColor = Label(ChooseColorWindow, textvariable = value3, fg = "black", anchor = W, relief = "sunken", bd = 2)
    BlueColor.grid(row = 5, column = 0, columnspan = 3, sticky = W+E+S)
    # 建立 Scale(Blue) 元件
    Blue = Scale(ChooseColorWindow, from_ = 0, to = 255, orient = "horizontal", resolution = 1, length = 300, showvalue = True, command = getValue)
    Blue.grid(row = 6, column = 0, columnspan = 3)
    # 顏色的label
    color = Label(ChooseColorWindow, text = "", fg = "white", bg = "white", relief = "sunken", bd = 2, font = (20), anchor = "center")
    color.grid(row = 7, column = 0, columnspan = 3, sticky = W+E+S)
    # 確定更改顏色的按鈕
    confirm = Button(ChooseColorWindow, text = "確定", fg = "black", command = lambda:changecolor(color["text"]))
    confirm.grid(row = 8, column = 0, columnspan = 3, sticky = W+E+S)
# 遊戲庫
def Storehouse():
    StorehouseWindow = Toplevel(root)
    StorehouseWindow.title("storehouse")
    Wait = Label(StorehouseWindow, text = "敬請期待!")
    Wait.pack()
# 類別左右方向鍵
def BestLeft():
    BestRightButton["state"] = ACTIVE
    # 把它變全域變數
    global BestMiddle
    global BestGames
    # 將中心點在所有遊戲中向右移一個
    BestMiddle -=1
    # 圖片1
    BestPicture1 = PILIMAGE.open(BestGames[BestMiddle-2])
    BestPicture1 = BestPicture1.resize((150, 150))
    global img_tk0
    img_tk0 = PILImageTK.PhotoImage(BestPicture1)
    BestButton1["image"] = img_tk0
    # 圖片2
    BestPicture2 = PILIMAGE.open(BestGames[BestMiddle-1])
    BestPicture2 = BestPicture2.resize((150, 150))
    global img_tk1
    img_tk1 = PILImageTK.PhotoImage(BestPicture2)
    BestButton2["image"] = img_tk1
    # 圖片3
    BestPicture3 = PILIMAGE.open(BestGames[BestMiddle])
    BestPicture3 = BestPicture3.resize((150, 150))
    global img_tk3
    img_tk3 = PILImageTK.PhotoImage(BestPicture3)
    BestButton3["image"] = img_tk3
    # 圖片4
    BestPicture4 = PILIMAGE.open(BestGames[BestMiddle+1])
    BestPicture4 = BestPicture4.resize((150, 150))
    global img_tk4
    img_tk4 = PILImageTK.PhotoImage(BestPicture4)
    BestButton4["image"] = img_tk4
    # 圖片5
    BestPicture5 = PILIMAGE.open(BestGames[BestMiddle+2])
    BestPicture5 = BestPicture5.resize((150, 150))
    global img_tk5
    img_tk5 = PILImageTK.PhotoImage(BestPicture5)
    BestButton5["image"] = img_tk5
    if BestMiddle == 2:
        BestLeftButton["state"] = DISABLED
def RecentLeft():
    print("hi")
def LongestLeft():
    print("hi")
def BestRight():
    BestLeftButton["state"] = ACTIVE
    # 把它變全域變數
    global BestMiddle
    global BestGames
    # 將中心點在所有遊戲中向右移一個
    BestMiddle +=1
    # 圖片1
    BestPicture1 = PILIMAGE.open(BestGames[BestMiddle-2])
    BestPicture1 = BestPicture1.resize((150, 150))
    global img_tk0
    img_tk0 = PILImageTK.PhotoImage(BestPicture1)
    BestButton1["image"] = img_tk0
    # 圖片2
    BestPicture2 = PILIMAGE.open(BestGames[BestMiddle-1])
    BestPicture2 = BestPicture2.resize((150, 150))
    global img_tk1
    img_tk1 = PILImageTK.PhotoImage(BestPicture2)
    BestButton2["image"] = img_tk1
    # 圖片3
    BestPicture3 = PILIMAGE.open(BestGames[BestMiddle])
    BestPicture3 = BestPicture3.resize((150, 150))
    global img_tk3
    img_tk3 = PILImageTK.PhotoImage(BestPicture3)
    BestButton3["image"] = img_tk3
    # 圖片4
    BestPicture4 = PILIMAGE.open(BestGames[BestMiddle+1])
    BestPicture4 = BestPicture4.resize((150, 150))
    global img_tk4
    img_tk4 = PILImageTK.PhotoImage(BestPicture4)
    BestButton4["image"] = img_tk4
    # 圖片5
    BestPicture5 = PILIMAGE.open(BestGames[BestMiddle+2])
    BestPicture5 = BestPicture5.resize((150, 150))
    global img_tk5
    img_tk5 = PILImageTK.PhotoImage(BestPicture5)
    BestButton5["image"] = img_tk5
    BestRightStop = (len(BestGames)-3)
    if BestMiddle == BestRightStop:
        BestRightButton["state"] = DISABLED
def RecentRight():
    print("hi")
def LongestRight():
    print("hi")
# 遊戲資訊
# 傳說對決
def AOVinfo():
    AOVinfoWindows = Toplevel(root)
    AOVinfoWindows.title("傳說對決")
    AOVinfoWindows.mainloop()
# 荒野亂鬥
def BSinfo():
    BSinfoWindows = Toplevel(root)
    BSinfoWindows.title("荒野亂鬥")
    BSinfoWindows.mainloop() 
# 創世神
def MCinfo():
    MCinfoWindows = Toplevel(root)
    MCinfoWindows.title("創世神")
    MCinfoWindows.mainloop()
# 機械磚塊
def Robloxinfo():
    RobloxinfoWindows = Toplevel(root)
    RobloxinfoWindows.title("機械磚塊")
    RobloxinfoWindows.mainloop()
# Fornite
def Forniteinfo():
    ForniteinfoWindows = Toplevel(root)
    ForniteinfoWindows.title("Fornite")
    ForniteinfoWindows.mainloop()
# Valorant
def Valorantinfo():
    ValorantinfoWindows = Toplevel(root)
    ValorantinfoWindows.title("Valorant")
    ValorantinfoWindows.mainloop()
# Mech Arena
def MechArenainfo():
    MechArenainfoWindows = Toplevel(root)
    MechArenainfoWindows.title("MechArena")
    MechArenainfoWindows.mainloop()
# 三種遊戲類別(我的最愛, 最近新增, 遊玩最久)
BestGroup = Label(root, text = "我的最愛", font = ("Arial", 13, "bold"))
RecentGroup = Label(root, text = "最近新增", font = ("Arial", 13, "bold"))
LongestGroup = Label(root, text = "遊玩最久", font = ("Arial", 13, "bold"))
BestGroup.grid(row = 0, column = 0, rowspan = 2)
RecentGroup.grid(row = 2, column = 0, rowspan = 2,)   
LongestGroup.grid(row = 4, column = 0, rowspan = 2)
# 遊戲類別中的左右選擇鍵
BestLeftButton = Button(root, text = "<", font = ("Arial", 13, "bold"), command = BestLeft)
BestLeftButton["state"] = DISABLED
RecentLeftButton = Button(root, text = "<", font = ("Arial", 13, "bold"), command = RecentLeft)
RecentLeftButton["state"] = DISABLED
LongestLeftButton = Button(root, text = "<", font = ("Arial", 13, "bold"), command = LongestLeft)
LongestLeftButton["state"] = DISABLED
BestRightButton = Button(root, text = ">", font = ("Arial", 13, "bold"), command = BestRight)
RecentRightButton = Button(root, text = ">", font = ("Arial", 13, "bold"), command = RecentRight)
LongestRightButton = Button(root, text = ">", font = ("Arial", 13, "bold"), command = LongestRight)
BestLeftButton.grid(row = 0, column = 1, rowspan = 2)
RecentLeftButton.grid(row = 2, column = 1, rowspan = 2)
LongestLeftButton.grid(row = 4, column = 1, rowspan = 2)
BestRightButton.grid(row = 0, column = 7, rowspan = 2)
RecentRightButton.grid(row = 2, column = 7, rowspan = 2)
LongestRightButton.grid(row = 4, column = 7, rowspan = 2)
# 帳戶資訊
Login = Button(root, text = "登入/註冊", font = ("Arial", 13, "bold"), command = Login)
Login.grid(row = 6, column = 2)
# 設定
Settings = Button(root, text = "遊戲設定", font = ("Arial", 13, "bold"), command = Settings)
Settings.grid(row = 6, column = 4)
# 遊戲庫
Storehouse = Button(root, text = "我的遊戲庫", font = ("Arial", 13, "bold"), command = Storehouse)
Storehouse.grid(row = 6, column = 6)
# 我的最愛-五個架上遊戲
# 圖片1
BestPicture1 = PILIMAGE.open(BestGames[BestMiddle-2])
BestPicture1 = BestPicture1.resize((150, 150))
BestPicture1 = PILImageTK.PhotoImage(BestPicture1)
BestButton1 = Button(root, image = BestPicture1, width = 150, height = 150, command = AOVinfo)
BestButton1["image"] = BestPicture1
BestButton1.grid(row = 0, column = 2, rowspan = 2)
# 圖片2
BestPicture2 = PILIMAGE.open(BestGames[BestMiddle-1])
BestPicture2 = BestPicture2.resize((150, 150))
BestPicture2 = PILImageTK.PhotoImage(BestPicture2)
BestButton2 = Button(root, image = BestPicture2, width = 150, height = 150, command = AOVinfo)
BestButton2["image"] = BestPicture2
BestButton2.grid(row = 0, column = 3, rowspan = 2)
# 圖片3
BestPicture3 = PILIMAGE.open(BestGames[BestMiddle])
BestPicture3 = BestPicture3.resize((150, 150))
BestPicture3 = PILImageTK.PhotoImage(BestPicture3)
BestButton3 = Button(root, image = BestPicture3, width = 150, height = 150, command = AOVinfo)
BestButton3["image"] = BestPicture3
BestButton3.grid(row = 0, column = 4, rowspan = 2)
# 圖片4
BestPicture4 = PILIMAGE.open(BestGames[BestMiddle+1])
BestPicture4 = BestPicture4.resize((150, 150))
BestPicture4 = PILImageTK.PhotoImage(BestPicture4)
BestButton4 = Button(root, image = BestPicture4, width = 150, height = 150, command = AOVinfo)
BestButton4["image"] = BestPicture4
BestButton4.grid(row = 0, column = 5, rowspan = 2)
# 圖片5
BestPicture5 = PILIMAGE.open(BestGames[BestMiddle+2])
BestPicture5 = BestPicture5.resize((150, 150))
BestPicture5 = PILImageTK.PhotoImage(BestPicture5)
BestButton5 = Button(root, image = BestPicture5, width = 150, height = 150, command = AOVinfo)
BestButton5["image"] = BestPicture5
BestButton5.grid(row = 0, column = 6, rowspan = 2)
# 遊戲
# 傳說對決
AOVimg = PILIMAGE.open("project/img/AOV.jpg")
AOVimg = AOVimg.resize((150, 150))
AOVimg = PILImageTK.PhotoImage(AOVimg)
AOVbutton = Button(root, image = AOVimg, width = 150, height = 150, command = AOVinfo)
# 荒野亂鬥
BSimg = PILIMAGE.open("project/img/brawl.png")
BSimg = BSimg.resize((150, 150))
BSimg = PILImageTK.PhotoImage(BSimg)
BSbutton = Button(root, image = BSimg, width = 150, height = 150, command = BSinfo)
# 創世神
MCimg = PILIMAGE.open("project/img/mc.jpg")
MCimg = MCimg.resize((150, 150))
MCimg = PILImageTK.PhotoImage(MCimg)
MCbutton = Button(root, image = MCimg, width = 150, height = 150, command = MCinfo)
# 機械磚塊
Robloximg = PILIMAGE.open("project/img/roblox.jpg")
Robloximg = Robloximg.resize((150, 150))
Robloximg = PILImageTK.PhotoImage(Robloximg)
Robloxbutton = Button(root, image = Robloximg, width = 150, height = 150, command = Robloxinfo)
# Fornite
Forniteimg = PILIMAGE.open("project/img/Fornite.jpg")
Forniteimg = Forniteimg.resize((150, 150))
Forniteimg = PILImageTK.PhotoImage(Forniteimg)
Fornitebutton = Button(root, image = Forniteimg, width = 150, height = 150, command = Forniteinfo)
# Valorant
Valorantimg = PILIMAGE.open("project/img/Valorant.jpg")
Valorantimg = Valorantimg.resize((150, 150))
Valorantimg = PILImageTK.PhotoImage(Valorantimg)
Valorantbutton = Button(root, image = Valorantimg, width = 150, height = 150, command = Valorantinfo)
# Mech Arena
MechArenaimg = PILIMAGE.open("project/img/Mech Arena.jpg")
MechArenaimg = MechArenaimg.resize((150, 150))
MechArenaimg = PILImageTK.PhotoImage(MechArenaimg)
MechArenabutton = Button(root, image = MechArenaimg, width = 150, height = 150, command = MechArenainfo)

root.mainloop()