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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loadData(catalog):

    loadUFOs(catalog)

def loadUFOs(catalog):
    UFOsFile = cf.data_dir + 'UFOS-utf8-large.csv'
    input_file = csv.DictReader(open(UFOsFile, encoding='utf-8'))
    for UFO in input_file:
        model.addUFO(catalog, UFO)


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def getUFOsByCity(catalog,cityName):
    return model.getUFOsByCity(catalog,cityName)

def getLargestDuration(catalog):
    return model.getLargestDuration(catalog)

def getUFOsByRange(catalog,inf,sup):
    return model.getUFOsByRange(catalog,inf,sup)

def getUFOsByTime(catalog,timeInf,timeSup):
    return model.getUFOsByTime(catalog,timeInf,timeSup)

def getOldestDate(catalog):
    return model.getOldestDate(catalog)

def getUFOsByDate(catalog,dateInf,dateSup):
    return model.getUFOsByDate(catalog,dateInf,dateSup)

def getUFOsByCoordinates(catalog,longInf,longSup,latInf,latSup):
    return model.getUFOsByCoordinates(catalog,longInf,longSup,latInf,latSup)
