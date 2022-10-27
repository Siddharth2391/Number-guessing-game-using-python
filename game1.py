from tkinter import *
from PIL import ImageTk,Image
import random
import tkinter.messagebox as tmsg

def basic():
    app.title("Number Guessing game")
    app.geometry("500x500")
    app.minsize(500,500)
    app.maxsize(500,500)
    photo = PhotoImage(file = "guess.png")
    app.iconphoto(False, photo)
    # appmenu=Menu(app)
    # appmenu.add_command(label='Start')
    # appmenu.add_command(label='Quit',command=quit())
    # app.config(menu=appmenu)
    # bg = Image.open('guess.png')
    # resized_image= bg.resize((400,400), Image.ANTIALIAS)
    # n= ImageTk.PhotoImage(resized_image)

    # canvas1 = Canvas( app, width = 400,height = 400)
    # canvas1.pack(fill = "both", expand = True)
    # canvas1.create_image( 0, 0, image = n,anchor = "nw")

    heading=Label(text='Number Guessing game',font="Helvicta 18 bold",bg='black',fg='tomato',padx=170).pack()
    with open('score.txt','r') as f:
        hg=f.read()
    
    sc=Label(app,text=f'Previous score: {hg}',font='lucida 8 bold ').pack(anchor=E,padx=25,pady=5)
    footer=Label(text='Developed by Siddharth Dyamgond',font="Helvicta 8 bold",bg='black',fg='tomato',padx=153).pack(side=BOTTOM)

def result():
    global count
    number=userv.get()
    if number=='':
        tmsg.showerror('Error',"Please enter a value")
    else:
        n=int(number)
        # print(n)
        count+=1
        # print(count)
        if comp==n:
            a=tmsg.showinfo('Win',f'You guess right number!\nYour score {count}')
            show.config(text='Winn!',fg='green')
            with open('score.txt','w') as f:
                f.write(str(count))
        elif comp>n:
            show.config(text='Select greater number',fg='red')
        else:
            show.config(text='Select smaller number',fg='red')

    
# def level():
#     pass
#     # with open('score.txt','a') as f:
#     #     f.write(str(count))
#     #     Label(text=f'Highscore  : {count}',font='Helvicta 18 bold').pack(pady=10)

def myfunc():
    pass

def call1():
    str1='This game is developed by Siddharth Dyamgond\n\ncopyright@2021-22 SD tech pvt limt.'
    tmsg.showinfo('About',str1)
    
app = Tk()
basic()
count=0
mymenu=Menu(app)
filee=Menu(mymenu,tearoff=0)
filee.add_command(label='Beginner',command=myfunc)
filee.add_command(label='Medium',command=myfunc)
filee.add_command(label='Hard',command=myfunc)
mymenu.add_cascade(label='Start',menu=filee)
mymenu.add_command(label='About',command=call1)
mymenu.add_command(label='Quit',command=quit)
app.config(menu=mymenu)


# set display image
i=Image.open('guess.png',mode='r')
img=ImageTk.PhotoImage(i)
l=Label(image=img).pack(pady=30)

#set entry box
# global count
# count=0cls
comp=random.randint(1, 101)
print(comp)
userv=StringVar()
user=Entry(app,textvariable=userv,justify=CENTER,relief=FLAT,borderwidth=2,font='Helvicta 18 bold').pack(pady=10) 
i= Image.open('bt.jpg')
resized_image= i.resize((150,50), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
submit=Button(app,image=new_image,command=result,font='Helvicta 18 bold',relief=FLAT).pack(pady=10)
show=Label(app,text='',font='Helvicta 12 bold')
show.pack(pady=10)



app.mainloop()

