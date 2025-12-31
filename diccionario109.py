# Creamos el diccionario y añadimos los elementos
titulares = {}
titulares[1] = 'Casillas'
titulares[3] = 'Pique'
titulares[5] = 'Puyol'
titulares[6] = 'Iniesta'
titulares[7] = 'Villa'
titulares[8] = 'Xavi Hernández'
titulares[11] = 'Capdevila'
titulares[14] = 'Xavi Alonso'
titulares[15] = 'Ramos'
titulares[16] = 'Busquets'
titulares[18] = 'Pedrito'

# (6)Creo la biblioteca suplentes
suplentes = {}
suplentes[4] = 'Marchena'
suplentes[9] = 'Torres'
suplentes[10] = 'Fàbregas'
suplentes[12] = 'Valdés'
suplentes[13] = 'Mata'
suplentes[17] = 'Arbeloa'
suplentes[19] = 'Llorente'
suplentes[20] = 'Javi Martínez'
suplentes[21] = 'Silva'
suplentes[22] = 'Navas'
suplentes[23] = 'Reina'

# Mostramos los resultados
print()
print('Jugando en el campo')
print('-------------------')
for i in range(1, 99, 1):
    if titulares.get(i, 'No') == 'No':
        continue
    else:
        print(i, '\t->', titulares.get(i))
print()
print('Suplentes')
print('---------')
for i in range(1, 99, 1):
    if suplentes.get(i, 'No') == 'No':
        continue
    else:
        print(i, '\t->', suplentes.get(i))
cambio = 1
# Con un bucle while controlamos el número de cambios
while cambio <= 3:
    # Preguntamos por el nombre del jugador a sustituir
    sale = int(input('Introduce el número del jugador que quieres sustituir:'))
    # Debemos leer el nombre del jugador sustituido
    # Si el número no existe no lo podemos sustituir
    nombresale = titulares.get(sale, 'No')
    if nombresale == 'No':
        # Si el número del jugador es incorrecto terminamos la iteración
        print('Número incorrecto - Cambio cancelado')
        continue
    else:
        print('Jugador a susituir:', nombresale, '\tnúmero:', sale)
    # Preguntamos por el nombre del jugador que va a entrar al campo
    entra = int(input('Introduce el número del jugador que va a entrar:'))
    # Debemos leer el nombre del jugador a introducir
    # Si el número no existe no lo podemos sustituir
    nombreentra = suplentes.get(entra, 'No')
    if nombreentra == 'No':
        # Si el número del jugador es incorrecto terminamos la iteración
        print('Número incorrecto - Cambio cancelado')
        continue
    else:
        print('Jugador a susituir:', nombresale, '\tnúmero:', sale)
        print('Jugador que entra en su lugar:', nombreentra, '\tnúmero:', entra)
        # Es en este momento cuando puedo realizar la sustitución
        ###########################################################################
        # Elimino al jugador sustituido del diccionario titulares
        titulares.pop(sale)

        # Elimino al jugador que entra del diccionario suplentes
        suplentes.pop(entra)

        # Añado el jugador que entra al diccionario titulares
        titulares.setdefault(entra, nombreentra)

        # Añado el jugador que sale al diccionario suplentes
        suplentes.setdefault(sale, nombresale)
        # Muestro los resultados actualizados
        # Mostramos los resultados
        print()
        print('Jugando en el campo')
        print('-------------------')
        for i in range(1, 99, 1):
            if titulares.get(i, 'No') == 'No':
                continue
            else:
                print(i, '\t->', titulares.get(i))
        print()
        print('Suplentes')
        print('---------')
        for i in range(1, 99, 1):
            if suplentes.get(i, 'No') == 'No':
                continue
            else:
                print(i, '\t->', suplentes.get(i))
        # Incrementamos el resultado de la variable cambio
        cambio = cambio + 1
print('Ya has realizado las tres sustituciones')
