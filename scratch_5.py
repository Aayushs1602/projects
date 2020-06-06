import tkinter as t
from tkinter import ttk
from tkinter import messagebox
player = 1
num =0
def check():
    global button1,button2,button3,button4,button5,button6,button7,button8,button9,num
    if  (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X') or (button5['text'] == 'X' and button6['text']=='X' and button4['text']=='X') or(button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X') or (button1['text'] == 'X' and button4['text'] == 'X' and button7['text']=='X') or(button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X') or (button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X') or(button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X') or (button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X'):
        messagebox._show('result of the game', 'player 1 won')
        tictac.quit()
    elif  (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O') or (button5['text'] == 'O' and button6['text']=='O' and button4['text']=='O') or(button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O') or (button1['text'] == 'O' and button4['text'] == 'O' and button7['text']=='O') or(button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O') or (button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O') or(button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O') or (button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O'):
        messagebox._show('result of the game','player 2 won')
        tictac.quit()
    else:
        if num > 9:
            messagebox._show('result of the game','draw!!')
def play():
    global tictac,button1,button2,button3,button4,button5,button6,button7,button8,button9, num
    tictac = t.Tk()
    tictac.title('TICTACTOC GAME')
    label = t.Label(tictac,text="player1 == X, plsyer2 == O\n\n\nOfcourse player1 goes first")
    t.Label(tictac,text="Note:plz click again after the game is over").grid(row=2,column=0)
    t.Label(tictac, text="NOTE: plz dont click the cross button it will most\n probably crash it isnt working like its supposed to be").grid(row=1, column=0)
    label.grid(column=0,row=0)

    button1 = ttk.Button(tictac, text=' ', command=lambda: button_press(1))
    button1.grid(column=1, row=0, ipadx=50, ipady=50)
    button4 = ttk.Button(tictac, text=' ', command=lambda: button_press(4))
    button4.grid(column=1, row=1, ipadx=50, ipady=50)
    button7 = ttk.Button(tictac, text=' ', command=lambda: button_press(7))
    button7.grid(column=1, row=2, ipadx=50, ipady=50)
    button2 = ttk.Button(tictac, text=' ', command=lambda: button_press(2))
    button2.grid(column=2, row=0, ipadx=50, ipady=50)
    button5 = ttk.Button(tictac, text=' ', command=lambda: button_press(5))
    button5.grid(column=2, row=1, ipadx=50, ipady=50)
    button8 = ttk.Button(tictac, text=' ', command=lambda: button_press(8))
    button8.grid(column=2, row=2, ipadx=50, ipady=50)
    button3 = ttk.Button(tictac, text=' ', command=lambda: button_press(3))
    button3.grid(column=3, row=0, ipadx=50, ipady=50)
    button6 = ttk.Button(tictac, text=' ', command=lambda: button_press(6))
    button6.grid(column=3, row=1, ipadx=50, ipady=50)
    button9 = ttk.Button(tictac, text=' ', command=lambda: button_press(9))
    button9.grid(column=3, row=2, ipadx=50, ipady=50)


    def button_press(value):
        check()
        global player,num
        value = int(value)
        if player == 1:
                if value == 1:
                    num+=1
                    player = 2
                    button1.config(text='X')
                elif value == 2:
                    num += 1
                    player = 2
                    button2.config(text='X')
                elif value == 3:
                    num += 1
                    player = 2
                    button3.config(text='X')
                elif value == 4:
                    num += 1
                    player = 2
                    button4.config(text='X')
                elif value == 5:
                    num += 1
                    player = 2
                    button5.config(text='X')
                elif value == 6:
                    num += 1
                    player = 2
                    button6.config(text='X')
                elif value == 7:
                    num += 1
                    player = 2
                    button7.config(text='X')
                elif value == 8:
                    num += 1
                    player = 2
                    button8.config(text='X')
                elif value == 9:
                    num += 1
                    player = 2
                    button9.config(text='X')

        else:
            if player == 2:

                    if value == 1:
                        num += 1
                        player = 1
                        button1.config(text='O')
                    elif value == 2:
                        num += 1
                        player = 1

                        button2.config(text='O')
                    elif value == 3:
                        num += 1
                        player = 1
                        button3.config(text='O')
                    elif value == 4:
                        num += 1
                        player = 1
                        button4.config(text='O')
                    elif value == 5:
                        num += 1
                        player = 1
                        button5.config(text='O')
                    elif value == 6:
                        num += 1
                        player = 1
                        button6.config(text='O')
                    elif value == 7:
                        num += 1
                        player = 1
                        button7.config(text='O')
                    elif value == 8:
                        num += 1
                        player = 1
                        button8.config(text='O')
                    elif value == 9:
                        num += 1
                        player = 1
                        button9.config(text='O')



    tictac.mainloop()

play()

messagebox._show('','do you want to play again\nyes or no:\nplz give the input in cmd')

while True:
    p = input('enter:')
    if p == 'yes':
        player = 1
        num = 0
        print('new should appear check if its minimized')
        play()
    else:
        print('bye')
        break