# with 'from tkinter import *' we don't need to reference every object from tkinter
# ex. button() instead of tkinter.button()
from tkinter import *

# creating an empty window
window = Tk()

def km_to_miles():
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)

# creating button
# command parameter will point to a function that will be executed
# when the button is pressed
b1 = Button(window, text="Execute", command=km_to_miles)

# pack() places the button in the window
# b1.pack()
# can use grid() as well, it places the button in the grid
# ex. grid(row=0,column=0)
b1.grid(row=0,column=0)

e1_value = StringVar()
# Entry - input text box
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

# Text - text widget
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)


# thanks to window.mainloop() the window won't close by itself
window.mainloop()