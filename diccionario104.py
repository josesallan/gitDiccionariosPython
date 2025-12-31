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

# Montamos una línea de cabecera para la tabla
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

# (Ejercicio 3)
# Mostraremos el número de elementos en el diccionario actual
# Utilizo la función len()
numero = len(titulares)
print('Iniciaron el partido', numero, 'jugadores')

#(Ejercicio 4)
# Crearemos ahora dos listas
# La primera está formada por la lista de todos lo índices utilizados
dorsales = titulares.keys()
#La segunda está formada por la lista de todos los datos almacenados
nombres = titulares.values()
#Mostramos ambas listas por pantalla.
print(dorsales)
print(nombres)