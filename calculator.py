from tkinter import *

root =Tk()
root.title("Calculator")


######################## Display #########################
screen = Entry(root, width=35, borderwidth=2, justify="right")
screen.grid(row=0, column=0, columnspan=4, pady=0)


###################### Definitions #######################
lst_num = [] # List of inputed numbers
lst_op = [] # List of operations that go between the inputted numbers


# Insert intergers into the calculator
def insertnum(number):
    current = screen.get()
    if current == "ERROR":
        screen.delete(0, END)
        return screen.insert(0, str(number))
    else:
        screen.delete(0, END)
        return screen.insert(0, current + str(number))


# Check if the number on the display already has a dot or not
def checkdot(entry):
    for i in range(len(entry)):
        if entry[i] == ".":
            return True
    return False


# Inserts a dot to create decimals. If a dot is already existant on the display, 
# returns the original number on the display
def insertdot():
    current = screen.get()
    if current == "ERROR":
        screen.delete(0, END)
        return screen.insert(0, ".")
    elif checkdot(current):
        screen.delete(0, END)
        return screen.insert(0, current)
    else:
        screen.delete(0, END)
        return screen.insert(0, current + ".")


# Turns the hnumber on the display into its negstive. If the display is blank,
# returns an error
def signbutton():
    current = screen.get()
    if (current == "") or (current == "ERROR"):
        screen.delete(0, END)
        return screen.insert(0, "ERROR")
    elif current[0] == "-":
        screen.delete(0, END)
        return screen.insert(0, current[1:])
    else:
        screen.delete(0, END)
        return screen.insert(0, "-" + current)


# Clears display and both lists of numbers and operations
def clearbutton():
    lst_num.clear()
    lst_op.clear()
    screen.delete(0, END)


# Saves the number on display into lst_num and saves
# the operation to be done in lst_op
def opbutton(op):
    current = screen.get()
    if (current == "") or (current == "ERROR"):
        screen.delete(0, END)
        return screen.insert(0, "ERROR")
    else:
        lst_op.append(op)
        lst_num.append(float(current))
        return screen.delete(0, END)


# Calculate the result using the list of numbers and list of operations and an accumulator "sofar"
# The inital accumulator must be the first element of lst_num, therefore the list of numbers
# inputed must be .pop() of its first elements
def calc(lst1, lst2, sofar):
    if lst2 == []:
        return sofar
    elif lst2[0] == "+":
        sofar = sofar + lst1[0]
        lst1.pop(0)
        lst2.pop(0)
        return calc(lst1, lst2, sofar)
    elif lst2[0] == "-":
        sofar = sofar - lst1[0]
        lst1.pop(0)
        lst2.pop(0)
        return calc(lst1, lst2, sofar)
    elif lst2[0] == "/":
        sofar = sofar / lst1[0]
        lst1.pop(0)
        lst2.pop(0)
        return calc(lst1, lst2, sofar)
    else:
        sofar = sofar * lst1[0]
        lst1.pop(0)
        lst2.pop(0)
        return calc(lst1, lst2, sofar)   


# Transforms results that can be written in integer form into integers
def float_int(num):
    if str(num)[-2:] == ".0":
        return int(num)
    else:
        return num

# Uses calc() to calculate the final result.
def equalbutton():
    final_num = screen.get()
    if (final_num == "ERROR") or (final_num == "") or ((final_num == "0") and (lst_op[-1] == "/")):
        screen.delete(0, END)
        return screen.insert(0, "ERROR")
    else:
        lst_num.append(float(final_num))
        sofar= lst_num[0]
        lst_num.pop(0)
        screen.delete(0, END)
        return screen.insert(0, str(float_int(calc(lst_num, lst_op, sofar))))


#################### Number buttons ######################
_1 = Button(root, text="1", padx=40, pady=20, command=lambda: insertnum(1))
_2 = Button(root, text="2", padx=40, pady=20, command=lambda: insertnum(2))
_3 = Button(root, text="3", padx=40, pady=20, command=lambda: insertnum(3))
_4 = Button(root, text="4", padx=40, pady=20, command=lambda: insertnum(4))
_5 = Button(root, text="5", padx=40, pady=20, command=lambda: insertnum(5))
_6 = Button(root, text="6", padx=40, pady=20, command=lambda: insertnum(6))
_7 = Button(root, text="7", padx=40, pady=20, command=lambda: insertnum(7))
_8 = Button(root, text="8", padx=40, pady=20, command=lambda: insertnum(8))
_9 = Button(root, text="9", padx=40, pady=20, command=lambda: insertnum(9))
_0 = Button(root, text="0", width=12, padx=40, pady=20, command=lambda: insertnum(0))
dot = Button(root, text=".", padx=42, pady=20, command=insertdot)

 
_1.grid(row=4, column=0)
_2.grid(row=4, column=1)
_3.grid(row=4, column=2)

_4.grid(row=3, column=0)
_5.grid(row=3, column=1)
_6.grid(row=3, column=2)

_7.grid(row=2, column=0)
_8.grid(row=2, column=1)
_9.grid(row=2, column=2)

_0.grid(row=5, column=0, columnspan=2)
dot.grid(row=5, column=2)


################### Operation buttons ####################
multiplication = Button(root, text="*", padx=41, pady=20, bg="yellow", command=lambda: opbutton("*"))
substraction = Button(root, text="-", padx=41, pady=20, bg="yellow", command=lambda: opbutton("-"))
division = Button(root, text="/", padx=42, pady=20, bg="yellow", command=lambda: opbutton("/"))
addition = Button(root, text="+", padx=40, pady=20, bg="yellow", command=lambda: opbutton("+"))
negative = Button(root, text="+/-", padx=34, pady=20, command=signbutton)
reset = Button(root, width=12, text="C", padx=40, pady=20, bg="orange", command=clearbutton)
equal = Button(root, text="=", padx=40, pady=20, bg="orange", command=equalbutton)

division.grid(row=1,column=3)
multiplication.grid(row=2,column=3)
substraction.grid(row=3,column=3)
addition.grid(row=4,column=3)

negative.grid(row=1, column=2)
equal.grid(row=5,column=3)
reset.grid(row=1, column=0, columnspan=2)


root.mainloop()