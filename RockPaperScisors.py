import tkinter as tk
from tkinter import messagebox as  msg
import random as ran

num=int(input("Enter number of rounds: "))
num-=1
def game(rounds:int):

    val=0
    while val<=rounds:
        val+=1
        gameOBJs=('rock','paper','scissors')
        compChoice=ran.choice(gameOBJs)

        r=tk.Tk()
        r.geometry('400x400')
        r.title('Rock Paper Scissors')

        def rock():
            if compChoice=='paper':msg.showinfo('Result','Paper beats Rock!\nYou lost....')

            if compChoice=='rock':msg.showinfo('Result','Rock and Rock dont do anything')

            if compChoice=='scissors':msg.showinfo('Result','Rock beats Scissors\nYou win!')

            r.destroy()

        def paper():
            if compChoice=='paper':msg.showinfo('Result','Paper and Paper do nothing...')

            if compChoice=='rock':msg.showinfo('Result','Paper beats Rock!\nYou Win!')

            if compChoice=='scissors':msg.showinfo('Result','Scissors beat Paper\nYou loose...')
            r.destroy()

        def scissors():
            if compChoice=='paper':msg.showinfo('Result','Scissors beat Paper!\nYou win!')

            if compChoice=='scissors':msg.showinfo('Result','Scissor and Scissor dont do anything')

            if compChoice=='rock':msg.showinfo('Result','Rock beats Scissors\nYou loose...')
            r.destroy()

        def randFUNC():
            funcs=('scissors','paper','rock')

            TheChoosenOne=ran.choice(funcs)

            if TheChoosenOne=='scissors':
                scissors()
            
            elif TheChoosenOne=='rock':
                rock()

            elif TheChoosenOne=='paper':
                paper()

        scissorsButton=tk.Button(r,text='Scissors',command=scissors).pack(pady=10)
        paperButton=tk.Button(r,text='Paper',command=paper).pack(pady=10)
        rockButton=tk.Button(r,text='Rock',command=rock).pack(pady=10)
        shoo=tk.Button(r,text='Rock Paper scissors shoo!',command=randFUNC).pack(pady=10)

        r.mainloop()

game(num)