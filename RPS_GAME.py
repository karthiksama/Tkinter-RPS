from tkinter import *
import random
r=''
l=0

p=Tk()

f=''

eq1=StringVar()
eq2=StringVar()
eq3=StringVar()
eq4=StringVar()
eq5=StringVar()
eq6=StringVar()

u=0
c=0

p.geometry("400x400")
p.title('ROPASI')
Label(p,text='VS',bg='grey',fg='white').place(x=180,y=200)

d1=Entry(p,textvariable=eq1)
d1.place(x=150,y=150)

d2=Entry(p,textvariable=eq2)
d2.place(x=150,y=250)

d3=Entry(p,textvariable=eq3)
d3.place(x=120,y=350)

d4=Entry(p,textvariable=eq4)
d4.place(x=200,y=200)

d5=Entry(p,textvariable=eq5)
d5.place(x=10,y=370)

d6=Entry(p,textvariable=eq6)
d6.place(x=180,y=370)

def user_score():
   global u
   u=u+5
   eq5.set(u)

def computer_score():
   global c
   c=c+5
   eq6.set(c)

def press(num):
 if(num==0):
      r='rock'
      eq1.set('rock')
 elif(num==1):
      r='paper'
      eq1.set('paper')
 else:
      r='scissors'
      eq1.set('scissors')

 l=random.choice(['rock','paper','scissors'])
 eq2.set(str(l))
 h=str(l)
 result(h,r)
    
Button(p,text='rock',command=lambda:press(0),bg='red',fg='white').grid(row=5,column=3)
Button(p,text='paper',command=lambda:press(1),bg='blue',fg='white').grid(row=7,column=3)
Button(p,text='scissors',command=lambda:press(2),bg='green',fg='white').grid(row=9,column=3)

Label(p,text='PLAYERS CHOICE',bg='orange',fg='white').place(x=150,y=130)
Label(p,text='COMPUTERS CHOICE',bg='orange',fg='white').place(x=150,y=230)
Label(p,text='RESULT',bg='indigo',fg='white').place(x=220,y=180)
Label(p,text='WINNER',bg='blue',fg='white').place(x=120,y=330)
Label(p,text='PLAYER SCORE',bg='green',fg='white').place(x=10,y=340)
Label(p,text='COMPUTER SCORE',bg='green',fg='white').place(x=270,y=340)


def result(h,r):
 if(r=='scissors' and h=='rock'):
    eq4.set('ROCK')
    eq3.set('COMPUTER ')
    computer_score()
 elif(r=='rock' and h=='scissors'):
    eq4.set('ROCK')
    eq3.set('PLAYER ')
    user_score()
 elif(r=='paper' and h=='rock'):
    eq4.set('PAPER')
    eq3.set('PLAYER ')
    user_score()
 elif(r=='rock' and h=='paper'):
    eq4.set('PAPER')
    eq3.set('COMPUTER ')
    computer_score()
 elif(r=='scissors' and h=='paper'):
    eq4.set('SCISSORS')
    eq3.set('PLAYER ')
    user_score()
 elif(r=='paper' and h=='scissors'):
    eq4.set('SCISSORS')
    eq3.set('COMPUTER ')   
    computer_score()
 else:
    eq4.set('DEAD LOCK')
    eq3.set('NO RESULT')

p.mainloop()