def generar_reporte(lista_equipos):
    with open('reporte.txt', 'w', encoding='utf-8') as archivo:
        archivo.write('REPORTE DE EQUIPOS\n\n')

        for equipo in lista_equipos:
            archivo.write(
                
                f'Código equipo: {equipo["codigo"]}\n'
                f'Nombre equipo: {equipo["nombre"]}\n'
                f'Estado: {equipo["estado"]}\n\n'
            )

    print('\nReporte generado con éxito')


def cuenta_regresiva(n):
    if n == 0:
        return 0
    return 1 + cuenta_regresiva(n - 1)