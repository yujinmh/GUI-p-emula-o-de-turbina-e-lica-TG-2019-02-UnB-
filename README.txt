Code by: Matheus Henrique Dinato Menezes e Victor Yuji Sato

Universidade de Bras�lia

Trabalho de Gradua��o 2019/02
Tema: Desenvolvimento de Interface de Comunica��o Baseada no Protocolo Modbus
para Conex�o de um Computador (PC) a um Inversor de Frequ�ncia

Orientador: L�lio Ribeiro Soares J�nior

O c�digo utiliza Python vers�o 3.7.0 para rodar. � poss�vel execut�-lo em plataformas Windows e Linux, utilizando o 
comando 'py tg_interface.py'. � necess�rio instalar algumas bibliotecas para executar o c�digo, tais como: serial e
minimalmodbus e tkinter (sendo o �ltimo um pacote padr�o de interface do Python).

A interface abrir� em uma nova janela ap�s a execu��o do comando citado anteriormente. Nela, � poss�vel criar
configura��es de velocidades e dura��es de diferentes tipos de ventos pr�programados, salvar a configura��o criada
pelo usu�rio em um arquivo .txt (no mesmo diret�rio em que se encontra o arquivo .py do c�digo) e/ou carregar um .txt
criado previamente com as configura��es desejadas. 

Links:
https://minimalmodbus.readthedocs.io/en/master/
https://pypi.org/project/pyserial/
https://docs.python.org/3/library/tkinter.html
