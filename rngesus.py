import random
import time

# vento = int(input('Insira a velocidade inicial do vento da ~BRISA~: '))

# for i in range (1, 100):
#     a = random.randint( -5, 5)
#     vento = vento + a
#     if vento <= 0:
#         vento = 0
#         vento = vento + 3
#     if vento > 10:
#         vento = 12
#     time.sleep(1.5)
#     print (vento)

vento = int(input('Insira a velocidade inicial do vento da RIPPLE: '))
amplitude = int(input('Insira a amplitude da onda da RIPPLE: '))
tempo = int(input('Insira a duracao da onda da RIPPLE: '))
aux = amplitude

for i in range(1, tempo+1):
    while aux != 0:
        passo = random.randint( 0, aux)
        time.sleep(0.1)
        aux = aux - passo
        print('AUX: ', aux,' PASSO: ', passo)
    aux = amplitude
    while aux != 0:
        passo = random.randint( 0, aux)
        time.sleep(0.1)
        aux = aux - passo
        print('AUX: ', aux,' PASSO: ', passo)
