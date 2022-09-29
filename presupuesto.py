presupuesto=100000
seguir="s"
gastoc=0
while seguir=="s" or seguir=="S":
    gasto=int(input("ingresa el valor del gasto:"))
    presupuesto=presupuesto-gasto
    gastoc=gastoc+1
    print(f"su gasto ha sido de {gasto} y le queda un presupuesto de {presupuesto}")
    
    if gastoc<=3 or gasto>100000 :
       seguir=input("escriba s si quiere agregar otro gasto:")
    else:
        break
