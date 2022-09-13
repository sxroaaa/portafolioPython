from random import randint, random

jugador1= randint(1,3)
jugador2= randint(1, 3)
print ('(1)piedra)')
print('(2)papel)')
print('(3)tijera')
eleccion=input('elige:' )

if jugador1==2 and jugador2==3:
    print('Ganaste tijera corta a papel')
elif jugador1==2 and jugador2==1:
    print('ganaste, piedra enrrolla papel')
elif jugador1==1 and jugador2==3:
    print('perdiste, piedra rompe las tijeras')
elif jugador1==1 and jugador2==2:
    print('Ganaste, papel enrrolla a la piedra')
elif jugador1==3 and jugador2== 2:
    print('perdiste, tijera corta a papel')
elif jugador1==3 and jugador2==1:
    print('Ganaste, piedra rompe a la tijera')
elif jugador1==jugador2:
    print('hay un empate')

 