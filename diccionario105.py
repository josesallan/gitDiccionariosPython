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
print('Plantilla selección 2010')
print('------------------------')
for i in range(1, 99, 1):
    if plantilla.get(i, 'No') == 'No':
        continue
    else:
        print(i, '\t->', plantilla.get(i))
