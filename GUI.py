#creating label
import tkinter as tk
from tkinter import *

window = Tk()
window.title("Personal information")
window.minsize(width=400, height=400)
#window.maxsize(width=1360, height=680)

label_1 = Label(window, text = "hello world", fg = "black", bg = "yellow", width = 15, height = 2, font=('Times New Roman', 40, 'bold'))
label_1.pack()
#label_1.place(x = 5, y = 5)
lable_2 = Label(window, text = "This is my first time to create a Graphical user interface label sample", fg = "green", width = 52, height = 2, highlightcolor = "black", font=(25))
# lablel_2.pack()
lable_2.place(x = 5, y = 150)
#
label_3 = Label(window, text = "Label", fg = "black", bg = "blue", width = 10, height = 2, highlightcolor = "black", font = (25))
label_3.place(x = 1, y = 111)


#
# label_3 = Label(window, text = "Christian Mayol Aribal", font = 7, bg = "yellow", fg = "blue", width = 20, height = 1)
# label_3.pack()

#label_1.grid(row = 0, column = 1)

window.mainloop()
