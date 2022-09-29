resultado=0
totalnota=0

for i in range(1, 5, 1):
    nota=float(input("Digite de 1.0 al 5.0 la nota obtenidad en cada uno de los talleres:"))


    resultado=nota+nota/3
    totalnota=resultado
    print(totalnota)
    
    if  0.0>= totalnota <=2.9:
        print("reprobaste la asignatura")
     
    elif totalnota>=3.0:
        print("pasaste raspando la asignatura")
        
    elif  totalnota<=4.0:
        print("pasaste raspando la asignatura")
    
    elif totalnota>4.0:
        print ("aprobaste con buenos resultados") 
