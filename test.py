import tkinter
from tkinter import *

window = Tk()
#x=window.winfo_screenwidth()
#y=window.winfo_screenheight()
#window.geometry("{}x{}".format(x,y))
window.configure(bg='steel blue')
window.state('zoomed')
#print(window.winfo_height())
#print(window.winfo_screenwidth())
x = window.winfo_screenwidth()
y= window.winfo_screenheight()
print(x, y)

menubar = Menu(window, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')  
file = Menu(menubar, tearoff=0, background='SteelBlue2', foreground='black')  
file.add_command(label="New")  
file.add_command(label="Open")  
file.add_command(label="Save")  
file.add_command(label="Save as")    
file.add_separator()  
file.add_command(label="Exit", command=window.quit)  
menubar.add_cascade(label="File", menu=file)  

edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
edit.add_separator()     
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
menubar.add_cascade(label="Edit", menu=edit)  

help = Menu(menubar, tearoff=0)  
help.add_command(label="About")  
menubar.add_cascade(label="Help", menu=help)  
    
window.config(menu=menubar)

FIRE_button = PhotoImage(file='C:/Users/mazar/Downloads/FIRE.png')
FIRE_label = Button(image=FIRE_button, borderwidth=0, bg='steel blue', foreground='steel blue', activebackground='steel blue')
#FIRE_label.pack(pady=5)

#Grid.rowconfigure(window,0,weight=1)
#Grid.columnconfigure(window,0,weight=1)
 
#Grid.rowconfigure(window,1,weight=1)

first_frame = Frame(window, bg='honeydew3', width=(x/4)-20, height=(y/2)-70, pady=3, highlightbackground='white', highlightthickness=1).grid(row=0, column=0, padx=10, pady=10)
second_frame = Frame(window, bg='honeydew3', width=(x/4)-20, height=(y/2)-70, pady=3, highlightbackground='white', highlightthickness=1).grid(row=0, column=1, padx=10, pady=10)
third_frame = Frame(window, bg='honeydew3', width=(x/4)-20, height=(y/2)-70, pady=3, highlightbackground='white', highlightthickness=1).grid(row=0, column=2, padx=10, pady=10)
fourth_frame = Frame(window, bg='honeydew3', width=(x/4)-20, height=(y/2)-70, pady=3, highlightbackground='white', highlightthickness=1).grid(row=0, column=3, padx=10, pady=10)

fifth_frame = Frame(window, bg='honeydew3', width=(x/4)-20, height=(y/2)-70, pady=3, highlightbackground='white', highlightthickness=1).grid(row=1, column=0, padx=10, pady=10)
sixth_frame = Frame(window, bg='honeydew3', width=(x/4)-20, height=(y/2)-70, pady=3, highlightbackground='white', highlightthickness=1).grid(row=1, column=1, padx=10, pady=10)
seventh_frame = Frame(window, bg='honeydew3', width=(x/4)-20, height=(y/2)-70, pady=3, highlightbackground='white', highlightthickness=1).grid(row=1, column=2, padx=10, pady=10)
eigth_frame = Frame(window, bg='honeydew3', width=(x/4)-20, height=(y/2)-70, pady=3, highlightbackground='white', highlightthickness=1).grid(row=1, column=3, padx=10, pady=10)

eightfifty1 = Label(first_frame, text="850PC", font=('Ubuntu',18,'bold'))

mainloop()