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
# root.geometry("1000x400")
# 類別左右方向鍵
def BestLeft():
    print("hi")
def RecentLeft():
    print("hi")
def LongestLeft():
    print("hi")
def BestRight():
    print("hi")
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
Login = Button(root, text = "登入/註冊", font = ("Arial", 13, "bold"))
Login.grid(row = 0, column = 8, rowspan = 2)
# 遊戲
# 傳說對決
AOVPlace = 2
AOVLabel = 2
AOVimg = PILIMAGE.open("project/img/AOV.jpg")
AOVimg = AOVimg.resize((150, 150))
AOVimg = PILImageTK.PhotoImage(AOVimg)
AOVbutton = Button(root, image = AOVimg, width = 150, height = 150, command = AOVinfo)
if AOVPlace < 7:
    AOVbutton.grid(row = AOVLabel, column = AOVPlace, rowspan = 2)
# 荒野亂鬥
BSPlace = 3
BSLabel = 2
BSimg = PILIMAGE.open("project/img/brawl.png")
BSimg = BSimg.resize((150, 150))
BSimg = PILImageTK.PhotoImage(BSimg)
BSbutton = Button(root, image = BSimg, width = 150, height = 150, command = BSinfo)
if BSPlace < 7:
    BSbutton.grid(row = BSLabel, column = BSPlace, rowspan = 2)
# 創世神
MCPlace = 4
MCLabel = 2
MCimg = PILIMAGE.open("project/img/mc.jpg")
MCimg = MCimg.resize((150, 150))
MCimg = PILImageTK.PhotoImage(MCimg)
MCbutton = Button(root, image = MCimg, width = 150, height = 150, command = MCinfo)
if MCPlace < 7:
    MCbutton.grid(row = MCLabel, column = MCPlace, rowspan = 2)
# 機械磚塊
RobloxPlace = 5
RobloxLabel = 2
Robloximg = PILIMAGE.open("project/img/roblox.jpg")
Robloximg = Robloximg.resize((150, 150))
Robloximg = PILImageTK.PhotoImage(Robloximg)
Robloxbutton = Button(root, image = Robloximg, width = 150, height = 150, command = Robloxinfo)
if RobloxPlace < 7:
    Robloxbutton.grid(row = RobloxLabel, column = RobloxPlace, rowspan = 2)
# Fornite
FornitePlace = 6
ForniteLabel = 2
Forniteimg = PILIMAGE.open("project/img/Fornite.jpg")
Forniteimg = Forniteimg.resize((150, 150))
Forniteimg = PILImageTK.PhotoImage(Forniteimg)
Fornitebutton = Button(root, image = Forniteimg, width = 150, height = 150, command = Forniteinfo)
if FornitePlace < 7:
    Fornitebutton.grid(row = ForniteLabel, column = FornitePlace, rowspan = 2)
# Valorant
ValorantPlace = 2
ValorantLabel = 4
Valorantimg = PILIMAGE.open("project/img/Valorant.jpg")
Valorantimg = Valorantimg.resize((150, 150))
Valorantimg = PILImageTK.PhotoImage(Valorantimg)
Valorantbutton = Button(root, image = Valorantimg, width = 150, height = 150, command = Valorantinfo)
if ValorantPlace < 7:
    Valorantbutton.grid(row = ValorantLabel, column = ValorantPlace, rowspan = 2)
# Mech Arena
MechArenaPlace = 2
MechArenaLabel = 0
MechArenaimg = PILIMAGE.open("project/img/Mech Arena.jpg")
MechArenaimg = MechArenaimg.resize((150, 150))
MechArenaimg = PILImageTK.PhotoImage(MechArenaimg)
MechArenabutton = Button(root, image = MechArenaimg, width = 150, height = 150, command = MechArenainfo)
if MechArenaPlace < 7:
    MechArenabutton.grid(row = MechArenaLabel, column = MechArenaPlace, rowspan = 2)

root.mainloop()