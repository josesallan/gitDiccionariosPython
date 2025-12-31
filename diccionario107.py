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

# (5)Creamos una copia de la biblioteca titulares y la llamamos plantilla.
plantilla = titulares.copy()
# Mostraremos ahora los elementos de la biblioteca con la misma forma que en el 2.

#(6)Creo la biblioteca suplentes
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
print()
# Añadimos los elementos de suplentes al diccionario plantilla
plantilla.update(suplentes)
# Mostramos los resultados
print()
print('Plantilla selección 2010')
print('------------------------')
for i in range(1, 99, 1):
    if plantilla.get(i, 'No') == 'No':
        continue
    else:
        print(i, '\t->', plantilla.get(i))
