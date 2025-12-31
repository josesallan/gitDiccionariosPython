materias = {}
materias["martes"] = 6201
materias["miércoles"] = [6103, 7540]
print(materias.get("domingo", 'No'))
print(materias.get("martes", 'No'))
for dia in materias:
    print(dia, ":", materias[dia])
for dia, codigos in materias.items():
    print(codigos)
