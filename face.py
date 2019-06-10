from tkinter import *
import tkinter.messagebox

def exitt():
    exit()

def arqtexto():
    global conflista
    f= open("inputdeventos.txt","w+")
    for i in range (len(conflista)):
        if i%4 == 0:
            f.write("Tipo:" + conflista[i] + " ")
        if i%4 == 1:
            if conflista[i] != 0:
                f.write("Tempo:" + conflista[i] + " ")
        if i%4 == 2:
            if conflista[i] != 0:
                f.write("Amplitude:" + conflista[i] + " ")
        if i%4 == 3:
            if conflista[i] != 0:
                f.write("Velocidade Final:" + conflista[i] + " \n")
      
    f.close()

def zerar():
    vel_max.set(0)
    ampl.set(0)
    tempo.set(0)

def printt():
    print("\nBAUD VALUE = ", int(baud.get()))
    print("PARIDADE = ", int(pary.get()))
    print("CONFIGURACAO = ", str(conf.get()))

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

def peguei():

    global count
    global conflista
    line = int(count.get())
    tipo = str(conf.get())
    t = str(tempo.get())
    a = str(ampl.get())
    v = str(vel_max.get())
    conflista.append(tipo)
    conflista.append(t)
    conflista.append(a)
    conflista.append(v)
    print (conflista)
    count.set(count.get()+1)
    if tipo == "BRISA":
        historico = str(line+1) + ": " + tipo + ": Tempo: " + t + "s"
    elif tipo =="RIPPLE":
        historico = str(line+1) + ": " + tipo + ": Tempo: " + t + "Amplitude: " + a
    elif tipo =="RAJADA":
        historico = str(line+1) + ": " + tipo + ": Tempo: " + t +"s Velocidade: " + v + "rpm"
    elif tipo =="RAMPA":
        historico = str(line+1) + ": " + tipo + ": Tempo: " + t +"s Velocidade: " + v + "rpm"
    if line < 14:
        label = Label(root,text= historico, font=("arial",7)).place(x=25, y=345 + line*16)

# VENTOS #

def brisa():
    zerar()
    wBrisa = Toplevel()
    wBrisa.title("BRISA")
    wBrisa.geometry("300x120+500+300")
    wBrisa.resizable(width=False, height=False)
    l1 = Label(wBrisa, text= "Duração: ").place(x=20, y=20)
    e1 = Entry(wBrisa, textvar= tempo).place(x=150, y=20)
    # w = Spinbox(wBrisa, from_=0, to=10).place(x=150, y=20)

    b0=Button(wBrisa, text="Salvar", width= 8, height=1 ,fg='black', bg= 'light blue', relief=GROOVE, font=("arial", 13, "italic"), command=peguei)
    b0.place(x=85, y=70)
    b1=Button(wBrisa, text="Sair", width= 8, height=1 ,fg='black', bg= 'light blue', relief=GROOVE, font=("arial", 13, "italic"), command=wBrisa.destroy)
    b1.place(x=185, y=70)

def ripple():
    zerar()
    wRipple = Toplevel()
    wRipple.title("RIPPLE")
    wRipple.geometry("300x160+500+300")
    wRipple.resizable(width=False, height=False)
    l1 = Label(wRipple, text= "Amplitude: ").place(x=20,y=20)
    l2 = Label(wRipple, text= "Duração: ").place(x=20, y=60)
    e1 = Entry(wRipple, textvar= ampl).place(x=150, y=20)
    e2 = Entry(wRipple, textvar= tempo).place(x=150, y=60)
    b0=Button(wRipple, text="Ok", width= 8, height=1 ,fg='black', bg= 'light blue', relief=GROOVE, font=("arial", 13, "italic"), command=peguei)
    b0.place(x=85, y=100)
    b1=Button(wRipple, text="Cancel", width= 8, height=1 ,fg='black', bg= 'light blue', relief=GROOVE, font=("arial", 13, "italic"), command=wRipple.destroy)
    b1.place(x=185, y=100)

def rajada():
    zerar()
    wRajada = Toplevel()
    wRajada.title("RAJADA")
    wRajada.geometry("300x160+500+300")
    wRajada.resizable(width=False, height=False)
    l1 = Label(wRajada, text= "Velocidade final: ").place(x=20,y=20)
    l2 = Label(wRajada, text= "Duração: ").place(x=20, y=60)
    e1 = Entry(wRajada, textvar= vel_max).place(x=150, y=20)
    e2 = Entry(wRajada, textvar= tempo).place(x=150, y=60)
    b0=Button(wRajada, text="Ok", width= 8, height=1 ,fg='black', bg= 'light blue', relief=GROOVE, font=("arial", 13, "italic"), command = peguei)
    b0.place(x=85, y=100)
    b1=Button(wRajada, text="Cancel", width= 8, height=1 ,fg='black', bg= 'light blue', relief=GROOVE, font=("arial", 13, "italic"), command=wRajada.destroy)
    b1.place(x=185, y=100)

def rampa():
    zerar()
    wRampa = Toplevel()
    wRampa.title("RAMPA")
    wRampa.geometry("300x160+500+300")
    wRampa.resizable(width=False, height=False)
    l1 = Label(wRampa, text= "Velocidade final: ").place(x=20,y=20)
    l2 = Label(wRampa, text= "Duração: ").place(x=20, y=60)
    e1 = Entry(wRampa, textvar= vel_max).place(x=150, y=20)
    e2 = Entry(wRampa, textvar= tempo).place(x=150, y=60)
    b0=Button(wRampa, text="Ok", width= 8, height=1 ,fg='black', bg= 'light blue', relief=GROOVE, font=("arial", 13, "italic"), command=peguei)
    b0.place(x=85, y=100)
    b1=Button(wRampa, text="Cancel", width= 8, height=1 ,fg='black', bg= 'light blue', relief=GROOVE, font=("arial", 13, "italic"), command=wRampa.destroy)
    b1.place(x=185, y=100)

###################################### INÍCIO ######################################

root=Tk()

w_soft = 570
h_soft = 600
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x_pos = (screen_w/2)-(w_soft/2)
y_pos = (screen_h/2)-(h_soft/2)

root.geometry("%dx%d+%d+%d" % (w_soft, h_soft, x_pos, y_pos))
# root.geometry("600x600+480+100")
root.title("Emulador de vento")
root.resizable(width=False, height=False)
# root.configure(bg = "#94d42b")

# VARIABLES ##
conflista = []
count = IntVar()
baud = IntVar()
pary = IntVar()
conf = StringVar()
vel_ini = IntVar()
vel_max = IntVar()
ampl = StringVar()
tempo = StringVar()


# LABELS #
label1 = Label(root,text="Gráfico", anchor= NW, bd= 4, relief="groove", width=25, height= 11, font=("arial", 12, "bold")).place(x=23, y=20)
label2 = Label(root,text="BaudRate (bit/s)", anchor= NW, bd= 4, relief="groove", width=22, height= 6, font=("arial", 12, "bold")).place(x=300, y=20)
# label3 = Label(root,text="Descrição", anchor= NW, bd= 4, relief="groove", width=22, height= 6, font=("arial", 12, "bold")).place(x=23, y=320)
label3 = Label(root,text="Histórico", anchor= NW, bd= 4, relief="groove", width=25, height= 13, font=("arial", 12, "bold")).place(x=23, y=320)
label4 = Label(root,text="Paridade", anchor= NW, bd= 4, relief="groove", width=22, height= 5, font=("arial", 12, "bold")).place(x=300, y=150)
label5 = Label(root,text="Velocidade Inicial", font=("arial", 9)).place(x=20, y=250)

# ENTRY #

# e1 = Entry(root, textvar= vel_ini, width= 19).place(x= 130, y=250)
s1 = Spinbox(root, from_=0, to=1800, textvar= vel_ini, width= 18).place(x= 130, y=250)

# COMBO BOX #
list1 = ['BRISA', 'RAMPA', 'RIPPLE', 'RAJADA']
droplist = OptionMenu(root, conf, *list1)
conf.set("Selecione a configuração")
droplist.config(width=22)
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
button0=Button(root, text="+Add", width= 5, height=1 ,fg='black', bg= 'light gray', justify= CENTER, relief=GROOVE, font=("arial", 10, "italic"), command= add)
button0.place(x=200, y=282)
button1=Button(root, text="Cadastrar", width= 22, fg='black', bg= 'light gray', relief=GROOVE, font=("arial", 13, "italic"), command=arqtexto)
button1.place(x=300, y=418)
button2=Button(root, text="Simular", width= 22, fg='black', bg= 'light gray', relief=GROOVE, font=("arial", 13, "italic"), command=printt)
button2.place(x=300, y=458)
button3=Button(root, text="Apagar", width= 22, fg='black', bg= 'light gray', relief=GROOVE, font=("arial", 13, "italic"))
button3.place(x=300, y=498)
button4=Button(root, text="Sair", width= 12, fg='white', bg= 'brown', relief=GROOVE, font=("arial", 13, "italic"), command=exitt)
button4.place(x=400, y=538)

root.mainloop()
