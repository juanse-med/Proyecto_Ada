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

# Parte 3
import os
number = 0
def borrar_consola():
    os.system('cls' if os.name=='nt' else 'clear')

while number <= 50:
    borrar_consola()
    print('Oprime la letra n para incrememntar el número, cualquier otra para salir')
    print(number)
    letra = readkey()
    if letra == 'n':
        number += 1
    else:
        break