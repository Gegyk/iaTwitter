from Constantes import archivos
import json
import re

"""
Metodos del archivo tweetsNoEntrenados
"""
def guardarTweetNoEntrenado(tweet):
    tweet = limpiarTexto(tweet)   
     
    # Cargar el archivo JSON
    with open(archivos.TWEETSNOENTRENADOS_01, 'r', encoding="utf-8") as file:
        data = json.load(file)

    # Agregar un nuevo tweet  
    data["tweetsNoEntrenados"].append(tweet)

    # Guardar los cambios en el archivo JSON
    with open(archivos.TWEETSNOENTRENADOS_01, 'w') as file:
        json.dump(data, file, indent=4)

def borrarDatosTweetNoEntrenado():
    data = {
        "tweetsNoEntrenados": []  # Lista vacía para borrar los tweets no entrenados
    }

    with open(archivos.TWEETSNOENTRENADOS_01, 'w') as file:
        json.dump(data, file, indent=4) 
        
def getTweetsNoEntrenadosText():
    # Leer el archivo JSON
    with open(archivos.TWEETSNOENTRENADOS_01, 'r', encoding="utf-8") as file:
        data = json.load(file)
    
    # Obtener la lista de tweets
    tweets = data.get("tweetsNoEntrenados", [])
    
    # Concatenar los tweets separados por un punto
    tweets_concatenados = ". ".join(tweets)        
    return tweets_concatenados



        
"""
Metodos del archivo tweetsEntrenados
"""
def guardarTweetEntrenado(tweet):
    # Cargar el archivo JSON
    with open(archivos.TWEETSENTRENADOS_01, 'r', encoding="utf-8") as file:
        data = json.load(file)

    # Agregar un nuevo seguidor    
    data["tweetsEntrenados"].append(tweet)

    # Guardar los cambios en el archivo JSON
    with open(archivos.TWEETSENTRENADOS_01, 'w') as file:
        json.dump(data, file, indent=4)


def comprobarTweetRepetido(tweet):
    tweet = limpiarTexto(tweet)
    with open(archivos.TWEETSENTRENADOS_01, 'r', encoding="utf-8") as file:
        data = json.load(file)
                
    # Obtener la lista de tweets
    tweets = data.get("tweetsEntrenados", [])
    
     # Verificar si el tweet ya está en la lista de tweets entrenados
    if tweet in tweets:
        return True  
    else:
        return False 




"""
Metodos de uso global
"""

def limpiarTexto(texto):
    # Elimina URLs
    texto = re.sub(r"http\S+", "", texto)
    # Elimina menciones (@usuario)
    texto = re.sub(r"@\w+", "", texto)
    # Elimina caracteres no alfabéticos y emojis
    texto = re.sub(r"[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]", "", texto)
    # Convierte a minúsculas
    texto = texto.lower()
    return texto