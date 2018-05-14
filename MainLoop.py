#tableauAff=[[0 for i in range(7)] for k in range(6)]

M=[ [ 0 for i in range(7) ] for i in range(6) ]
J=[ [ 0 for i in range(7) ] for i in range(7) ]
#tableauAff=[[0 for i in range(7)] for k in range(6)]

from tkinter import *
from Benef import Benef

def clique(event):
        print("bonjour")
        x=event.x
        y=event.y
        #if 600<x<650 and 500<y<550:
        #        print("l ia joue")
        #else:
        #i=(x-20)//90
        #j = (y-20)//90
        #M[j][i]=1
        i=(x-20)//90
        j=(y-20)//90
        M[j][i]=1
        if j>1:
                M[j-1][i]=2
        can.create_oval(90*i+20,90*j+20,90*i+70,90*j+70,fill='yellow')
        #FAIRE JOUER L IA

        Benef(M,J)
        Danger(M,J)
        Eval(J)
        Optim(J)
        (j,i)=OrdiJoue(M,J)
        i=(x-20)//90
        j=(y-20)//90
        can.create_oval(90*i+20,90*j+20,90*i+70,90*j+70,fill='red')
        #checkWin

fen=Tk()
can=Canvas(fen,height=600,width=750)
can.pack()
can.create_rectangle(0,0,650,700,fill='blue')
#can.create_rectangle(600,500,650,550,fill='green')
for i in range(7):
        for j in range(6):
                can.create_oval(90*i+20,90*j+20,90*i+70,90*j+70,fill='white')
fen.bind('<Button-1>',clique)
fen.mainloop()

