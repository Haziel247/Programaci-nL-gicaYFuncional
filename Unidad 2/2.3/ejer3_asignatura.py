
asignatura_VII = ["Progrmacion lógica"] #lista con asignatura
print(asignatura_VII)

asignatura_nueva = asignatura_VII + ["Programacion web"] #lista nueva
print(asignatura_nueva)

def agregar_asignatura(lista, asignatura):
    return lista + asignatura

print(agregar_asignatura(asignatura_VII, ["Administración de redes"]))

