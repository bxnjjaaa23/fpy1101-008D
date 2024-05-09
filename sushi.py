import os
import time
clave = "soyotaku"
contador=1
opcion=0
descuento=0
pikachup=4500
otakurp=5000
pulpop=5200
anguilap=4800
os.system("cls")
total_sushi=0
while contador<=1:
        time.sleep(1)
        print('''bienvenido a nuestro local de sushi
      En nuestra carta tenemos diferentes sushis
      1) Pikachu Roll $4500
      2) Otaku Roll $5000
      3) Pulpo Venenoso Roll $5200
      4) Anguila Elèctrica Roll $4800''')
        contador=5
        sushi=int(input('¿Que sushi desea comprar? '))
        if sushi==1:
                pikachu_cantidad=int(input('¿Cuantos desea comprar? '))
                pikachutotal=pikachup*pikachu_cantidad
                print(f'llevas {pikachu_cantidad} sushis "Pikachu Roll", en total es ${pikachutotal}')
                total_sushi=total_sushi+pikachutotal
                print(f'llevas en total a pagar ${total_sushi}')
        
        elif sushi==2:
                otaku_cantidad=int(input('¿Cuantos desea comprar? '))
                otakurtotal=otakurp*otaku_cantidad
                print(f'llevas {otaku_cantidad} sushis "Otaku Roll", en total es ${otakurtotal}')
                total_sushi=total_sushi+otakurtotal
                print(f'llevas en total a pagar ${total_sushi}')
            
        elif sushi==3:
                pulpo_cantidad=int(input('¿Cuantos desea comprar? '))
                pulpototal=pulpop*pulpo_cantidad
                print(f'llevas {pulpo_cantidad} sushis "Pulpo Venenoso", en total es ${pulpototal}')
                total_sushi=total_sushi+pulpototal
                print(f'llevas en total a pagar ${total_sushi}')
            
        elif sushi==4:
                anguila_cantidad=int(input('¿Cuantos desea comprar? '))
                anguilatotal=anguilap*anguila_cantidad
                print(f'llevas {anguila_cantidad} sushis "Anguila electrica", en total es ${anguilatotal}')
                total_sushi=total_sushi+anguilatotal
                print(f'llevas en total a pagar ${total_sushi}')
        else:
             print('opcion invalida')
        opcion=int(input('¿Desea comprar algo mas 1=si - 2= no? : '))
        if opcion==1:
            print('volviendo al menu...')
            contador=1
        else: 
            opcion==2
            print('okey, sigamos')
            contador=5
while contador>=5:
       int(input('Tienes un descuento?   1=si  -  2=no'))
       contador=4
       if descuento==1:
              claves = input('ingresa tu codigo de descuento')
              clave==claves
              valordesc=float(total_sushi*0.1)
              valortotal=total_sushi-valordesc
              print(f'el valor total con descuento es{valortotal}')
       elif descuento==2:
              opcion=int(input('¿Desea reingresar el codigo?  1=si  -  2=no'))
              if opcion==1:
                     print('volviendo...')
                     contador=5
              else:
                     opcion==2
                     print('aqui esta tu boleta')
else:
              print('')

    