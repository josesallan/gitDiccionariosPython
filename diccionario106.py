# Creamos el diccionario y añadimos los elementos
# Partimos de un diccionario vacío
titulares = {}

# Añadimos cada uno de los jugadores, cada uno de los datos será a su vez un diccionario

titulares[1] = {'posicion': 'POR', 'nombre': 'Iker Casillas', 'capitan': 'X'}
titulares[15] = {'posicion': 'DEF', 'nombre': 'Sergio Ramos'}
titulares[3] = {'posicion': 'DEF', 'nombre': 'Gerard Piqué'}
titulares[5] = {'posicion': 'DEF', 'nombre': 'Carles Puyo'}
titulares[11] = {'posicion': 'DEF', 'nombre': 'Joan Capdevila'}
titulares[14] = {'posicion': 'MED', 'nombre': 'Xabi Alonso'}
titulares[16] = {'posicion': 'MED', 'nombre': 'Sergio Busquets'}
titulares[8] = {'posicion': 'MED', 'nombre': 'Sergio Busquets'}
titulares[18] = {'posicion': 'MED', 'nombre': 'Pedro Rodríguez'}
titulares[6] = {'posicion': 'MED', 'nombre': 'Andrés Iniesta'}
titulares[7] = {'posicion': 'DEL', 'nombre': 'David Villa'}


# (5)Creamos una copia de la biblioteca titulares y la llamamos plantilla.
plantilla = titulares.copy()
# Mostraremos ahora los elementos de la biblioteca con la misma forma que en el 2.
print('   Plantilla selección 2010')
print('------------------------------')
print()
print(' Nº - Pos -  Nombre')
print(' =============================')

# Ejecutamos un bucle for que recorre todos los posibles índices (del 1 al 99)
for numero_camiseta in range(1, 99, 1):
    # Si no existe el índice termino la iteración actual
    if titulares.get(numero_camiseta, 'no') == 'no':
        continue
    # Si existe el índice lo muestro
    else:
        # Asigno a la variable datos_jugador el valor asociado en titulares al índice numero_camiseta
        datos_jugador = titulares[numero_camiseta]
        # Muestro el número del jugador actual y sus datos.
        if len(str(numero_camiseta)) == 1:
            print('  ' + str(numero_camiseta) + ' - ', end="")
        else:
            print(' ' + str(numero_camiseta) + ' - ', end="")
        print(datos_jugador['posicion'], '-> ', end="")
        print(datos_jugador['nombre'], end="")
        if datos_jugador.get('capitan', "no") == 'no':
            print()
        else:
            print(' (C)')
print("-")

# (6)Creamos la biblioteca suplentes
suplentes = {}

suplentes[4]  = {'posicion': 'DEF', 'nombre': 'Carlos Marchena'}
suplentes[9]  = {'posicion': 'DEL', 'nombre': 'Fernando Torres'}
suplentes[10] = {'posicion': 'MED', 'nombre': 'Cesc Fàbregas'}
suplentes[12] = {'posicion': 'POR', 'nombre': 'Víctor Valdés'}
suplentes[13] = {'posicion': 'DEL', 'nombre': 'Juan Mata'}
suplentes[17] = {'posicion': 'DEF', 'nombre': 'Álvaro Arbeloa'}
suplentes[19] = {'posicion': 'DEL', 'nombre': 'Fernando Llorente'}
suplentes[20] = {'posicion': 'MED', 'nombre': 'Javi Martínez'}
suplentes[21] = {'posicion': 'MED', 'nombre': 'David Silva'}
suplentes[22] = {'posicion': 'DEL', 'nombre': 'Jesús Navas'}
suplentes[23] = {'posicion': 'POR', 'nombre': 'Pepe Reina'}
print()

print('   Suplentes selección')
print('------------------------------')
print()
print(' Nº - Pos -  Nombre')
print(' =============================')
# Mostramos los datos de los suplentes
# Ejecutamos un bucle for que recorre todos los posibles índices (del 1 al 99)
for numero_camiseta in range(1, 99, 1):
    # Si no existe el índice termino la iteración actual
    if suplentes.get(numero_camiseta, 'no') == 'no':
        continue
    # Si existe el índice lo muestro
    else:
        # Asigno a la variable datos_jugador el valor asociado en titulares al índice numero_camiseta
        datos_jugador = suplentes[numero_camiseta]
        # Muestro el número del jugador actual y sus datos.
        if len(str(numero_camiseta)) == 1:
            print('  ' + str(numero_camiseta) + ' - ', end="")
        else:
            print(' ' + str(numero_camiseta) + ' - ', end="")
        print(datos_jugador['posicion'], '-> ', end="")
        print(datos_jugador['nombre'], end="")
        if datos_jugador.get('capitan', "no") == 'no':
            print()
        else:
            print(' (C)')
print("-")


