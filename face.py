#!/usr/bin/env python3
from tkinter import *
from PIL import Image, ImageTk

import tkinter.messagebox

def exitt():
    exit()

def printt():
    print("BAUD VALUE = ", int(baud.get()))
    print("PARIDADE = ", int(pary.get()))
    print("CONFIGURAÇÃO = ", str(conf.get()))

def add():
    aux = str(conf.get())
    if aux == 'BRISA':
        brisa()
    elif aux == 'RAMPA':
        rampa()
    elif aux == 'RIPPLE':
        ripple()
    elif aux == 'RAJADA':
        rajada()

def brisa():
    wBrisa = Tk()
    wBrisa.title("BRISA")
    wBrisa.geometry("300x200")
    l1 = Label(wBrisa, text= "Duração: ").place(x=20, y=20)
    e1 = Entry(wBrisa, textvar= duracao).place(x=150, y=20)  
    
    b0=Button(wBrisa, text="Ok", width= 8, height=1 ,fg='black', bg= 'gray', relief=GROOVE, font=("arial", 13, "italic"), command=listar)
    b0.place(x=60, y=120)
    b1=Button(wBrisa, text="Cancel", width= 8, height=1 ,fg='black', bg= 'gray', relief=GROOVE, font=("arial", 13, "italic"), command=wBrisa.destroy)
    b1.place(x=180, y=120)

def ripple():
    wRipple = Tk()
    wRipple.title("RIPPLE")
    wRipple.geometry("300x200")
    l1 = Label(wRipple, text= "Amplitude: ").place(x=20,y=20)
    l2 = Label(wRipple, text= "Duração: ").place(x=20, y=60)
    e1 = Entry(wRipple).place(x=150, y=20)
    e2 = Entry(wRipple).place(x=150, y=60)
    b0=Button(wRipple, text="Ok", width= 8, height=1 ,fg='black', bg= 'gray', relief=GROOVE, font=("arial", 13, "italic"))
    b0.place(x=60, y=120)
    b1=Button(wRipple, text="Cancel", width= 8, height=1 ,fg='black', bg= 'gray', relief=GROOVE, font=("arial", 13, "italic"), command=wRipple.destroy)
    b1.place(x=180, y=120)

def rajada():
    wRajada = Tk()
    wRajada.title("RAJADA")
    wRajada.geometry("300x200")
    l1 = Label(wRajada, text= "Velocidade final: ").place(x=20,y=20)
    l2 = Label(wRajada, text= "Duração: ").place(x=20, y=60)
    e1 = Entry(wRajada).place(x=150, y=20)
    e2 = Entry(wRajada).place(x=150, y=60)
    b0=Button(wRajada, text="Ok", width= 8, height=1 ,fg='black', bg= 'gray', relief=GROOVE, font=("arial", 13, "italic"))
    b0.place(x=60, y=120)
    b1=Button(wRajada, text="Cancel", width= 8, height=1 ,fg='black', bg= 'gray', relief=GROOVE, font=("arial", 13, "italic"), command=wRajada.destroy)
    b1.place(x=180, y=120)

def rampa():
    wRampa = Tk()
    wRampa.title("RAMPA")
    wRampa.geometry("300x200")
    l1 = Label(wRampa, text= "Velocidade final: ").place(x=20,y=20)
    l2 = Label(wRampa, text= "Duração: ").place(x=20, y=60)
    e1 = Entry(wRampa).place(x=150, y=20)
    e2 = Entry(wRampa).place(x=150, y=60)
    b0=Button(wRampa, text="Ok", width= 8, height=1 ,fg='black', bg= 'gray', relief=GROOVE, font=("arial", 13, "italic"), command= listar)
    b0.place(x=60, y=120)
    b1=Button(wRampa, text="Cancel", width= 8, height=1 ,fg='black', bg= 'gray', relief=GROOVE, font=("arial", 13, "italic"), command=wRampa.destroy)
    b1.place(x=180, y=120)

def listar():
    aux = int(duracao.get())
    print (aux)

###################################### INÍCIO ######################################

root=Tk()
root.geometry("600x600")
root.title("Emulador de vento")

# VARIABLES #
baud = IntVar()
pary = IntVar()
duracao = IntVar()
conf = StringVar()
vel_ini = IntVar()
vel_max = IntVar()
tempo = IntVar()

# LABELS #
label1 = Label(root,text="Gráfico", font=("arial", 12, "bold")).place(x=20, y=20)
label2 = Label(root,text="BaudRate (bit/s)", font=("arial", 12, "bold")).place(x=300, y=20)
label3 = Label(root,text="Histórico", font=("arial", 12, "bold")).place(x=20, y=320)
label4 = Label(root,text="Paridade", font=("arial", 12, "bold")).place(x=300, y=150)
label5 = Label(root,text="Velocidade Inicial", font=("arial", 9)).place(x=20, y=250)

# ENTRY #

e1 = Entry(root, textvar= vel_ini).place(x= 130, y=250)

# COMBO BOX #
list1 = ['BRISA', 'RAMPA', 'RIPPLE', 'RAJADA']
droplist = OptionMenu(root, conf, *list1)
conf.set("Selecione a configuração")
droplist.config(width=20)
droplist.place(x=20, y = 280)

# RADIO BUTTONS #
b1 = Radiobutton(root, text="9600", variable= baud, value= 1).place(x=310, y=50)
b2 = Radiobutton(root, text="19200", variable= baud, value= 2).place(x=310, y=70)
b3 = Radiobutton(root, text="38400", variable= baud, value= 3).place(x=310, y=90)
b4 = Radiobutton(root, text="57600", variable= baud, value= 4).place(x=310, y=110)

p1 = Radiobutton(root, text="None", variable= pary, value= 1).place(x=310, y=180)
p2 = Radiobutton(root, text="Even", variable= pary, value= 2).place(x=310, y=200)
p3 = Radiobutton(root, text="Odd", variable= pary, value= 3).place(x=310, y=220)

# BUTTONS #
button0=Button(root, text="+ Add", width= 4, height=1 ,fg='black', bg= 'gray', relief=GROOVE, font=("arial", 13, "italic"), command= add)
button0.place(x=200, y=280)
button1=Button(root, text="Cadastrar", width= 12, fg='black', bg= 'gray', relief=GROOVE, font=("arial", 13, "italic"))
button1.place(x=450, y=470)
button2=Button(root, text="Simular", width= 12, fg='black', bg= 'gray', relief=GROOVE, font=("arial", 13, "italic"), command=printt)
button2.place(x=450, y=510)
button3=Button(root, text="Sair", width= 12, fg='white', bg= 'brown', relief=GROOVE, font=("arial", 13, "italic"), command=exitt)
button3.place(x=450, y=550)

root.mainloop()
