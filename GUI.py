#creating label
from tkinter import *

window = Tk()

label_1 = Label(window, text = "hello world", font = 5, bg = "green", fg = "red", width = 10, height = 2)
label_1.pack()
label_1.place(x = 5, y = 5)

lablel_2 = Label(window, text = "Hi", font = 3, bg = "green", fg = "black", highlightcolor = "black",
                 width = 10, height = 2)
lablel_2.pack()
lablel_2.place(x = 5, y = 50)

label_3 = Label(window, text = "Christian Mayol Aribal", font = 7, bg = "yellow", fg = "blue", width = 20,
                height = 1)
label_3.pack()

#label_1.grid(row = 0, column = 1)

window.mainloop()
