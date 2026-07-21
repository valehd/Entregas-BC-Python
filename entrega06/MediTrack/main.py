from equipos import registrar_equipo, mostrar_equipos
from utilidades import generar_reporte

equipos = []

while True:
    print('\n=== MEDITRACK ===')
    print('1. Registrar equipo')
    print('2. Mostrar equipos')
    print('3. Generar reporte')
    print('4. Salir')

    opcion = input('\nSeleccione una opción: ')

    if opcion == '1':
        registrar_equipo(equipos)

    elif opcion == '2':
        mostrar_equipos(equipos)

    elif opcion == '3':
        generar_reporte(equipos)

    elif opcion == '4':
        print('Saliendo...')
        break

    else:
        print('\nOpción inválida')


print('Prueba recursiva:', cuenta_regresiva(3))