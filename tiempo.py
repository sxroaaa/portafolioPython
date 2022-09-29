segundos=int(input("ingrese cantidad segundos:"))
horas=segundos//3600
sobrante1=segundos%3600
minutos=sobrante1//60
sobrante2= sobrante1%60
print('horas')
print(horas)

print('minutos')
print(minutos)

print('segundos')
print(sobrante2)