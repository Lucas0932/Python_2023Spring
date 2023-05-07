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
# 類別左右方向鍵
def BestLeft():
    print("hi")
def RecentLeft():
    print("hi")
def LongestLeft():
    print("hi")
def BestRight():
    # 把它變全域變數
    global BestMiddle
    BestMiddle +=1
    # 圖片1
    BestPicture1 = PILIMAGE.open(place1)
    BestPicture1 = BestPicture1.resize((150, 150))
    BestPicture1 = PILImageTK.PhotoImage(BestPicture1)
    BestButton1["image"] = BestPicture1
    # 圖片2
    BestPicture2 = PILIMAGE.open(place2)
    BestPicture2 = BestPicture2.resize((150, 150))
    BestPicture2 = PILImageTK.PhotoImage(BestPicture2)
    BestButton2 = Button(root, image = BestPicture2, width = 150, height = 150, command = AOVinfo)
    BestButton2["image"] = BestPicture2
    # 圖片3
    BestPicture3 = PILIMAGE.open(place3)
    BestPicture3 = BestPicture3.resize((150, 150))
    BestPicture3 = PILImageTK.PhotoImage(BestPicture3)
    BestButton3 = Button(root, image = BestPicture3, width = 150, height = 150, command = AOVinfo)
    BestButton3["image"] = BestPicture3
    # 圖片4
    BestPicture4 = PILIMAGE.open(place4)
    BestPicture4 = BestPicture4.resize((150, 150))
    BestPicture4 = PILImageTK.PhotoImage(BestPicture4)
    BestButton4 = Button(root, image = BestPicture4, width = 150, height = 150, command = AOVinfo)
    BestButton4["image"] = BestPicture4
    # 圖片5
    BestPicture5 = PILIMAGE.open(place5)
    BestPicture5 = BestPicture5.resize((150, 150))
    BestPicture5 = PILImageTK.PhotoImage(BestPicture5)
    BestButton5 = Button(root, image = BestPicture5, width = 150, height = 150, command = AOVinfo)
    BestButton5["image"] = BestPicture5
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
# 先創建三個類別的遊戲 list
BestGames = []
RecentGames = []
LongestGames = []
# 創建三個類別的中心點
BestMiddle = 2
RecentMiddle = 2
LongestMiddle = 2
# 我的最愛類別:
BestGames = ["project/img/AOV.jpg", "project/img/brawl.png", "project/img/mc.jpg", "project/img/roblox.jpg", 'project/img/Fornite.jpg', "project/img/Valorant.jpg", "project/img/Mech Arena.jpg"]
# 位置1
place1 = BestGames[BestMiddle-2]
# 位置2
place2 = BestGames[BestMiddle-1]
# 位置3
place3 = BestGames[BestMiddle]
# 位置4
place4 = BestGames[BestMiddle+1]
# 位置5
place5 = BestGames[BestMiddle+2]
# 圖片1
BestPicture1 = PILIMAGE.open(place1)
BestPicture1 = BestPicture1.resize((150, 150))
BestPicture1 = PILImageTK.PhotoImage(BestPicture1)
BestButton1 = Button(root, image = BestPicture1, width = 150, height = 150, command = AOVinfo)
BestButton1.grid(column = 2, row = 0)
# 圖片2
BestPicture2 = PILIMAGE.open(place2)
BestPicture2 = BestPicture2.resize((150, 150))
BestPicture2 = PILImageTK.PhotoImage(BestPicture2)
BestButton2 = Button(root, image = BestPicture2, width = 150, height = 150, command = AOVinfo)
BestButton2.grid(column = 3, row = 0)
# 圖片3
BestPicture3 = PILIMAGE.open(place3)
BestPicture3 = BestPicture3.resize((150, 150))
BestPicture3 = PILImageTK.PhotoImage(BestPicture3)
BestButton3 = Button(root, image = BestPicture3, width = 150, height = 150, command = AOVinfo)
BestButton3.grid(column = 4, row = 0)
# 圖片4
BestPicture4 = PILIMAGE.open(place4)
BestPicture4 = BestPicture4.resize((150, 150))
BestPicture4 = PILImageTK.PhotoImage(BestPicture4)
BestButton4 = Button(root, image = BestPicture4, width = 150, height = 150, command = AOVinfo)
BestButton4.grid(column = 5, row = 0)
# 圖片5
BestPicture5 = PILIMAGE.open(place5)
BestPicture5 = BestPicture5.resize((150, 150))
BestPicture5 = PILImageTK.PhotoImage(BestPicture5)
BestButton5 = Button(root, image = BestPicture5, width = 150, height = 150, command = AOVinfo)
BestButton5.grid(column = 6, row = 0)
# 三種遊戲類別(我的最愛, 最近新增, 遊玩最久)
BestGroup = Label(root, text = "我的最愛", font = ("Arial", 13, "bold"))
RecentGroup = Label(root, text = "最近新增", font = ("Arial", 13, "bold"))
LongestGroup = Label(root, text = "遊玩最久", font = ("Arial", 13, "bold"))
BestGroup.grid(row = 0, column = 0, rowspan = 2)
RecentGroup.grid(row = 2, column = 0, rowspan = 2,)   
LongestGroup.grid(row = 4, column = 0, rowspan = 2)
# 遊戲類別中的左右選擇鍵
BestLeftButton = Button(root, text = "<", font = ("Arial", 13, "bold"), command = BestLeft)
RecentLeftButton = Button(root, text = "<", font = ("Arial", 13, "bold"), command = RecentLeft)
LongestLeftButton = Button(root, text = "<", font = ("Arial", 13, "bold"), command = LongestLeft)
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
Settings = Button(root, text = "遊戲設定", font = ("Arial", 13, "bold"))
Settings.grid(row = 6, column = 4)
# 遊戲庫
Storehouse = Button(root, text = "我的遊戲庫", font = ("Arial", 13, "bold"))
Storehouse.grid(row = 6, column = 6)
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