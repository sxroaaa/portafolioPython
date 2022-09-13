from random import randint, random


dado1= randint(1, 6)
dado2= randint(1, 6)
print('el lanzamiento fue',dado1, 'y',dado2)

if dado1==1 and dado2 == 1:
  print('Ganaste')


elif dado1 == 1 and dado2 == 2 or dado1 == 2 and dado2 == 1:
    print('Ganaste')

elif dado1 + dado2 == 11:
    print('Ganaste')

elif dado1 + dado2 == 2 or dado1 + dado2 == 12:
    print('Ganaste')

elif dado1 + dado2 == 7:
    print('Ganaste')

else:
    print('Perdiste:( sigue intentando')
