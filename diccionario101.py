# Creamos el diccionario y añadimos los elementos
# Partimos de un diccionario vacío
titulares = {}

# Añadimos cada uno de los jugadores.
# La información de cada uno de los jugadores estará almacenada en un diccionario independiente
# No es necesaro que los diccionarios de todos los jugadores tengan los mismos campos.
# Para acceder a los diferentes campos del diccionario de un jugador necesitaré conocer el nombre de las claves.

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

# Mostramos el diccionario por pantalla
print(titulares)
