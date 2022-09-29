Hombre=0
Mujer=0
for i in range(1, 11, 1):
    genero=input('Escriba el genero con el que se identifica:')

    if genero=='mujer' or genero==Mujer:
        Mujer=Mujer+1
    if genero=='hombre' or genero==Hombre:
        Hombre=Hombre+1
    else:
        ('Ninguno de los dos')
print(f'el total de mujeres son {Mujer} y el total de hombres son {Hombre}')
