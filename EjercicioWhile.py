from re import S

repetir='s'
alcancia=0

while repetir == 's' or repetir == 'S':

    plata=int (input('ingrese el valor a ahorrar:'))
    alcancia=alcancia+plata
    if alcancia<=100000:
        repetir=input('desear ingresar mas dinero s o n para salir:')
    else:
        break

print(f'el total ahorrado es {alcancia}')