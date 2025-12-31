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

# Creo un bucle for que recorre todos los posibles índices (del 1 al 99)
for i in range(1, 99, 1):
    # Si no existe el índice termino la iteración actual
    if titulares.get(i, 'no') == 'no':
        continue
    # Si existe el índice lo muestro
    else:
        # Asigno a la variable nombre el valor asociado en titulares al índice i
        nombre = titulares[i]
        # Muestro el número del jugador y su nombre.
        print(i,'\t-> ',nombre)
# (3) Mostraré el número de elementos en el diccionario actual
# Utilizo la función len()
numero = len(titulares)
print('Iniciaron el partido',numero,'jugadores')
# Crearemos ahora dos listas
# La primera está formada por la lista de todos lo índices utilizados
dorsales = titulares.keys()
#La segunda está formada por la lista de todos los datos almacenados
nombres = titulares.values()
#Mostramos ambas listas por pantalla.
print(dorsales)
print(nombres)