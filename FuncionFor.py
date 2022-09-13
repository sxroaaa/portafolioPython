total=0
minutos=0
for i in range(1, 4, 1):
    precio=int(input('ingrese valor del producto:'))
    cantidad=int(input('ingrese la cantidad de productos_:'))
    subtotal=precio*cantidad
    total=total+subtotal
    minutos=minutos+1
    

print(f'por esta compra obtuviste {minutos} minutos para recargar a tu movil exito')
print('adios')
