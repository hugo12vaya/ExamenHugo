import random

numeroCasella = 0

while caselles>100 or caselles<10:

    caselles=int(input('Quantes caselles ha de tindre el tauler: '))

while numeroCasella!=caselles:
    
    dau = random.randint(1,6)

    numeroCasella = caselles + dau

    print ('He tret' ,dau, 'i he anat a la casella' ,numeroCasella,)

