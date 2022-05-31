words = ['start','Mango', 'Apple', 'Gun', 'Mobile','Notebook','colorful','Laptop','window','navigation','zebronics','youtube','exercise',
         'newspaper']


##################################to add slide of welcome to typing speed

def time():
    global timeleft,score,miss
    if(timeleft>0):
        timeleft -= 1
        timeLabelcount.configure(text=timeleft)
        timeLabelcount.after(1000,time)
    else:
        gameplaydetailLabel.configure(text='Hit ={} | Miss={} | Totalscore={}'.format(score,miss,score-miss))
        rr=messagebox.askretrycancel('Notification','For again hit Retry button')
        if(rr==True):
            score=0
            timeleft=60
            miss=0
            timeLabelcount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)

def startGame(event):
    global score,miss
    if(timeleft==60):
        time()
    gameplaydetailLabel.configure(text='')
    if (wordEntry.get() == wordLabel['text']):
        score += 1
        scoreLabelCount.configure(text=score)
    else:
        miss += 1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0, END)


from tkinter import *

import random
from tkinter import messagebox

##########################################################root method
root = Tk()
root.geometry('800x600+400+100')
root.configure(bg='powder blue')
root.title('Typing Speed Increaser Game')

###################################################################################variable section
score = 0
timeleft = 60
count = 0
sliderwords = ''
miss=0

##########################################################label method
fontLabel = Label(root, text='Welcome to the typing speed game', font=('airal', 25, 'bold'), bg='powder blue', fg='red', width=40)
fontLabel.place(x=10, y=10)


random.shuffle(words)

wordLabel = Label(root, text=words[0], font=('airal', 35, 'bold'), bg='powder blue')
wordLabel.place(x=350, y=200)

scoreLabel = Label(root, text='Your Score:', font=('airal', 20, 'bold'), bg='powder blue', fg='blue')
scoreLabel.place(x=10, y=60)

scoreLabelCount = Label(root, text=score, font=('airal', 25, 'bold'), bg='powder blue', fg='blue')
scoreLabelCount.place(x=80, y=100)

timerLabel = Label(root, text='Time left', font=('airal', 25, 'bold'), bg='powder blue', fg='blue')
timerLabel.place(x=600, y=60)

timeLabelcount = Label(root, text=timeleft, font=('airal', 25, 'bold'), bg='powder blue', fg='blue')
timeLabelcount.place(x=620, y=100)

gameplaydetailLabel = Label(root, text='Type word and Hit Enter buttom', font=('airal', 30, 'bold'), bg='powder blue',
                            fg='dark grey')
gameplaydetailLabel.place(x=120, y=450)

##########################################################Entry method
wordEntry = Entry(root, font=('airal', 25, 'bold'), bd=10, justify='center')
wordEntry.place(x=250, y=300)
wordEntry.focus_set()

#################################################################################
root.bind('<Return>', startGame)

root, mainloop()