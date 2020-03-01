# Ian Stroszeck Quadratic Equation Program

###IMPORTS###
from tkinter import *
from math import *

###FUNCTIONS###
def calculate():
    ###shows user equation correctly
    if float(c_value.get()) > 0:
        c_sign = "+"
    if float(c_value.get()) < 0:
        c_sign = ""
    if float(b_value.get()) > 0:
        b_sign = "+"
    if float(b_value.get()) < 0:
        b_sign = ""

    # Simplify a, b, and c values into floats and single letter
    a = float(a_value.get())
    b = float(b_value.get())
    c = float(c_value.get())

    ##Shows Equation depending on if there is a zero in it
    if b == 0 and c == 0:
        output_label.configure(text='Equation: {:.1f}x^2'.format(a), font=('Verdana', 10))
    if b == 0:
        output_label.configure(text='Equation: {:.1f}x^2 {} {:.1f}'.format(a, c_sign, c), font=('Verdana', 10))
    if c == 0:
        output_label.configure(text='Equation: {:.1f}x^2 {} {:.1f}x '.format(a, b_sign, b), font=('Verdana', 10))
    else:
        output_label.configure(text='Equation: {:.1f}x^2 {} {:.1f}x {} {:.1f}'.format(a, b_sign, b, c_sign, c),
                               font=('Verdana', 10))

    ###Start calucating quad formula
    ##Calculate discriminant
    disc = (b ** 2) - (4) * (a) * (c)

    ##Run formula

    ####If disc is less than one
    if (disc < 0):
        # Formula for imaginary roots and ask user input for radical or decimal form
        los = ((-b) / (2 * a))
        x = abs((sqrt(-disc))) / (2 * a)

        # radical form or not
        if radicalOrNot == "radical" or radicalOrNot == "r":
            radX = (x * x)
            radical = round(radX, 6)
            los = round(los, 6)
            ##Output to Tkinter Window
            raddec_label.configure(text="The Imaginary solutions to your quadratic equation are:".format(),
                                   font=('Verdana', 10))
            raddec_answer.configure(text='{:.0001f} + √({:.0001f})i'.format(los, radical), font=('Verdana', 10))
            raddec_answer2.configure(text='{:.0001f} - √({:.0001f})i'.format(los, radical), font=('Verdana', 10))
            '''
            ##Legacy Code for Terminal##########################################
            print("The imaginary solutions to your quadratic equation are: ")
            print(los, "+","√(", radical, ")i")
            print(los, "-","√(", radical, ")i")
            '''
        elif radicalOrNot == "decimal" or radicalOrNot == "d":
            x = round(x, 6)
            los = round(los, 6)
            # Output to Tkinter window
            raddec_label.configure(text="The Imaginary solutions to your quadratic equation are:".format(),
                                   font=('Verdana', 10))
            raddec_answer.configure(text='{} + {}i'.format(los, x), font=('Verdana', 10))
            raddec_answer2.configure(text='{} - {}i'.format(los, x), font=('Verdana', 10))
            '''
            #Legacy Code for Terminal window####################################
            print("The imaginary solutions to your quadratic equation are: ")
            print(los, "+", x, "i")
            print(los, "-", x, "i")
            '''

    ####If disc is greater than or equal to one
    elif (disc >= 0):
        # Formula for real roots
        x1 = ((-b) / (2 * a)) + (sqrt((b ** 2) - (4) * (a) * (c))) / (2 * a)
        x2 = ((-b) / (2 * a)) - (sqrt((b ** 2) - (4) * (a) * (c))) / (2 * a)

        # Printing real root answers to user
        if x1 == x2:
            x = round(x1, 6)
            # Output to Tkinter Window####
            raddec_label.configure(text="There is only one solution to your quadratic equation: ".format(),
                                   font=('Verdana', 10))
            raddec_answer.configure(text='x = {}'.format(x1), font=('Verdana', 10))
            ##MAY NOT NEED SECOND PART OF CODE
            raddec_answer2.configure(text=''.format(los, radical), font=('Verdana', 10))
            '''
            #Legacy code for Terminal######################################
            print("There is only one solution to your quadratic equation: ")
            print("x = ", x1)
            '''

        else:
            x1 = round(x1, 6)
            x2 = round(x2, 6)
            raddec_label.configure(text="The solutions to your quadratic equation are: ".format(), font=('Verdana', 10))
            raddec_answer.configure(text='x = {}'.format(x1), font=('Verdana', 10))
            raddec_answer2.configure(text='x = {}'.format(x2), font=('Verdana', 10))
            '''
            ##Legacy code for Terminal
            print("The solutions to your quadratic equation are: ")
            print("x = ", x1)
            print("x = ", x2)
            '''

        ###LABELS AND SETTINGS FOR TKINTER WELCOME SCREEN###


# Welcome note
welcome_label = Label(text="Please input values corresponding to: ax^2 + bx + c", font=('Verdana', 10))
welcome_label.grid(row=0, column=0, columnspan=3)

# Define Output Value
output_label = Label(font=('Verdana', 16))

# Define Answers raddec
raddec_label = Label(font=('Verdana', 10))
raddec_answer = Label(font=('Verdana', 10))
raddec_answer2 = Label(font=('Verdana', 10))

# A Value
a_label = Label(text='Enter an "a" value: ', font=('Verdana', 16))
a_value = Entry(font=('Verdana', 16), width=4)

# B value
b_label = Label(text='Enter an "b" value: ', font=('Verdana', 16))
b_value = Entry(font=('Verdana', 16), width=4)

# C value
c_label = Label(text='Enter an "c" value: ', font=('Verdana', 16))
c_value = Entry(font=('Verdana', 16), width=4)

##Calculate
calc_button = Button(text='Enter', font=('Verdana', 10), command=calculate)

# Radical/ Decimal Radio Button
v = IntVar()

# makes button selected and return decimal value
v.set('d')
radicalOrNot = 'd'


def varsetr():
    global radicalOrNot
    radicalOrNot = 'r'


def varsetd():
    global radicalOrNot
    radicalOrNot = 'd'


Radiobutton(text="Radical", command=varsetr, variable=v, value='r', indicatoron=0).grid(row=4, column=0)
Radiobutton(text="Decimal", command=varsetd, variable=v, value='d', indicatoron=0).grid(row=4, column=1)

####FIELD LOCATIONS####
a_label.grid(row=1, column=0)
a_value.grid(row=1, column=1)

b_label.grid(row=2, column=0)
b_value.grid(row=2, column=1)

c_label.grid(row=3, column=0)
c_value.grid(row=3, column=1)

calc_button.grid(row=2, column=2)

##Outputs to user
output_label.grid(row=5, column=0, columnspan=3)
raddec_label.grid(row=6, column=0, columnspan=3)
raddec_answer.grid(row=7, column=0, columnspan=1)
raddec_answer2.grid(row=7, column=1, columnspan=1)

mainloop()

###CHANGE LIST:###
# Fixed labels, on a_value
# got tkinter to print inputted values with check for c value
# Simplify a, b, and c values into floats and single letter
# check for negative values on b and a values in FLOAT
# check for disc
# Changed root() to √()
# Round Radicals
# add radio buttons, figure out how to implement in code so that radicalOrNot can use it.
# Round all other parts of answers
# Radical and Decimal form
####Change Radical_Label to answer_label
###Force Decimal mode unless otherwise changed v.set('d') and make selected button return value
##Add rad-dec answers and label to grid
##Add rad-dec answers to configure and to each if statement
##Change {:.001f} rounding
# Get equation to show up in Tkinter window
## If B or C Value = 0, then don't show in equation
##Add Tkinter outputs to window itself.

###STUFF TO DO###

'''COMPLETED ON THURSDAY, JUNE 4TH'''













