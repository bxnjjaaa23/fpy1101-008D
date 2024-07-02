import time
def media(data):
    producto = 1
    for valor in data:
        producto *= valor
        return producto ** ( 1/ len(data))
    
a=[5,8,1,9,2]
media=media(a)
print(media)

time.sleep(0.7)

matriz= [
    [85, 45, 1, 7, 9],
    [12, 52, 9 , 151, 56],
    [76, 10, 56, 99, 9]
]

for lista in matriz:
    maximo=max(lista)
    i_max=lista.index(maximo)
    minimo=min(lista)
    i_min=lista.index(minimo)
    print(f'El maximo es {maximo} que esta en la columna {i_max}')
    time.sleep(0.3)
    print(f'El minimo es {minimo} que esta en la columna {i_min}')
    print('')
    
def calcular_prom(lista):
    total=sum(lista)
    cantidad=len(lista)
    return total / cantidad

time.sleep(0.7)
print('')
mi_lista = [10, 20, 30, 40, 50]
promedio=calcular_prom(mi_lista)
print(f'el promedio es {promedio:.2f}')

lis=[1, 5, 30, 60, 3234, 12984]

#for lista in lis:
maximo=max(lis)
i_max=lis.index(maximo)
minimo=min(lis)
i_min=lis.index(minimo)
print(f'El maximo es {maximo} que esta en la columna {i_max}')
time.sleep(0.3)
print(f'El minimo es {minimo} que esta en la columna {i_min}')
print('')
