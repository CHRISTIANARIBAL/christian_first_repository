#creating label
import tkinter as tk
import tkinter
from tkinter import messagebox as msg
from tkinter import *


window = Tk()
window.title("Personal information")
window.minsize(width=800, height=700)
window.maxsize(width=800, height=700)

label_1 = Label(window, text = "hello world", fg = "black", bg = "yellow", width = 15, height = 2, font=('Times New Roman', 40, 'bold'))
label_1.pack()
#label_1.place(x = 5, y = 5)

label_3 = Label(window, text = "Label", fg = "white", bg = "blue", width = 10, height = 2, highlightcolor = "black", font = (25))
label_3.place(x = 1, y = 140)

lable_2 = Label(window, text = "This is my first time to create a Graphical user interface", fg = "green", width = 42, height = 2, highlightcolor = "black", font=(25))
# lablel_2.pack()
lable_2.place(x = 5, y = 190)
#

label_4 = Label(window, text = "option sample", fg = "white", bg = "blue", width = 15, height = 2, highlightcolor = "black", font = (25))
label_4.place(x = 1, y = 250)


#creating_an_option_menu
colors = StringVar(window)
colors.set("COLOURS")

option_colors = OptionMenu(window, colors, "Yellow", "Blue", "Green", "Purple", "Black", "White")
option_colors.place(x = 5, y = 300)

numbers = StringVar(window)
numbers.set("Numbers")

option_numbers = OptionMenu(window, numbers, "one", "two", "three", "four", "five")
option_numbers.place(x = 5, y = 330)

#creating_button_with_label_and_entry_box
variable_1 = StringVar()
def click():
    x = variable_1.get()
    print(x)
    button_click_output.config(text=x, fg="black", bg="yellow")
button_1_label = Label(window, text="enter name", fg="blue", bg="red")
button_1_label.place(x = 280, y = 305)
output_label = Label(window, text="Output:", fg="red")
output_label.place(x=165, y=370)
button_entry = Entry(window, font=("corbel", 10), bd=5, textvariable=variable_1)
button_entry.place(x = 350, y = 303)
button_1 = Button(window, text="Enter", fg="red", bg="green", command=click)
button_1.place(x = 400, y = 330)
button_click_output = Label(window, text="                                              ")
button_click_output.place(x = 215, y = 370)

#creating_list_box
list_box_1_label = Label(window, text=" List box sample ", fg="black", bg="magenta", font=(15))
list_box_1_label.place(x=601, y=225)
list_box_1 = Listbox(window, width=20, height=10)
list_box_1.place(y=250, x=600)
list_1 = ["Red", "White", "Green", "Violet"]
for i in list_1:
    list_box_1.insert(END, i)
def list_button_click():
    list_box_1.delete(ANCHOR)
list_button_1 = Button(window, text="Delete", fg="white", bg="red", font=(15), command=list_button_click)
list_button_1.place(x=633, y=415)
#show_info_message

#msg.showinfo( "Hello Python", "Hello World")


window.mainloop()
