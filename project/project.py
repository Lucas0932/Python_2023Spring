# 引入 tkinter module
from tkinter import *
# 引入 tkinter.ttk module
import tkinter.ttk as ttk
# 引入 Pillow module
from PIL import Image, ImageTk
# 建立主視窗 Frame
root = Tk()
group1 = Button(root, text = "分類1", font = ("Arial", 13, "bold"))
group1.grid(row = 2, column = 0, rowspan = 2, columnspan = 3, sticky = N+S+W+E, padx = 1)

group2 = Button(root, text = "分類2", font = ("Arial", 13, "bold"))
group2.grid(row = 6, column = 0, rowspan = 2, columnspan = 3, sticky = N+S+W+E, padx = 1)   

group3 = Button(root, text = "分類3", font = ("Arial", 13, "bold"))
group3.grid(row = 8, column = 0, rowspan = 2, columnspan = 3, sticky = N+S+W+E, padx = 1)

game1 = Button(root, text = "game1", font = ("Arial", 13, "bold"))
game1.grid(row = 1, column = 6, columnspan = 4, rowspan = 4)

# MyGames = Button(root, text = "我的遊戲", font = ("Arial", 13, "bold"))
# MyGames.grid(row = 10, columnspan = 2, column = 1)

root.mainloop()




































