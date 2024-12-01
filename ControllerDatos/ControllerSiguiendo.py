from Constantes import archivos
import json
import random

def getSeguidores():
    # Cargar el JSON desde un archivo
    with open(archivos.SIGUIENDO_01, 'r') as file:
        data = json.load(file)

    # Extraer la lista de seguidores
    seguidores = data.get("siguiendo", [])

    return seguidores

def getSeguidorAleatorio():
    """
    Devuelve un seguidor aleatorio de la lista obtenida por getSeguidores.
    """
    seguidores = getSeguidores()
    if seguidores:  # Verifica que la lista no esté vacía
        return random.choice(seguidores)
    else:
        return "No hay seguidores disponibles"