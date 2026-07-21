



def generar_reporte(lista_equipos):
    total = contar_equipos(lista_equipos)
    with open('reporte.txt', 'w', encoding='utf-8') as archivo:
        archivo.write('REPORTE DE EQUIPOS\n\n')

        for equipo in lista_equipos:
            archivo.write(
                
                f'Código equipo: {equipo["codigo"]}\n'
                f'Nombre equipo: {equipo["nombre"]}\n'
                f'Estado: {equipo["estado"]}\n\n'
            )
        archivo.write('\n')
        archivo.write(f'TOTAL DE EQUIPOS: {total}\n')

    print('\nReporte generado con éxito')


def contar_equipos(lista_equipos):
    if lista_equipos == []:
        return 0
    return 1 + contar_equipos(lista_equipos[1:])