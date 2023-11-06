# Parte 1
nombre = input('\n\nEscibe tu Nombre: ')
print('\nHola', nombre, '\nBienvenido a tu')
print( ''' \n
        ******         ***               ***          ***        ***
        *********      ***              *****         ***        ***
        ***    ***     ***             *** ***        ***        ***
        ***    ***     ***            ***   ***       ***       ***
        ********       ***           ***********       ****   ****
        ***            ***           ***********         *******
        ***            **********    ***     ***           ***
        ***            **********    ***     ***           *** ''')

# Parte 2
from readchar import readkey, key
    
while True:
    tecla = readkey()
    if tecla != key.UP:
        print(tecla)
    else:
        tecla == key.UP
        print('TERMINADO')
        break
