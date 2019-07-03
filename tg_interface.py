#Code by: Matheus Henrique Dinato Menezes e Victor Yuji Sato
#
#Universidade de Brasília
#
#Trabalho de Graduação 2019/02
#Tema: Desenvolvimento de Interface de Comunicação Baseada no Protocolo Modbus
#para Conexão de um Computador (PC) a um Inversor de Frequência
#
#Orientador: Lélio Ribeiro Soares Júnior

from tkinter import *
from tkinter import filedialog
import minimalmodbus
import serial
import time
import tkinter.messagebox

#FUNÇÃO PARA FECHAMENTO DE JANELA
def exitt():
    exit()

#FUNÇÃO PARA CRIAÇÃO DE ARQUIVO .TXT COM AS CONFIGURAÇÕES CRIADAS PELO USUÁRIO
def arqtexto():
    global conflista
    f= open("inputdeventos.txt","w+")
    f.write("Tipo:\tTempo:\tAmplitude:\tVelocidade Final\n")
    for i in range (len(conflista)):
        if i%4 == 0:
            f.write( conflista[i] + "\t")
        if i%4 == 1:
            if conflista[i] != 0:
                f.write(conflista[i] + "\t")
        if i%4 == 2:
            if conflista[i] != 0:
                f.write(conflista[i] + "\t\t")
        if i%4 == 3:
            if conflista[i] != 0:
                f.write(conflista[i] + "\n")
      
    f.close()

#FUNÇÃO PARA BROWSER, UTILIZADA PARA PROCURAR UM ARQUIVO .TXT COM CONFIGURAÇÕES JÁ CRIADAS PREVIAMENTE E CARREGAR AS
#CONFIGURAÇÕES CONTIDAS NELE
def browser():
    global conflista
    aux = []
    string = ''

    # filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File")
    filename = filedialog.askopenfilename(initialdir = "/Users/Matheus/Desktop/tgPy", title = "Select a File")
    label = Label(root, text=filename, anchor=E, width=24).place(x=23, y=252)
    f = open(filename, "r") 
    f.seek(42) # Pular a primeira linha
    msg = f.read()

    # Implementar alguma coisa aqui

    for x in msg:
        i = 0
        if x != '\n' and x != '\t':
            string += x
        elif x == '\n' or x == '\t':
            if string != '':
                aux.append(string)
            string = ''

    conflista.extend(aux)    
    f.close()
    print(conflista)

#FUNÇÃO PARA ZERAMENTO DE FUNÇÕES. IMPORTANTE PARA INICIALIZAÇÃO DE CADA JANELA ABERTA PARA CADA
#CONFIGURAÇÃO NOVA DE VENTO
def zerar():
    vel_max.set(0)
    ampl.set(0)
    tempo.set(0)

#FUNÇÃO PARA APAGAR A LISTA COM OS VENTOS SELECIONADOS ANTERIORMENTE
def apagar():
    global conflista
    global count

    count.set(0)
    conflista.clear()
    label = Label(root, anchor=E, width=24).place(x=23, y=252)
    label3 = Label(root,text="Histórico", anchor= NW, bd= 4, relief="groove", width=25, height= 13, font=("arial", 12, "bold")).place(x=23, y=320)

#FUNÇÃO PARA ENCERRAMENTO DE SIMULAÇÃO
def parar():
    b=Button(root, text="Parar Simulação", width= 22, fg='white', bg= 'brown', relief=GROOVE, font=("arial", 13, "italic"), command= b_all)
    b.place(x=300, y=458)

#FUNÇÃO PARA CRIAÇÃO DE BOTÕES CONTIDOS NA INTERFACE
def b_all():
    button0=Button(root, text="+Add", width= 5, height=1 ,fg='black', bg= 'light gray', justify= CENTER, relief=GROOVE, font=("arial", 10, "italic"), command= add)
    button0.place(x=200, y=282)
    button1=Button(root, text="Gerar txt", width= 24, fg='black', bg= 'light gray', relief=GROOVE, font=("arial", 13, "italic"), command=arqtexto)
    button1.place(x=300, y=418)
    button2=Button(root, text="Iniciar Emulação", width= 24, fg='black', bg= 'light gray', relief=GROOVE, font=("arial", 13, "italic"), command=inversor)
    button2.place(x=300, y=458)
    button3=Button(root, text="Apagar", width= 24, fg='black', bg= 'light gray', relief=GROOVE, font=("arial", 13, "italic"), command=apagar)
    button3.place(x=300, y=498)
    button4=Button(root, text="Sair", width= 12, fg='white', bg= 'brown', relief=GROOVE, font=("arial", 13, "italic"), command=exitt)
    button4.place(x=420, y=538)
    button5=Button(root, text="Browse", width= 5, height=1 ,fg='black', bg= 'light gray', justify= CENTER, relief=GROOVE, font=("arial", 10, "italic"), command= browser)
    button5.place(x=200, y=248)


#FUNÇÃO PARA ADQUIRIR O TIPO DE VENTO QUE O USUÁRIO DESEJAR
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

#FUNÇÃO PARA INSERIR NOVAS CONFIGURAÇÕES DE VENTO EM UMA LISTA. A LISTA É UTILIZADA PARA CRIAÇÃO DE TXT E PARA
#COMEÇAR A SIMULAÇÃO
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
        historico = str(line+1) + ": " + tipo + ": Tempo: " + t + " Amplitude: " + a
    elif tipo =="RAJADA":
        historico = str(line+1) + ": " + tipo + ": Tempo: " + t +"s Velocidade: " + v + "rpm"
    elif tipo =="RAMPA":
        historico = str(line+1) + ": " + tipo + ": Tempo: " + t +"s Velocidade: " + v + "rpm"
    if line < 14:
        label = Label(root,text= historico, font=("arial",7)).place(x=25, y=330 + (count.get()*16))

#FUNÇÃO RESPONSÁVEL POR COMUNICAR COM O INVERSOR. A TROCA DE MENSAGENS OCORRE AQUI
def inversor():
    global conflista
    global pary
    global baud
    global tsr
    global vel_ini
    global comprimento

    print("Comprimento = " + str(comprimento.get()))
    print("Tsr = " + str(tsr.get()))

    # conflista[1] = (int(tsr.get())*int(conflista[1])*9.549)/int(comprimento.get())
    # print(conflista[1])

    instrument = minimalmodbus.Instrument('COM3', 1) # port name, slave address (in decimal)
       
    if int(baud.get()) == 1:
        instrument.serial.baudrate = 9600   # Baud
        print(9600)
    elif int(baud.get()) == 2:
        instrument.serial.baudrate = 19200   # Baud
        print(19200)
    elif int(baud.get()) == 3:
        instrument.serial.baudrate = 38400   # Baud
        print(38400)
    elif int(baud.get()) == 4:
        instrument.serial.baudrate = 57600   # Baud
        print(19200)

    instrument.serial.bytesize = 8

    if int(pary.get()) == 1:
        instrument.serial.parity   = serial.PARITY_NONE
    elif int(pary.get()) == 2:
        instrument.serial.parity   = serial.PARITY_EVEN
    elif int(pary.get()) == 3:
        instrument.serial.parity   = serial.PARITY_ODD
    
    instrument.serial.stopbits = 1
    # instrument.serial.timeout  = 0.5 # seconds
    instrument.serial.xonxoff = False
    instrument.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode

    # INICIAR VALORES NO INVERSOR #

    time.sleep(2)

    instrument.write_register(682,0x0014)   # Deixar ele em modo operacional
    instrument.write_register(134,1500)     # Setar a velocidade máxima para 1800
    instrument.write_register(133,0)        # Setar a velocidade mínima para 0
    instrument.write_register(683,0)        # Setar a velocidade de referência para 0
    instrument.write_register(682,0x0013)   # Deixar ele em modo operacional

    time.sleep(2)
    
    # print(i)

    for i in range(len(conflista)):
        if i%4 == 0:

            if conflista[i] == "BRISA":
                print("A duracao da BRISA sera de " + conflista[i+1])
                instrument.write_register(133,30)   

                for i in range (1,conflista[i+1]+1):
                    vel_anterior = int(instrument.read_register(683,0)
                    a = random.randint( -5, 5)
                    vento =  vel_anterior + a
                    if vento <= 0:
                        vento = 3
                    elif vento > 100:
                        vento = 99
                    instrument.write_register(134,int(vento))
                    instrument.write_register(100,(int(vento))/int(vento)-int(vel_anterior))
                    instrument.write_register(683,int(vento)*8045/885)
                    time.sleep(1)

            elif conflista[i] == "RAJADA":
                print("A duracao da RAJADA sera de " + conflista[i+1])
                print("A velocidade maxima da RAJADA sera de " + conflista[i+3])

                conflista[i+3] = (int(tsr.get())*int(conflista[i+3])*9.549)/int(comprimento.get())
                v_ini = int(instrument.read_register(683,0))

                if conflista[i+3] > instrument.read_register(683, 0):
                    instrument.write_register(134,int(conflista[i+3]))
                    instrument.write_register(100,(int(conflista[i+1])*int(conflista[i+3]))/(2*(int(conflista[i+3])-int(instrument.read_register(683,0)))),1)
                    instrument.write_register(683,int(conflista[i+3])*8045/885)
                    time.sleep(int(conflista[i+1])/2)
                    instrument.write_register(101,(int(conflista[i+1])*int(conflista[i+3]))/(2*(int(instrument.read_register(683,0)-int(conflista[i+3])))),1)
                    instrument.write_register(683,v_ini*8045/885)
                    time.sleep(int(conflista[i+1]/2))
                elif conflista[i+3] == instrument.read_register(683,0):
                    time.sleep(int(conflista[i+1]))
                else:
                    instrument.write_register(101,(int(conflista[i+1])*int(conflista[i+3]))/(2*(int(instrument.read_register(683,0) - int(conflista[i+3])))),1)
                    instrument.write_register(683,int(conflista[i+3])*8045/885)
                    time.sleep(int(conflista[i+1])/2)
                    instrument.write_register(100,(int(conflista[i+1])*int(conflista[i+3]))/(2*(int(conflista[i+3])-int(instrument.read_register(683,0)))),1)
                    instrument.write_register(683,v_ini*8045/885)
                    time.sleep(int(conflista[i+1]/2))

            elif conflista[i] == "RIPPLE":
                print("A duracao da RIPPLE sera de " + conflista[i+1])
                print("A amplitude da RIPPLE sera de " + conflista[i+2])
                instrument.write_register(133,30)
                time.sleep(int(conflista[i+1]))

            elif conflista[i] == "RAMPA": 
                print("A duracao da RAMPA sera de " + conflista[i+1])
                print("A velocidade maxima da RAMPA sera de " + conflista[i+3])
                
                conflista[i+3] = (int(tsr.get())*int(conflista[i+3])*9.549)/int(comprimento.get())
                

                if int(conflista[i+3]) > int(instrument.read_register(683, 0)):

                    time.sleep(5)    
                    instrument.write_register(134,int(conflista[i+3]))
                    
                    instrument.write_register(100,(int(conflista[i+1])*int(conflista[i+3]))/(int(conflista[i+3])-int(instrument.read_register(683,0))),1)
                    
                    instrument.write_register(683,int(conflista[i+3])*8045/885)
                    time.sleep(int(conflista[i+1]))
                elif conflista[i+3] == instrument.read_register(683,0):
                    time.sleep(int(conflista[i+1]))
                else:
                    
                    instrument.write_register(101,(int(conflista[i+1])*int(conflista[i+3]))/(int(instrument.read_register(683,0) - int(conflista[i+3]))),1)
                    
                    instrument.write_register(683,int(conflista[i+3])*8045/885)
                    time.sleep(int(conflista[i+1]))
    
    print('Fim da emulacao!')
    instrument.write_register(682,0x0014)   # Deixar ele em modo operacional
    

# VENTOS #
#FUNÇÕES ('brisa', 'ripple', 'rajada' e 'rampa') PARA CRIAÇÃO DE JANELAS PARA CADA VEZ QUE O USUÁRIO DESEJAR ADICIONAR
#UMA NOVA CONFIGURAÇÃO DE VENTO
def brisa():
    zerar()
    wBrisa = Toplevel()
    wBrisa.title("BRISA")
    wBrisa.geometry("300x120+500+300")
    wBrisa.resizable(width=False, height=False)
    l1 = Label(wBrisa, text= "Duração (s): ").place(x=20, y=20)
    e1 = Entry(wBrisa, textvar= tempo).place(x=150, y=20)
   
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
    l1 = Label(wRipple, text= "Amplitude (m/s): ").place(x=20,y=20)
    l2 = Label(wRipple, text= "Duração (s): ").place(x=20, y=60)
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
    l1 = Label(wRajada, text= "Velocidade final (m/s): ").place(x=20,y=20)
    l2 = Label(wRajada, text= "Duração (s): ").place(x=20, y=60)
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
    l1 = Label(wRampa, text= "Velocidade final (m/s): ").place(x=20,y=20)
    l2 = Label(wRampa, text= "Duração (s): ").place(x=20, y=60)
    e1 = Entry(wRampa, textvar= vel_max).place(x=150, y=20)
    e2 = Entry(wRampa, textvar= tempo).place(x=150, y=60)
    b0=Button(wRampa, text="Ok", width= 8, height=1 ,fg='black', bg= 'light blue', relief=GROOVE, font=("arial", 13, "italic"), command=peguei)
    b0.place(x=85, y=100)
    b1=Button(wRampa, text="Cancel", width= 8, height=1 ,fg='black', bg= 'light blue', relief=GROOVE, font=("arial", 13, "italic"), command=wRampa.destroy)
    b1.place(x=185, y=100)

###################################### INÍCIO DA MAIN ######################################

root=Tk()

w_soft = 570
h_soft = 600
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x_pos = (screen_w/2)-(w_soft/2)
y_pos = (screen_h/2)-(h_soft/2)

root.geometry("%dx%d+%d+%d" % (w_soft, h_soft, x_pos, y_pos))
root.title("Emulador de vento")
root.resizable(width=False, height=False)
# root.configure(bg = "#94d42b")

# VARIABLES #
conflista = []
count = IntVar()
baud = IntVar()
pary = IntVar()
conf = StringVar()
vel_ini = IntVar()
vel_max = IntVar()
ampl = StringVar()
tempo = StringVar()
tsr = IntVar()
comprimento = IntVar()

# INICIAR VARIÁVEIS #

tsr.set(1)
comprimento.set(1)
pary.set(1)
baud.set(1)

# LABELS #
label1 = Label(root,text="Gráfico", anchor= NW, bd= 4, relief="groove", width=25, height= 11, font=("arial", 12, "bold")).place(x=23, y=20)
label2 = Label(root,text="BaudRate (bit/s)", anchor= NW, bd= 4, relief="groove", width=24, height= 6, font=("arial", 12, "bold")).place(x=300, y=20)
label3 = Label(root,text="Histórico", anchor= NW, bd= 4, relief="groove", width=25, height= 13, font=("arial", 12, "bold")).place(x=23, y=320)
label4 = Label(root,text="Paridade", anchor= NW, bd= 4, relief="groove", width=24, height= 5, font=("arial", 12, "bold")).place(x=300, y=150)
label5 = Label(root,text="Parâmetros Inicias", anchor= NW, bd= 4, relief="groove", width=24, height= 7, font=("arial", 12, "bold")).place(x=300, y=260)
label6 = Label(root,text="Velocidade Inicial\n(m/s)", font=("arial", 8)).place(x=305, y=290)
label7 = Label(root,text="Tip Speed Ratio", font=("arial", 8)).place(x=305, y=320)
label8 = Label(root,text="Comprimento da pá\n(m)", font=("arial", 8)).place(x=305, y=350)

# ENTRY #
s1 = Spinbox(root, from_=0, to=1800, textvar= vel_ini, width= 19, increment = 0.4).place(x= 405, y=290)
e2 = Entry(root, textvar= tsr).place(x=405, y=320)
e3 = Entry(root, textvar= comprimento).place(x=405, y=350)

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

b_all()

root.mainloop()
