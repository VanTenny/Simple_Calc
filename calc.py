from tkinter import *


root = Tk()
root.title("Simple Calculator")
root.iconbitmap('c:/users/owner/desktop/calculator/icon.ico')

e = Entry(root,width=35, borderwidth=5, fg="white", bg="black")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

my_menu = Menu(root)
root.config(menu=my_menu)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def our_command():
    my_label= label(root, text="you just clicked a dropdown menu!!!!").pack()

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File" ,menu=file_menu)
file_menu.add_command(label="New...", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit" ,menu=edit_menu)
edit_menu.add_command(label="Cut", command=our_command)
edit_menu.add_separator
edit_menu.add_command(label="Copy",command=our_command)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)+ str(number))
    return

def button_clear():
    e.delete(0,END)
    
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num= int(first_number)
    e.delete(0,END)
    
def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num= int(first_number)
    e.delete(0,END)
    
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num= int(first_number)
    e.delete(0,END)
    
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num= int(first_number)
    e.delete(0,END)
    
    
def button_equal():
    second_number = e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0,f_num + int(second_number))

    if math == "subtraction":
        e.insert(0,f_num - int(second_number))

    if math == "multiplication":
        e.insert(0,f_num * int(second_number))

    if math == "division":
        e.insert(0,f_num / int(second_number))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Define Buttons

button_1 = Button(root,text="1", padx=40, pady=20, command=lambda: button_click(1), fg= "white", bg = "gray47")
button_2 = Button(root,text="2", padx=40, pady=20, command=lambda: button_click(2), fg= "white", bg = "gray47")
button_3= Button(root,text="3", padx=40, pady=20, command=lambda: button_click(3), fg= "white", bg = "gray47")
button_4 = Button(root,text="4", padx=40, pady=20, command=lambda: button_click(4), fg= "white", bg = "gray47")
button_5 = Button(root,text="5", padx=40, pady=20, command=lambda: button_click(5), fg= "white", bg = "gray47")
button_6= Button(root,text="6", padx=40, pady=20, command=lambda: button_click(6), fg= "white", bg = "gray47")
button_7 = Button(root,text="7", padx=40, pady=20, command=lambda: button_click(7), fg= "white", bg = "gray47")
button_8 = Button(root,text="8", padx=40, pady=20, command=lambda: button_click(8), fg= "white", bg = "gray47")
button_9 = Button(root,text="9", padx=40, pady=20, command=lambda: button_click(9), fg= "white", bg = "gray47")
button_0 = Button(root,text="0", padx=40, pady=20, command=lambda: button_click(0), fg= "white", bg = "gray47")

button_add = Button(root,text="+", padx=39, pady=20, command= button_add, fg= "white", bg = "gray47")
button_subtract = Button(root,text="-", padx=42, pady=20, command= button_subtract, fg= "white", bg = "gray47")
button_multiply = Button(root,text="x", padx=40, pady=20, command= button_multiply, fg= "white", bg = "gray47")
button_divide = Button(root,text="%", padx=41, pady=20, command= button_divide, fg= "white", bg = "gray47")

button_equal = Button(root,text="=", padx=91, pady=20, command= button_equal, fg= "white", bg = "gray47")
button_clear = Button(root,text="clear", padx=79, pady=20, command= button_clear, fg= "white", bg = "gray47")


# Put the buttons on the screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1, columnspan=2)

button_add.grid(row=5,column=0,)
button_equal.grid(row=5,column=1, columnspan=2)

button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

root.mainloop()
