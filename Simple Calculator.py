# importing the needed modules
import tkinter as t
from tkinter import ttk

expression = ""

def base():
    global expression,equation
    win = t.Tk()# intitaling the window
    win.title("calculator")# intitaling the window title

    equation = t.StringVar() #varaible for the entry can be changed

    #layout entry adding

    entry = t.Entry(win, textvariable=equation)
    equation.set("")  # setting the value of the entry
    entry.grid(row=0,columnspan=5,ipady = 20,ipadx =200)

    #layout buttons adding
    button1  = ttk.Button(win,text='1',command=lambda:pressed(1))
    button1.grid(row=1,column=0,ipadx =30, ipady = 30)
    button2 = ttk.Button(win, text='2', command=lambda: pressed(2))
    button2.grid(row=1, column=1,ipadx =30, ipady = 30)
    button3 = ttk.Button(win, text='3', command=lambda: pressed(3))
    button3.grid(row=1, column=2,ipadx =30, ipady = 30)
    button4 = ttk.Button(win, text='4', command=lambda: pressed(4))
    button4.grid(row=2, column=0,ipadx =30, ipady = 30)
    button5 = ttk.Button(win, text='5', command=lambda: pressed(5))
    button5.grid(row=2, column=1,ipadx =30, ipady = 30)
    button6 = ttk.Button(win, text='6', command=lambda: pressed(6))
    button6.grid(row=2, column=2,ipadx =30, ipady = 30)
    button7 = ttk.Button(win, text='7', command=lambda: pressed(7))
    button7.grid(row=3, column=0,ipadx =30, ipady = 30)
    button8 = ttk.Button(win, text='8', command=lambda: pressed(8))
    button8.grid(row=3, column=1,ipadx =30, ipady =30)
    button9 = ttk.Button(win, text='9', command=lambda: pressed(9))
    button9.grid(row=3, column=2,ipadx =30, ipady = 30)
    button0 = ttk.Button(win, text='0', command=lambda: pressed(0))
    button0.grid(row=4, column=1,ipadx =30, ipady = 30)
    buttonpu = ttk.Button(win,text='+',command=lambda:pressed('+'))
    buttonpu.grid(row=1,column=3,ipadx =30, ipady = 30)
    buttonmi = ttk.Button(win, text='-', command=lambda: pressed('-'))
    buttonmi.grid(row=2, column=3,ipadx =30, ipady = 30)
    buttonmu = ttk.Button(win, text='x', command=lambda: pressed('*'))
    buttonmu.grid(row=3, column=3,ipadx =30, ipady = 30)
    buttonde = ttk.Button(win, text='/', command=lambda: pressed('/'))
    buttonde.grid(row=4, column=3,ipadx =30, ipady = 30)
    buttoneu = ttk.Button(win, text='=', command=lambda: equal())
    buttoneu.grid(row=4, column=2,ipadx =30, ipady = 30)
    buttondot = ttk.Button(win, text='.', command=lambda: pressed('.'))
    buttondot.grid(row=4, column=0,ipadx =30, ipady = 30)

    win.mainloop() #looping the window so it doesn't crash after starting
def equal():
    """
    starts when = button is pressed
    gives the output
    """
    global equation
    try:
        global expression
        total = str(eval(expression)) #calcualting the expression

        equation.set(total) #display the equation's answer
        expression = ""
    except Exception as e: #handling the exception

        #equation.set(" Error {}".format(e)) for checking which error occurred
        equation.set(" Error ")
        expression = ""
def pressed(value):
    """
    starts when any other button is pressed
    updates the value
    :param value:
    :return:
    """
    global expression, equation

    expression = expression + str(value)

    equation.set(expression) #updating the expression

if __name__ == "__main__":
    base() #calling the main function
