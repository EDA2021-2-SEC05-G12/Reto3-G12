"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import time 

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Contar los avistamientos en una ciudad")
    print("3- Contar los avistamientos por duración")
    print("4- Contar avistamientos en un rango de horas del día")
    print("5- Contar los avistamientos en un rango de fechas")
    print("6- Contar los avistamientos de una zona geográfica")
    print("0- Salir")

def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    return controller.loadData(catalog)

def printResults(first3,last3):
    print('Fecha y hora\t\tCiudad, País\t\tDuración (s)\t\tForma del objeto')
    for i in range(1, 4):
        ufo = lt.getElement(first3, i)
        datetime = ufo['datetime']
        city = ufo['city']
        country = ufo['country']
        durationSec = ufo['duration (seconds)']
        shape = ufo['shape']
        print(f'{datetime}\t\t{city}, {country}\t\t{durationSec}\t\t{shape}')

    for i in range(1, 4):
        ufo = lt.getElement(last3, i)
        datetime = ufo['datetime']
        city = ufo['city']
        country = ufo['country']
        durationSec = ufo['duration (seconds)']
        shape = ufo['shape']
        print(f'{datetime}\t\t{city}, {country}\t\t{durationSec}\t\t{shape}')

def printFifthRequirement(first5,last5):
    print('Fecha y hora\t\tCiudad, País\t\tDuración (s)\t\tForma del objeto\t\tLatitud\t\tLongitud')
    for i in range(1, 6):
        ufo = lt.getElement(first5, i)
        datetime = ufo['datetime']
        city = ufo['city']
        country = ufo['country']
        durationSec = ufo['duration (seconds)']
        shape = ufo['shape']
        latitude = ufo['latitude']
        longitude = ufo['longitude']
        print(f'{datetime}\t\t{city}, {country}\t\t{durationSec}\t\t{shape}\t\t{latitude}\t\t{longitude}')

    for i in range(1, 6):
        ufo = lt.getElement(last5, i)
        datetime = ufo['datetime']
        city = ufo['city']
        country = ufo['country']
        durationSec = ufo['duration (seconds)']
        shape = ufo['shape']
        latitude = ufo['latitude']
        longitude = ufo['longitude']
        print(f'{datetime}\t\t{city}, {country}\t\t{durationSec}\t\t{shape}\t\t{latitude}\t\t{longitude}')


# Funciones de búsqueda
def getUFOsByCity(catalog,cityName):
    return controller.getUFOsByCity(catalog,cityName)

def getLargestDuration(catalog):
    return controller.getLargestDuration(catalog)

def getUFOsByRange(catalog,inf,sup):
    return controller.getUFOsByRange(catalog,inf,sup)

def getUFOsByTime(catalog,timeInf,timeSup):
    return controller.getUFOsByTime(catalog,timeInf,timeSup)

def getOldestDate(catalog):
    return controller.getOldestDate(catalog)

def getUFOsByDate(catalog,dateInf,dateSup):
    return controller.getUFOsByDate(catalog,dateInf,dateSup)

def getUFOsByCoordinates(catalog,longInf,longSup,latInf,latSup):
    return controller.getUFOsByCoordinates(catalog,longInf,longSup,latInf,latSup)


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1: # Carga de datos
        start_time = time.process_time()
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        # Imprimimos el total de avistamientos
        sizeUFOs = lt.size(catalog['UFOs'])
        print(f'Avistamientos cargados: {sizeUFOs}')

        # Primeros y últimos 5 avistamientos
        firstOnes = list(range(1,6))
        lastOnes = list(range(sizeUFOs-4,sizeUFOs+1))

        # Primeros 5
        print()
        print('Primeros 5 avistamientos:')
        print('Fecha\t\tCiudad\t\tForma\t\tDuración (s)')
        for i in firstOnes:
            UFO = lt.getElement(catalog['UFOs'],i)
            datetime = UFO['datetime']
            city = UFO['city']
            shape = UFO['shape']
            durationSec = UFO['duration (seconds)']
            print(f'{datetime}\t\t{city}\t\t{shape}\t\t{durationSec}')

        # Últimos 5
        print()
        print('Últimos 5 avistamientos:')
        print('Fecha\t\tCiudad\t\tForma\t\tDuración (s)')
        for i in lastOnes:
            UFO = lt.getElement(catalog['UFOs'], i)
            datetime = UFO['datetime']
            city = UFO['city']
            shape = UFO['shape']
            durationSec = UFO['duration (seconds)']              
            print(f'{datetime}\t\t{city}\t\t{shape}\t\t{durationSec}')
        stop_time = time.process_time()
        etms = (stop_time - start_time)*1000
        print('El tiempo de ejecucion es ' + str(etms) + 'ms')

    elif int(inputs[0]) == 2: # Requerimiento 1
        start_time = time.process_time()
        cityName = input('Ingrese el nombre de la ciudad: ')
        cityUFOs = getUFOsByCity(catalog,cityName)
        # El total de avistamientos
        totalUFOs = lt.size(cityUFOs)
        first3 = lt.subList(cityUFOs,1,3) # Primeros 3
        last3 = lt.subList(cityUFOs,totalUFOs-2,3) # Últimos 3

        #Imprimimos info:
        print(f'Se han presentado {totalUFOs} avistamientos en la ciudad de {cityName}.')
        print()
        print('A continuación, los primeros y últimos 3 avistamientos listados cronológicamente:')
        print()
        printResults(first3,last3)
        stop_time = time.process_time()
        etms = (stop_time - start_time)*1000
        print('El tiempo de ejecucion es ' + str(etms) + 'ms')

    elif int(inputs[0]) == 3: # Requerimiento 2
        start_time = time.process_time()
        inf = int(input('Ingrese el límite inferior (en segundos): '))
        sup = int(input('Ingrese el línimte superior (en segundos): '))
        largest,sizeLargest = getLargestDuration(catalog)

        # Primera parte de la impresión:
        print(f'La duración más larga fue de {largest} segundos, con un total de {sizeLargest} avistamientos')
        print()

        # Segunda parte: avistamientos dentro del rango.
        UFOsInRange = getUFOsByRange(catalog,inf,sup)
        sizeInRange = lt.size(UFOsInRange)
        first3 = lt.subList(UFOsInRange,1,3)
        last3 = lt.subList(UFOsInRange,sizeInRange-2,3)

        print('A continuación, los primeros y últimos 3 avistamientos dentro del rango de duración')
        printResults(first3,last3)
        stop_time = time.process_time()
        etms = (stop_time - start_time)*1000
        print('El tiempo de ejecucion es ' + str(etms) + 'ms')

    elif int(inputs[0]) == 4: # Requerimiento 3
        start_time = time.process_time()
        timeInf = input('Ingrese el límite inferior (HH:MM): ')
        timeSup = input('Ingrese el límite superior (HH:MM): ')
        UFOsInRange = getUFOsByTime(catalog,timeInf,timeSup)
        sizeInRange = lt.size(UFOsInRange)
        # Imprimimos el total en el rango
        print(f'Se encontraron {sizeInRange} avistamientos en el rango entre las {timeInf} y las {timeSup}.')
        print()
        # Imprimimos los tres primeros y últimos.
        first3 = lt.subList(UFOsInRange, 1, 3)
        last3 = lt.subList(UFOsInRange, sizeInRange - 2, 3)
        print('A continuación, los primeros y últimos 3 avistamientos dentro del rango de horas')
        printResults(first3,last3)
        stop_time = time.process_time()
        etms = (stop_time - start_time)*1000
        print('El tiempo de ejecucion es ' + str(etms) + 'ms')

    elif int(inputs[0]) == 5: # Requerimiento 4
        start_time = time.process_time()
        dateInf = input('Ingrese el límite inferior (AAAA-MM-DD): ')
        dateSup = input('Ingrese el límite superior (AAAA-MM-DD): ')
        UFOsInRange = getUFOsByDate(catalog, dateInf, dateSup)
        sizeInRange = lt.size(UFOsInRange)
        # Imprimimos la fecha más antigua y la cantidad de avistamientos
        oldest,sizeOldest = getOldestDate(catalog)
        print(f'La fecha más antigua registrada es {oldest}, con un total de {sizeOldest} avistamientos')
        print()

        # Imprimimos el total en el rango
        print(f'Se encontraron {sizeInRange} avistamientos en el rango entre {dateInf} y {dateSup}.')
        print()
        # Imprimimos los tres primeros y últimos.
        first3 = lt.subList(UFOsInRange, 1, 3)
        last3 = lt.subList(UFOsInRange, sizeInRange - 2, 3)
        print('A continuación, los primeros y últimos 3 avistamientos dentro del rango de fechas')
        printResults(first3, last3)
        stop_time = time.process_time()
        etms = (stop_time - start_time)*1000
        print('El tiempo de ejecucion es ' + str(etms) + 'ms')

    elif int(inputs[0]) == 6: # Requerimiento 5
        start_time = time.process_time()
        longInf,longSup = input('Ingrese los límites mínimo y máximo de longitud (Separados por espacio y usando . como separador): ').split(' ')
        latInf, latSup = input('Ingrese los límites mínimo y máximo de latitud (Separados por espacio y usando . como separador): ').split(' ')
        UFOsInCoordinates = getUFOsByCoordinates(catalog,longInf,longSup,latInf,latSup)
        sizeInCoordinates = lt.size(UFOsInCoordinates)
        # Total de avistamientos:
        print(f'Se hallaron {sizeInCoordinates} avistamientos en el rango de coordenadas ingresadas')
        # Imprimimos los cinco primeros y últimos.
        first5 = lt.subList(UFOsInCoordinates, 1, 5)
        last5 = lt.subList(UFOsInCoordinates, sizeInCoordinates-4, 5)
        print('A continuación, los primeros y últimos 5 avistamientos dentro del rango de coordenadas')
        printFifthRequirement(first5,last5)
        stop_time = time.process_time()
        etms = (stop_time - start_time)*1000
        print('El tiempo de ejecucion es ' + str(etms) + 'ms')

    else:
        sys.exit(0)
sys.exit(0)
