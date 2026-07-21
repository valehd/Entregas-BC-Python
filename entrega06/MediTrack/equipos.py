# Tupla con los estados válidos (inmutable)
ESTADOS = (
    'Operativo',
    'Mantenimiento',
    'Fuera de servicio'
)


def registrar_equipo(lista_equipos):
    codigo = input('Código: ')
    nombre = input('Nombre: ')

    print('\nEstados disponibles:')
    for i, estado in enumerate(ESTADOS, start=1):
        print(f'{i}. {estado}')

    opcion = input('Seleccione un estado (1-3): ')

    # Validar la opción
    if opcion in ('1', '2', '3'):
        estado = ESTADOS[int(opcion) - 1]
    else:
        print('\nOpción inválida. Se asignará "Operativo" por defecto.')
        estado = ESTADOS[0]

    equipo = {
        'codigo': codigo,
        'nombre': nombre,
        'estado': estado
    }

    lista_equipos.append(equipo)
    print('\nEquipo registrado exitosamente')


def mostrar_equipos(lista_equipos):
    if len(lista_equipos) == 0:
        print('\nNo hay equipos registrados')
        return

    print('\n--- LISTA DE EQUIPOS ---\n')

    for equipo in lista_equipos:
        print(
            f'Código equipo: {equipo["codigo"]}\n'
            f'Nombre: {equipo["nombre"]}\n'
            f'Estado: {equipo["estado"]}\n'
        )