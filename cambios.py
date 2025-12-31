# Añado el código necesario para conseguir que la aplicación funcione de forma
# elegante desde consola

# Importo el módulo os que permitirá manejar funciones dependientes del Sitema
# operativo
import os


# Creo una función para borrar la pantalla
def borrar():
    # Selecc la orden que hará el borrado en función de Sistema operativo utili.
    if os.name == "posix":
        var = "clear"
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        var = "cls"
    # borro pantalla
    os.system(var)


# En este ejercicio final es necesario evitar que un jugador que ya ha sido
# sustituido pueda entrar de nuevo al campo.  Para evitarlo, cuando "siente" a
# un jugador no sólo guardaré su dorsal como índice y su nombre como valor en la
# tabla suplentes.  También mofidicaré su nombre para que comience por "S-...".
# Antes de hacer el cambio habrá que comprobar si el nombre del que entra
# empieza por S- y en ese caso no se hará"
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


# Mostramos los resultados, en esta versión creo una función que muestre a la
# titulares y suplentes.  El truco es que como el número de jugadores y suplent.
# es once, las dos columnas tienen la misma longitud.  Mostraré un suplente
# cada vez que lea un titular y lo pondré en la misma línea.
# guardaré el número del suplente en una variable y al escribir el siguiente
# titular buscaré el suplente siguiente al anterior
def mostrar_jugadores():
    borrar()
    ultimo_suplente = 0
    print("                   Gestor de cambios")
    print("                   =================")
    print()

    print()
    print('    Jugando en el campo          Suplentes')
    print('    -------------------          ---------')
    for i in range(1, 99, 1):
        if titulares.get(i, 'No') == 'No':
            continue
        else:
            # Muestro el nombre de los jugadores de campo
            # El if me permite tabular de forma correcta los datos
            if i < 10:
                print('   ', i, ' ->', titulares.get(i), end="       ")
            else:
                print('   ', i, '->', titulares.get(i), end="       ")

            # Para tabular los suplentes necesito conocer la longitud de la cadena del jugador de campo
            longitud = 4 + len(titulares.get(i))

            # Cada vez que leo un jugador de campo debo leer el siguiente suplente en la misma línea

            for j in range(ultimo_suplente + 1, 99, 1):
                if suplentes.get(j, 'No') == 'No':
                    continue
                else:
                    espacio = 20 - longitud
                    print(espacio * " ", end="")
                    if j < 10:
                        print(j, ' ->', suplentes.get(j))
                    else:
                        print(j, '->', suplentes.get(j))
                    ultimo_suplente = j
                    break
    print()


mostrar_jugadores()
cambio = 1
# Con un bucle while controlamos el número de cambios
while cambio <= 3:
    if cambio == 1:
        print("No has realizado ningún cambio.  Todavía puedes hacer tres cambios.")
    elif cambio == 2:
        print("Has realizado un cambio.  Todavía puedes hacer otros dos.")
    elif cambio == 3:
        print("Ya has realizado dos cambios.  Solo puedes hacer un cambio más.")

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
        print('Jugador a sustituir:', nombresale, '\t\tnúmero:', sale)
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
        # En primer lugar comprobamos si el jugador todavía no ha sido sustituido
        # Leo las dos primeras letras de su nombre
        comprobacion = nombreentra[0:2]
        if comprobacion != 'S-':
            print('Jugador a sustituir:', nombresale, '\t\tnúmero:', sale)
            print('Jugador que entra en su lugar:', nombreentra, '\tnúmero:', entra)
            # Es en este momento cuando puedo realizar la sustitución
            ###########################################################################
            # Cambio el nombre del jugador que sale para que su formato no le deje volver a entrar
            nombresale = 'S-' + nombresale
            # Elimino al jugador sustituido del diccionario titulares
            titulares.pop(sale)
            # Elimino al jugador que entra del diccionario suplentes
            suplentes.pop(entra)
            # Añado el jugador que entra al diccionario titulares
            titulares.setdefault(entra, nombreentra)
            # Añado el jugador que sale al diccionario suplentes
            suplentes.setdefault(sale, nombresale)
            # Necesito indicar de alguna manera que jugarores ya han sido sustituidos
            # Muestro los resultados actualizados
            mostrar_jugadores()
        else:
            # Muestro un mensaje con el nombre del jugador [2:] hace que no lea los dos primeros caracteres
            print(nombreentra[2:], ' no puede volver al campo')
            continue
        # Incrementamos el resultado de la variable cambio
        cambio = cambio + 1
print('Ya has realizado las tres sustituciones')
input()
