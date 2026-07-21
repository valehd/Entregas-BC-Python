# MediTrack

Mini sistema de gestión de equipos médicos desarrollado en Python.

## Descripción

MediTrack permite registrar equipos médicos, asignarles un estado y visualizar los equipos almacenados. Además, genera un archivo de reporte en formato `.txt`.

Este proyecto fue creado como parte de la evaluación del Módulo 3 de Python.

## Funcionalidades

* Registrar equipos médicos.
* Seleccionar el estado del equipo (Operativo, Mantenimiento o Fuera de servicio).
* Mostrar la lista de equipos registrados.
* Generar un archivo `reporte.txt` con la información de los equipos.

## Estructuras de datos utilizadas

* **Lista (`list`)**: almacena los equipos registrados.
* **Diccionario (`dict`)**: guarda los datos de cada equipo.
* **Tupla (`tuple`)**: contiene los estados válidos del sistema.

## Archivos del proyecto

* `main.py` → menú principal del sistema.
* `equipos.py` → funciones para registrar y mostrar equipos.
* `utilidades.py` → generación del reporte.
* `reporte.txt` → archivo de salida generado por el sistema.

## Cómo ejecutar

Desde la terminal, ejecutar:

```bash
python main.py
```

## Autor

Valentina Hernández
