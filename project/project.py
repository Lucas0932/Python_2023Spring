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

#創建三個存放遊戲的list
BestGames = ["project/img/AOV.jpg", "project/img/brawl.png", "project/img/mc.jpg", "project/img/roblox.jpg", 'project/img/Fornite.jpg', "project/img/Valorant.jpg", "project/img/Mech Arena.jpg"]
RecentGames = ["project/img/CallOfDuty.png", "project/img/LOL.jfif", "project/img/LuigisMansion.jpg", "project/img/Mariooo.jpeg", "project/img/OverCook.jpg", "project/img/Pubg.png", "project/img/Splatoon3.jfif", "project/img/zelda.jfif"]
LongestGame = ["project/img/fall guys.jfif", "project/img/mario.jpg"]
BestGameInfo = ["AOVinfo", "BSinfo", "MCinfo", "Robloxinfo", "Forniteinfo", "Valorantinfo", "MechArenainfo"]
languagedata = {"Chinese" : ["我的最愛", "最近新增", "遊玩最久", "登入/註冊", "遊戲設定", "我的遊戲庫", "字幕顏色", "語言", "退出", "帳戶登入", "帳號", "密碼", "登入", "繁體中文", "英文", "敬請期待!"], "English" : ["My Favorite", "Recent Add", "Played Longest", "Login/Sign Up", "Game Settings", "My Games Storehouse", "Word Color", "Language", "Go Back", "User Login", "Account", "Password", "Login", "Chinese", "English", "Stay Tuned!"]}
language = "Chinese"

# 創建三個類別的中心點
BestMiddle = 2
RecentMiddle = 2
LongestMiddle = 2

# 登入按鈕
def Login():
    global language
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
    UserLogin = Label(LoginWindow, text = languagedata[language][9])
    UserLogin.grid(column = 1, row = 0)
    Account = Label(LoginWindow, text = languagedata[language][10])
    Account.grid(column = 0, row = 1)
    Password = Label(LoginWindow, text = languagedata[language][11])
    Password.grid(column = 0, row = 2)
    AccountEntry = Entry(LoginWindow)
    AccountEntry.grid(column = 1, row = 1, columnspan = 2)
    PasswordEntry = Entry(LoginWindow, show = "*")
    PasswordEntry.grid(column = 1, row = 2, columnspan = 2)
    LoginButton = Button(LoginWindow, text = languagedata[language][12], width = 10, command = lambda:verifyUser(LoginWindow, AccountEntry, PasswordEntry))
    LoginButton.grid(column = 1, row = 3)


# 設定按鈕
def Settings():
    global language
    def closethewindow():
        SettingsWindow.destroy()
    SettingsWindow = Toplevel(root)
    SettingsWindow.title("Settings")
    WordColor = Button(SettingsWindow, text = languagedata[language][6], command = ChooseColor)
    WordColor.grid(row = 0, column = 0)
    llanguage = Button(SettingsWindow, text = languagedata[language][7], command = ChooseLanguage)
    llanguage.grid(row = 1, column = 0)
    CloseIt = Button(SettingsWindow, text = languagedata[language][8], command = closethewindow)
    CloseIt.grid(row = 2, column = 0)


# 設定語言
def ChooseLanguage():
    def ChooseChinese():
        global language
        global WordColor
        global llanguage
        global CloseIt
        global UserLogin
        global Account
        global Password
        global LoginButton
        language = "Chinese"
        BestGroup["text"] = languagedata[language][0]
        RecentGroup["text"] = languagedata[language][1]
        LongestGroup["text"] = languagedata[language][2]
        Login["text"] = languagedata[language][3]
        Settings["text"] = languagedata[language][4]
        Storehouse["text"] = languagedata[language][5]
        WordColor["text"] = languagedata[language][6]
        llanguage["text"] = languagedata[language][7]
        CloseIt["text"] = languagedata[language][8]
        UserLogin["text"] = languagedata[language][9]
        Account["text"] = languagedata[language][10]
        Password["text"] = languagedata[language][11]
        LoginButton["text"] = languagedata[language][12]
        ChooseLanguageWindow.destroy()
    def ChooseEnglish():
        global language
        global WordColor
        global llanguage
        global CloseIt
        global UserLogin
        global Account
        global Password
        global LoginButton
        language = "English"
        BestGroup["text"] = languagedata[language][0]
        RecentGroup["text"] = languagedata[language][1]
        LongestGroup["text"] = languagedata[language][2]
        Login["text"] = languagedata[language][3] 
        Settings["text"] = languagedata[language][4]
        Storehouse["text"] = languagedata[language][5]
        WordColor["text"] = languagedata[language][6]
        llanguage["text"] = languagedata[language][7]
        CloseIt["text"] = languagedata[language][8]
        UserLogin["text"] = languagedata[language][9]
        Account["text"] = languagedata[language][10]
        Password["text"] = languagedata[language][11]
        LoginButton["text"] = languagedata[language][12]
        ChooseLanguageWindow.destroy()
    ChooseLanguageWindow = Toplevel(root)
    ChooseLanguageWindow.title("選擇語言")
    Chinese = Button(ChooseLanguageWindow, text = "繁體中文", command = ChooseChinese)
    Chinese.pack()
    English = Button(ChooseLanguageWindow, text = "英文", command = ChooseEnglish)
    English.pack()


# 設定字幕顏色
def ChooseColor():
    def changecolor(colorHex):
        global Chinese
        Login["fg"] = colorHex
        Settings["fg"] = colorHex
        Storehouse["fg"] = colorHex
        BestGroup["fg"] = colorHex
        LongestGroup["fg"] = colorHex
        RecentGroup["fg"] = colorHex
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
    RecentRightButton["state"] = ACTIVE
    # 把它變全域變數
    global RecentMiddle
    global RecentGames
    # 將中心點在所有遊戲中向右移一個
    RecentMiddle -=1
    # 圖片1
    RecentPicture1 = PILIMAGE.open(RecentGames[RecentMiddle-2])
    RecentPicture1 = RecentPicture1.resize((150, 150))
    global img_tkk0
    img_tkk0 = PILImageTK.PhotoImage(RecentPicture1)
    RecentButton1["image"] = img_tkk0
    # 圖片2
    RecentPicture2 = PILIMAGE.open(RecentGames[RecentMiddle-1])
    RecentPicture2 = RecentPicture2.resize((150, 150))
    global img_tkk1
    img_tkk1 = PILImageTK.PhotoImage(RecentPicture2)
    RecentButton2["image"] = img_tkk1
    # 圖片3
    RecentPicture3 = PILIMAGE.open(RecentGames[RecentMiddle])
    RecentPicture3 = RecentPicture3.resize((150, 150))
    global img_tkk3
    img_tkk3 = PILImageTK.PhotoImage(RecentPicture3)
    RecentButton3["image"] = img_tkk3
    # 圖片4
    RecentPicture4 = PILIMAGE.open(RecentGames[RecentMiddle+1])
    RecentPicture4 = RecentPicture4.resize((150, 150))
    global img_tkk4
    img_tkk4 = PILImageTK.PhotoImage(RecentPicture4)
    RecentButton4["image"] = img_tkk4
    # 圖片5
    RecentPicture5 = PILIMAGE.open(RecentGames[RecentMiddle+2])
    RecentPicture5 = RecentPicture5.resize((150, 150))
    global img_tkk5
    img_tkk5 = PILImageTK.PhotoImage(RecentPicture5)
    RecentButton5["image"] = img_tkk5
    if RecentMiddle == 2:
        RecentLeftButton["state"] = DISABLED
def LongestLeft():
    LongestRightButton["state"] = ACTIVE
    # 把它變全域變數
    global LongestMiddle
    global LongestGames
    # 將中心點在所有遊戲中向右移一個
    LongestMiddle -=1
    # 圖片1
    LongestPicture1 = PILIMAGE.open(LongestGames[LongestMiddle-2])
    LongestPicture1 = LongestPicture1.resize((150, 150))
    global img_tkkk0
    img_tkkk0 = PILImageTK.PhotoImage(LongestPicture1)
    LongestButton1["image"] = img_tkkk0
    # 圖片2
    LongestPicture2 = PILIMAGE.open(LongestGames[LongestMiddle-1])
    LongestPicture2 = LongestPicture2.resize((150, 150))
    global img_tkkk1
    img_tkkk1 = PILImageTK.PhotoImage(LongestPicture2)
    LongestButton2["image"] = img_tkkk1
    # 圖片3
    LongestPicture3 = PILIMAGE.open(LongestGames[LongestMiddle])
    LongestPicture3 = LongestPicture3.resize((150, 150))
    global img_tkkk3
    img_tkkk3 = PILImageTK.PhotoImage(LongestPicture3)
    LongestButton3["image"] = img_tkkk3
    # 圖片4
    LongestPicture4 = PILIMAGE.open(LongestGames[LongestMiddle])
    LongestPicture4 = LongestPicture4.resize((150, 150))
    global img_tkkk4
    img_tkkk4 = PILImageTK.PhotoImage(LongestPicture3)
    LongestButton4["image"] = img_tkkk4
    # 圖片5
    LongestPicture5 = PILIMAGE.open(LongestGames[LongestMiddle])
    LongestPicture5 = LongestPicture5.resize((150, 150))
    global img_tkkk5
    img_tkkk5 = PILImageTK.PhotoImage(LongestPicture3)
    LongestButton5["image"] = img_tkkk5
    if LongestMiddle == 2:
        LongestLeftButton["state"] = DISABLED
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
    RecentLeftButton["state"] = ACTIVE
    # 把它變全域變數
    global RecentMiddle
    global RecentGames
    # 將中心點在所有遊戲中向右移一個
    RecentMiddle +=1
    # 圖片1
    RecentPicture1 = PILIMAGE.open(RecentGames[RecentMiddle-2])
    RecentPicture1 = RecentPicture1.resize((150, 150))
    global img_tkk0
    img_tkk0 = PILImageTK.PhotoImage(RecentPicture1)
    RecentButton1["image"] = img_tkk0
    # 圖片2
    RecentPicture2 = PILIMAGE.open(RecentGames[RecentMiddle-1])
    RecentPicture2 = RecentPicture2.resize((150, 150))
    global img_tkk1
    img_tkk1 = PILImageTK.PhotoImage(RecentPicture2)
    RecentButton2["image"] = img_tkk1
    # 圖片3
    RecentPicture3 = PILIMAGE.open(RecentGames[RecentMiddle])
    RecentPicture3 = RecentPicture3.resize((150, 150))
    global img_tkk3
    img_tkk3 = PILImageTK.PhotoImage(RecentPicture3)
    RecentButton3["image"] = img_tkk3
    # 圖片4
    RecentPicture4 = PILIMAGE.open(RecentGames[RecentMiddle+1])
    RecentPicture4 = RecentPicture4.resize((150, 150))
    global img_tkk4
    img_tkk4 = PILImageTK.PhotoImage(RecentPicture4)
    RecentButton4["image"] = img_tkk4
    # 圖片5
    RecentPicture5 = PILIMAGE.open(RecentGames[RecentMiddle+2])
    RecentPicture5 = RecentPicture5.resize((150, 150))
    global img_tkk5
    img_tkk5 = PILImageTK.PhotoImage(RecentPicture5)
    RecentButton5["image"] = img_tkk5
    RecentRightStop = (len(RecentGames)-3)
    if RecentMiddle == RecentRightStop:
        RecentRightButton["state"] = DISABLED
def LongestRight():
    LongestLeftButton["state"] = ACTIVE
    # 把它變全域變數
    global LongestMiddle
    global LongestGames
    # 將中心點在所有遊戲中向右移一個
    LongestMiddle +=1
    # 圖片1
    LongestPicture1 = PILIMAGE.open(LongestGames[LongestMiddle-2])
    LongestPicture1 = LongestPicture1.resize((150, 150))
    global img_tkkk0
    img_tkkk0 = PILImageTK.PhotoImage(LongestPicture1)
    LongestButton1["image"] = img_tkkk0
    # 圖片2
    LongestPicture2 = PILIMAGE.open(LongestGames[LongestMiddle-1])
    LongestPicture2 = LongestPicture2.resize((150, 150))
    global img_tkkk1
    img_tkkk1 = PILImageTK.PhotoImage(LongestPicture2)
    LongestButton2["image"] = img_tkkk1
    # 圖片3
    LongestPicture3 = PILIMAGE.open(LongestGames[LongestMiddle])
    LongestPicture3 = LongestPicture3.resize((150, 150))
    global img_tkkk3
    img_tkkk3 = PILImageTK.PhotoImage(LongestPicture3)
    LongestButton3["image"] = img_tkkk3
    # 圖片4
    LongestPicture4 = PILIMAGE.open(LongestGames[LongestMiddle])
    LongestPicture4 = LongestPicture4.resize((150, 150))
    global img_tkkk4
    img_tkkk4 = PILImageTK.PhotoImage(LongestPicture3)
    LongestButton4["image"] = img_tkkk4
    # 圖片5
    LongestPicture5 = PILIMAGE.open(LongestGames[LongestMiddle])
    LongestPicture5 = LongestPicture5.resize((150, 150))
    global img_tkkk5
    img_tkkk5 = PILImageTK.PhotoImage(LongestPicture3)
    LongestButton5["image"] = img_tkkk5
    LongestRightStop = (len(LongestGames)-3)
    if LongestMiddle == LongestRightStop:
        LongestRightButton["state"] = DISABLED


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
# Fall Guys
def FallGuysinfo():
    FallGuysinfoWindows = Toplevel(root)
    FallGuysinfoWindows.title("Fall Guys")
    FallGuysinfoWindows.mainloop()
# Mario
def Marioinfo():
    MarioinfoWindows = Toplevel(root)
    MarioinfoWindows.title("Mario")
    MarioinfoWindows.mainloop()
# Zelda
def Zeldainfo():
    ZeldainfoWindows = Toplevel(root)
    ZeldainfoWindows.title("Zelda")
    ZeldainfoWindows.mainloop()
# CallOfDuty
def CallOfDutyinfo():
    CallOfDutyinfoWindows = Toplevel(root)
    CallOfDutyinfoWindows.title("Call Of Duty")
    CallOfDutyinfoWindows.mainloop()
# LoL
def LoLinfo():
    LoLinfoWindows = Toplevel(root)
    LoLinfoWindows.title("LoL")
    LoLinfoWindows.mainloop()
# LuigisMansion
def LuigisMansioninfo():
    LuigisMansioninfoWindows = Toplevel(root)
    LuigisMansioninfoWindows.title("Luigi's Mansion")
    LuigisMansioninfoWindows.mainloop()
# SuperSmashBros
def SuperSmashBrosinfo():
    SuperSmashBrosinfoWindows = Toplevel(root)
    SuperSmashBrosinfoWindows.title("Super Smash Bros")
    SuperSmashBrosinfoWindows.mainloop()
# OverCook
def OverCookinfo():
    OverCookinfoWindows = Toplevel(root)
    OverCookinfoWindows.title("OverCook")
    OverCookinfoWindows.mainloop()
# Splatoon 3
def Splatoon3info():
    Splatoon3infoWindows = Toplevel(root)
    Splatoon3infoWindows.title("Splatoon 3")
    Splatoon3infoWindows.mainloop()
# Overcook
def Overcookinfo():
    OvercookinfoWindows = Toplevel(root)
    OvercookinfoWindows.title("Overcook")
    OvercookinfoWindows.mainloop()


# 三種遊戲類別(我的最愛, 最近新增, 遊玩最久)
BestGroup = Label(root, text = languagedata[language][0], font = ("Arial", 13, "bold"))
RecentGroup = Label(root, text = languagedata[language][1], font = ("Arial", 13, "bold"))
LongestGroup = Label(root, text = languagedata[language][2], font = ("Arial", 13, "bold"))
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
if len(BestGames) < 5:
    BestRightButton["state"] = DISABLED
else:
    BestRightButton["state"] = ACTIVE
if len(RecentGames) < 5:
    RecentRightButton["state"] = DISABLED
else:
    RecentRightButton["state"] = ACTIVE
if len(LongestGame) < 5:
    LongestRightButton["state"] = DISABLED
else:
    LongestRightButton["state"] = ACTIVE
BestLeftButton.grid(row = 0, column = 1, rowspan = 2)
RecentLeftButton.grid(row = 2, column = 1, rowspan = 2)
LongestLeftButton.grid(row = 4, column = 1, rowspan = 2)
BestRightButton.grid(row = 0, column = 7, rowspan = 2)
RecentRightButton.grid(row = 2, column = 7, rowspan = 2)
LongestRightButton.grid(row = 4, column = 7, rowspan = 2)


# 帳戶資訊
Login = Button(root, text = languagedata[language][3], font = ("Arial", 13, "bold"), command = Login)
Login.grid(row = 6, column = 2)
# 設定
Settings = Button(root, text = languagedata[language][4], font = ("Arial", 13, "bold"), command = Settings)
Settings.grid(row = 6, column = 4)
# 遊戲庫
Storehouse = Button(root, text = languagedata[language][5], font = ("Arial", 13, "bold"), command = Storehouse)
Storehouse.grid(row = 6, column = 6)


# 我的最愛-五個架上遊戲
# 圖片1
if len(BestGames) > 0:
    BestPicture1 = PILIMAGE.open(BestGames[BestMiddle-2])
    BestPicture1 = BestPicture1.resize((150, 150))
    BestPicture1 = PILImageTK.PhotoImage(BestPicture1)
    BestButton1 = Label(root, image = BestPicture1, width = 150, height = 150)
    BestButton1["image"] = BestPicture1
    BestButton1.grid(row = 0, column = 2, rowspan = 2)
# 圖片2
if len(BestGames) > 1:
    BestPicture2 = PILIMAGE.open(BestGames[BestMiddle-1])
    BestPicture2 = BestPicture2.resize((150, 150))
    BestPicture2 = PILImageTK.PhotoImage(BestPicture2)
    BestButton2 = Label(root, image = BestPicture2, width = 150, height = 150)
    BestButton2["image"] = BestPicture2
    BestButton2.grid(row = 0, column = 3, rowspan = 2)
# 圖片3
if len(BestGames) > 2:
    BestPicture3 = PILIMAGE.open(BestGames[BestMiddle])
    BestPicture3 = BestPicture3.resize((150, 150))
    BestPicture3 = PILImageTK.PhotoImage(BestPicture3)
    BestButton3 = Label(root, image = BestPicture3, width = 150, height = 150)
    BestButton3["image"] = BestPicture3
    BestButton3.grid(row = 0, column = 4, rowspan = 2)
# 圖片4
if len(BestGames) > 3:
    BestPicture4 = PILIMAGE.open(BestGames[BestMiddle+1])
    BestPicture4 = BestPicture4.resize((150, 150))
    BestPicture4 = PILImageTK.PhotoImage(BestPicture4)
    BestButton4 = Label(root, image = BestPicture4, width = 150, height = 150)
    BestButton4["image"] = BestPicture4
    BestButton4.grid(row = 0, column = 5, rowspan = 2)
# 圖片5
if len(BestGames) > 4:
    BestPicture5 = PILIMAGE.open(BestGames[BestMiddle+2])
    BestPicture5 = BestPicture5.resize((150, 150))
    BestPicture5 = PILImageTK.PhotoImage(BestPicture5)
    BestButton5 = Label(root, image = BestPicture5, width = 150, height = 150)
    BestButton5["image"] = BestPicture5
    BestButton5.grid(row = 0, column = 6, rowspan = 2)


# 遊玩最久-五個架上遊戲
# 圖片1
if len(LongestGame) > 0:
    LongestPicture1 = PILIMAGE.open(LongestGame[LongestMiddle-2])
    LongestPicture1 = LongestPicture1.resize((150, 150))
    LongestPicture1 = PILImageTK.PhotoImage(LongestPicture1)
    LongestButton1 = Label(root, image = LongestPicture1, width = 150, height = 150)
    LongestButton1["image"] = LongestPicture1
    LongestButton1.grid(row = 4, column = 2, rowspan = 2)
# 圖片2
if len(LongestGame) > 1:
    LongestPicture2 = PILIMAGE.open(LongestGame[LongestMiddle-1])
    LongestPicture2 = LongestPicture2.resize((150, 150))
    LongestPicture2 = PILImageTK.PhotoImage(LongestPicture2)
    LongestButton2 = Label(root, image = LongestPicture2, width = 150, height = 150)
    LongestButton2["image"] = LongestPicture2
    LongestButton2.grid(row = 4, column = 3, rowspan = 2)
# 圖片3
if len(LongestGame) > 2:
    LongestPicture3 = PILIMAGE.open(LongestGame[LongestMiddle])
    LongestPicture3 = LongestPicture1.resize((150, 150))
    LongestPicture3 = PILImageTK.PhotoImage(LongestPicture3)
    LongestButton3 = Label(root, image = LongestPicture1, width = 150, height = 150)
    LongestButton3["image"] = LongestPicture3
    LongestButton3.grid(row = 4, column = 2, rowspan = 2)
# 圖片4
if len(LongestGame) > 3:
    LongestPicture4 = PILIMAGE.open(LongestGame[LongestMiddle+1])
    LongestPicture4 = LongestPicture1.resize((150, 150))
    LongestPicture4 = PILImageTK.PhotoImage(LongestPicture4)
    LongestButton4 = Label(root, image = LongestPicture4, width = 150, height = 150)
    LongestButton4["image"] = LongestPicture4
    LongestButton4.grid(row = 4, column = 2, rowspan = 2)
# 圖片5
if len(LongestGame) > 4:
    LongestPicture5 = PILIMAGE.open(LongestGame[LongestMiddle+2])
    LongestPicture5 = LongestPicture1.resize((150, 150))
    LongestPicture5 = PILImageTK.PhotoImage(LongestPicture5)
    LongestButton5 = Label(root, image = LongestPicture5, width = 150, height = 150)
    LongestButton5["image"] = LongestPicture5
    LongestButton5.grid(row = 4, column = 2, rowspan = 2)


# 最近新增-五個架上遊戲
# 圖片1
if len(RecentGames) > 0:
    RecentPicture1 = PILIMAGE.open(RecentGames[RecentMiddle-2])
    RecentPicture1 = RecentPicture1.resize((150, 150))
    RecentPicture1 = PILImageTK.PhotoImage(RecentPicture1)
    RecentButton1 = Label(root, image = RecentPicture1, width = 150, height = 150)
    RecentButton1["image"] = RecentPicture1
    RecentButton1.grid(row = 2, column = 2, rowspan = 2)
# 圖片2
if len(RecentGames) > 1:
    RecentPicture2 = PILIMAGE.open(RecentGames[RecentMiddle-1])
    RecentPicture2 = RecentPicture2.resize((150, 150))
    RecentPicture2 = PILImageTK.PhotoImage(RecentPicture2)
    RecentButton2 = Label(root, image = RecentPicture2, width = 150, height = 150)
    RecentButton2["image"] = RecentPicture2
    RecentButton2.grid(row = 2, column = 3, rowspan = 2)
# 圖片3
if len(RecentGames) > 2:
    RecentPicture3 = PILIMAGE.open(RecentGames[RecentMiddle])
    RecentPicture3 = RecentPicture3.resize((150, 150))
    RecentPicture3 = PILImageTK.PhotoImage(RecentPicture3)
    RecentButton3 = Label(root, image = RecentPicture3, width = 150, height = 150)
    RecentButton3["image"] = RecentPicture3
    RecentButton3.grid(row = 2, column = 4, rowspan = 2)
# 圖片4
if len(RecentGames) > 3:
    RecentPicture4 = PILIMAGE.open(RecentGames[RecentMiddle+1])
    RecentPicture4 = RecentPicture4.resize((150, 150))
    RecentPicture4 = PILImageTK.PhotoImage(RecentPicture4)
    RecentButton4 = Label(root, image = RecentPicture4, width = 150, height = 150)
    RecentButton4["image"] = RecentPicture4
    RecentButton4.grid(row = 2, column = 5, rowspan = 2)
# 圖片5
if len(RecentGames) > 4:
    RecentPicture5 = PILIMAGE.open(RecentGames[RecentMiddle+2])
    RecentPicture5 = RecentPicture5.resize((150, 150))
    RecentPicture5 = PILImageTK.PhotoImage(RecentPicture5)
    RecentButton5 = Label(root, image = RecentPicture5, width = 150, height = 150)
    RecentButton5["image"] = RecentPicture5
    RecentButton5.grid(row = 2, column = 6, rowspan = 2)


#重複執行
root.mainloop()