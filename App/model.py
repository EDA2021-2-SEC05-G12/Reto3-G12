"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import orderedmap as om
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {'UFOs': lt.newList('ARRAY_LIST'),
               'cities': mp.newMap(numelements=1000, maptype = 'PROBING', loadfactor = 4.0),
               'durations': om.newMap(),
               'times': om.newMap(),
               'dates': om.newMap(),
               'longitudes': om.newMap()}

    return catalog

# Funciones para agregar informacion al catalogo

def addUFO(catalog,UFO):
    lt.addLast(catalog['UFOs'],UFO)
    addUFOCity(catalog,UFO)
    addUFODuration(catalog,UFO)
    addUFOTime(catalog,UFO)
    addUFODate(catalog,UFO)
    addUFOLongitude(catalog,UFO)

def addUFOCity(catalog,UFO):
    try:
        cities = catalog['cities']
        cityName = UFO['city']
        if cityName == "":
            cityName = 'unknown'
        existCity = mp.contains(cities,cityName)
        if existCity:
            entry = mp.get(cities,cityName)
            city = me.getValue(entry)
        else:
            city = newCity(cityName)
            mp.put(cities,cityName,city)
        lt.addLast(city['UFOs'],UFO)
    except Exception:
        return None

def newCity(cityName):
    entry = {'city': cityName,
             'UFOs': lt.newList('ARRAY_LIST')}
    return entry

def addUFODuration(catalog,UFO):
    try:
        durations = catalog['durations']
        seconds = UFO['duration (seconds)']
        if seconds == '':
            seconds = '0'
        seconds = float(seconds)
        existDuration = om.contains(durations,seconds)
        if existDuration:
            entry = om.get(durations,seconds)
            duration = me.getValue(entry)
        else:
            duration = newDuration(seconds)
            om.put(durations,seconds,duration)
        lt.addLast(duration['UFOs'],UFO)
    except Exception:
        return None

def newDuration(seconds):
    entry = {'duration': seconds, 'UFOs': lt.newList('ARRAY_LIST')}
    return entry

def addUFOTime(catalog,UFO):
    try:
        times = catalog['times']
        datetime = UFO['datetime']
        timeNumber = int(datetime.split(' ')[1].replace(':',''))
        existTime = om.contains(times,timeNumber)
        if existTime:
            entry = om.get(times,timeNumber)
            time = me.getValue(entry)
        else:
            time = newTime(timeNumber)
            om.put(times,timeNumber,time)
        lt.addLast(time['UFOs'],UFO)
    except Exception:
        return None

def newTime(timeNumber):
    entry = {'time': timeNumber, 'UFOs': lt.newList('ARRAY_LIST')}
    return entry

def addUFODate(catalog,UFO):
    try:
        dates = catalog['dates']
        datetime = UFO['datetime']
        dateNumber = int(datetime.split(' ')[0].replace('-',''))
        existDate = om.contains(dates,dateNumber)
        if existDate:
            entry = om.get(dates,dateNumber)
            date = me.getValue(entry)
        else:
            date = newTime(dateNumber)
            om.put(dates,dateNumber,date)
        lt.addLast(date['UFOs'],UFO)
    except Exception:
        return None

def newDate(dateNumber):
    entry = {'date': dateNumber, 'UFOs': lt.newList('ARRAY_LIST')}
    return entry

def addUFOLongitude(catalog,UFO):
    try:
        longitudes = catalog['longitudes']
        longitudeNumber = UFO['longitude']
        if longitudeNumber == '':
            longitudeNumber = '0'
        longitudeNumber = round(float(longitudeNumber),2)
        existLongitude = om.contains(longitudes,longitudeNumber)
        if existLongitude:
            entry = om.get(longitudes,longitudeNumber)
            longitude = me.getValue(entry)
        else:
            longitude = newLongitude(longitudeNumber)
            om.put(longitudes,longitudeNumber,longitude)
        addUFOLatitude(longitude,UFO)
    except Exception:
        return None

def newLongitude(longitudeNumber):
    entry = {'longitude': longitudeNumber,
             'latitudes': om.newMap()}

    return entry

def addUFOLatitude(longitude,UFO):
    try:
        latitudes = longitude['latitudes']
        latitudeNumber = UFO['latitude']
        if latitudeNumber == '':
            latitudeNumber = '0'
        latitudeNumber = round(float(latitudeNumber),2)
        existLatitude = om.contains(latitudes,latitudeNumber)
        if existLatitude:
            entry = om.get(latitudes,latitudeNumber)
            latitude = me.getValue(entry)
        else:
            latitude = newLatitude(latitudeNumber)
            om.put(latitudes,latitudeNumber,latitude)

        lt.addLast(latitude['UFOs'],UFO)
    except Exception:
        return None

def newLatitude(latitudeNumber):
    entry = {'latitude': latitudeNumber,
             'UFOs': lt.newList('ARRAY_LIST')}

    return entry

# Funciones para creacion de datos

# Funciones de consulta

def getUFOsByCity(catalog,cityName):
    entry = mp.get(catalog['cities'],cityName)
    UFOs = me.getValue(entry)['UFOs']
    UFOs = sa.sort(UFOs,compareByDate)
    return UFOs

def getLargestDuration(catalog):
    durations = catalog['durations']
    values = om.keySet(durations)
    largest = lt.lastElement(values)
    entry = om.get(durations,largest)
    ufos = me.getValue(entry)['UFOs']
    size = lt.size(ufos)

    return largest,size

def getUFOsByRange(catalog,inf,sup):
    durations = catalog['durations']
    subSets = om.values(durations,inf,sup)
    selectedUFOs = lt.newList('ARRAY_LIST')
    for i in range(1,lt.size(subSets)+1):
        subSet = lt.getElement(subSets,i)['UFOs']
        subSet = sa.sort(subSet,compareByCity)
        for j in range(1,lt.size(subSet)+1):
            UFO = lt.getElement(subSet,j)
            lt.addLast(selectedUFOs,UFO)

    return selectedUFOs

def getUFOsByTime(catalog,timeInf,timeSup):
    timeInf = int(timeInf.replace(':','')+'00')
    timeSup = int(timeSup.replace(':','')+'00')
    times = catalog['times']
    subSets = om.values(times,timeInf,timeSup)
    selectedUFOs = lt.newList('ARRAY_LIST')
    for i in range(1,lt.size(subSets)+1):
        subSet = lt.getElement(subSets,i)['UFOs']
        subSet = sa.sort(subSet,compareByDate)
        for j in range(1,lt.size(subSet)+1):
            UFO = lt.getElement(subSet,j)
            lt.addLast(selectedUFOs,UFO)

    return selectedUFOs

def getOldestDate(catalog):
    dates = catalog['dates']
    oldest = om.minKey(dates)
    entry = om.get(dates,oldest)
    ufos = me.getValue(entry)['UFOs']
    size = lt.size(ufos)
    year = str(oldest)[0:4]
    month = str(oldest)[4:6]
    day = str(oldest)[6:8]
    oldest = f'{year}-{month}-{day}'

    return oldest,size

def getUFOsByDate(catalog,dateInf,dateSup):
    dateInf = int(dateInf.replace('-',''))
    dateSup = int(dateSup.replace('-',''))
    dates = catalog['dates']
    subSets = om.values(dates,dateInf,dateSup)
    selectedUFOs = lt.newList('ARRAY_LIST')
    for i in range(1,lt.size(subSets)+1):
        subSet = lt.getElement(subSets,i)['UFOs']
        subSet = sa.sort(subSet,compareByDate)
        for j in range(1,lt.size(subSet)+1):
            UFO = lt.getElement(subSet,j)
            lt.addLast(selectedUFOs,UFO)

    return selectedUFOs

def getUFOsByCoordinates(catalog,longInf,longSup,latInf,latSup):
    longInf = round(float(longInf),2)
    longSup = round(float(longSup), 2)
    latInf = round(float(latInf), 2)
    latSup = round(float(latSup), 2)
    longitudes = catalog['longitudes']
    print(om.minKey(longitudes))
    latitudesMaps = om.values(longitudes,longInf,longSup)
    selectedUFOs = lt.newList('ARRAY_LIST')
    for i in range(1,lt.size(latitudesMaps)+1):
        map = lt.getElement(latitudesMaps,i)['latitudes']
        subSets = om.values(map,latInf,latSup)
        for j in range(1,lt.size(subSets)+1):
            ufos = lt.getElement(subSets,j)['UFOs']
            for k in range(1,lt.size(ufos)+1):
                ufo = lt.getElement(ufos,k)
                lt.addLast(selectedUFOs,ufo)

    return selectedUFOs



# Funciones utilizadas para comparar elementos dentro de una lista
def compareByDate(UFO1,UFO2):
    datetime1 = UFO1['datetime'].split(' ')
    date1 = datetime1[0].replace('-','')
    time1 = datetime1[1].replace(':','')
    number1 = int(date1+time1)

    datetime2 = UFO2['datetime'].split(' ')
    date2 = datetime2[0].replace('-', '')
    time2 = datetime2[1].replace(':', '')
    number2 = int(date2 + time2)

    return number1 < number2

def compareByCity(UFO1,UFO2):
    city1 = UFO1['city']
    city2 = UFO2['city']

    return city1 < city2

# Funciones de ordenamiento


