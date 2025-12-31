# Creamos el diccionario y añadimos los elementos
titulares = {}
titulares[1] = 'Casillas'
titulares[3] = 'Pique'
titulares[5] = 'Puyol'
titulares[6] = 'Iniesta'
titulares[7] = 'Villa'
titulares[8] = 'Xavi Hernández'
titulares[11] = 'Capdevila'
titulares[14] = 'Xabi Alonso'
titulares[15] = 'Ramos'
titulares[16] = 'Busquets'
titulares[18] = 'Pedrito'

# (5)Creamos una copia de la biblioteca titulares y la llamamos final.
final = titulares.copy()
# Eliminamos los tres jugadores sustituidos
final.pop(14)  # Xabi Alonso
final.pop(18)  # Pedrito
final.pop(7)  # Villa
# Añadimos los tres jugadores sustituidos
final.setdefault(22, 'Navas')
final.setdefault(10, 'Fàbregas')
final.setdefault(9, 'Torres')

# Mostramos los resultados
print()
print('Final partido 2010')
print('------------------')
for i in range(1, 99, 1):
    if final.get(i, 'No') == 'No':
        continue
    else:
        print(i, '\t->', final.get(i))
