# Program: Calculator 
# author: Manusri Allam
# date: 3/6/2023
'''
# file: Calculator is a program that takes an expression from the user, then does infix to postfix conversion,
makes a tree using stack functionality to organize the various operators and operands. Finally does the calculation
and returns the final answer to the expression. The programn gets advanced by implementing a GUI (a global user interface)
'''
# input: Inputs that are given by the user is the expression to evaluate by the calculator program
# output: It outputs an answer as a float to the given expression provided by the user.



# create a GUI calculator using tkinter
from tkinter import *
import calculator

def calculator1(gui):   
    # name the gui window
    gui.title("Calculator")
    # make a entry text box
    entrybox = Entry(gui, width=36, borderwidth=5)
    # position the entry text box in the gui window using the grid manager
    entrybox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    
    # create buttons: 1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,= 
    #These are the various buttons 
    b0 = addButton(gui,entrybox,'0')
    b1 = addButton(gui,entrybox,'1')
    b2 = addButton(gui,entrybox,'2')
    b3 = addButton(gui,entrybox,'3')
    b4 = addButton(gui,entrybox,'4')
    b5 = addButton(gui,entrybox,'5')
    b6 = addButton(gui,entrybox,'6')
    b7 = addButton(gui,entrybox,'7')
    b8 = addButton(gui,entrybox,'8')
    b9 = addButton(gui,entrybox,'9')
    b_add = addButton(gui,entrybox,'+')
    b_sub = addButton(gui,entrybox,'-')
    b_mult = addButton(gui,entrybox,'*')
    b_div = addButton(gui,entrybox,'/')
    b_clr = clearButton(gui,entrybox,'c')
    b_eq = calcButton(gui,entrybox,'=')


    # add buttons to the grid
    buttons =[ b7,    b8, b9,    b_clr, 
               b4,    b5, b6,    b_sub, 
               b1,    b2, b3,    b_add, 
               b_mult,b0, b_div, b_eq ]
    k = 4           
    for i in range(k):
        for j in range(k):
            buttons[i*k+j].grid(row=i+1, column=j, columnspan=1)
#adds to entry widget
def addButton(gui, entrybox, value):
    return Button(gui, text=value, height=4, width=9, command = lambda: clickButton(entrybox, value))
#clears output
def clearButton(gui, entrybox, value):
    return Button(gui, text=value, height=4, width=9, command = lambda: button_clear(entrybox))

#Function finally calculates the answer
def calcButton(gui, entrybox, value):
    return Button(gui, text=value, height=4, width=9, command = lambda: calculate(entrybox))

#clicks button functionality
def clickButton(entrybox, value):
    # the function clickButton() is not implemented!!!
    current = entrybox.get()
    entrybox.delete(0,END)
    entrybox.insert(0, str(current) + str(value))

def button_clear(entrybox):
    entrybox.delete(0,END)

def calculate(entrybox):
    input = entrybox.get()
    entrybox.delete(0, END)
    #Now we need to use the input to do the calculation
    final_eval = calculator.calculate(input)
    entrybox.insert(0,str(final_eval))

       
# main program
# create the main window
gui = Tk()
# create the calculator layout
calculator1(gui)
# update the window
gui.mainloop()