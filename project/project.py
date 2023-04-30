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
root.geometry("1000x200")
# 三種遊戲類別(冒險，戰鬥，生存)
BestGroup = Label(root, text = "我的最愛", font = ("Arial", 13, "bold"))
RecentGroup = Label(root, text = "最近新增", font = ("Arial", 13, "bold"))
LongestGroup = Label(root, text = "遊玩最久", font = ("Arial", 13, "bold"))
BestGroup.grid(row = 0, column = 0, rowspan = 2)
RecentGroup.grid(row = 2, column = 0, rowspan = 2,)   
LongestGroup.grid(row = 4, column = 0, rowspan = 2)
# 遊戲類別中的左右選擇鍵
BestLeftButton = Button(root, text = "<=", font = ("Arial", 13, "bold"), command = BestLeft)
RecentLeftButton = Button(root, text = "<=", font = ("Arial", 13, "bold"), command = RecentLeft)
LongestLeftButton = Button(root, text = "<=", font = ("Arial", 13, "bold"), command = LongestLeft)
BestRightButton = Button(root, text = "=>", font = ("Arial", 13, "bold"), command = BestRight)
RecentRightButton = Button(root, text = "=>", font = ("Arial", 13, "bold"), command = RecentRight)
LongestRightButton = Button(root, text = "=>", font = ("Arial", 13, "bold"), command = LongestRight)
BestLeftButton.grid(row = 0, column = 1, rowspan = 2)
RecentLeftButton.grid(row = 2, column = 1, rowspan = 2)
LongestLeftButton.grid(row = 4, column = 1, rowspan = 2)
BestRightButton.grid(row = 0, column = 6, rowspan = 2)
RecentRightButton.grid(row = 2, column = 6, rowspan = 2)
LongestRightButton.grid(row = 4, column = 6, rowspan = 2)
# 冒險類

# 戰鬥類
# 傳說對決
AOVimg = PILIMAGE.open("project/img/AOV.jpg")
AOVimg = AOVimg.resize((200, 200))
AOVimg = PILImageTK.PhotoImage(AOVimg)
AOVlabel = Button(root, image = AOVimg, width = 200, height = 200)
AOVlabel.grid(row = 2, column = 2, rowspan = 2)
# 荒野亂鬥
BSimg = PILIMAGE.open("project/brawl.png")
BSimg = BSimg.resize((200, 200))
BSimg = PILImageTK.PhotoImage(BSimg)
BSimg = Button(root, image = BSimg, width = 200, height = 200)
BSimg.grid(row = 2, column = 3, rowspan = 2)

# 麥塊
MCimg = PILIMAGE.open("project/mc.jpg")
MCimg = MCimg.resize((100, 100))
MCimg = PILImageTK.PhotoImage(MCimg)
MCimg = Button(root, image = MCimg, width = 100, height = 100)
MCimg.grid(row = 2, column = 4, rowspan = 2)
# 機械磚塊
ROBLOXimg = PILIMAGE.open("project/roblox.jpg")
ROBLOXimg = ROBLOXimg.resize((100, 100))
ROBLOXimg = PILImageTK.PhotoImage(ROBLOXimg)
ROBLOXimg = Button(root, image = ROBLOXimg, width = 100, height = 100)
ROBLOXimg.grid(row = 2, column = 5, rowspan = 2)
# 生存類

# MyGames = Button(root, text = "我的遊戲", font = ("Arial", 13, "bold"))
# MyGames.grid(row = 10, columnspan = 2, column = 1)

root.mainloop()




































