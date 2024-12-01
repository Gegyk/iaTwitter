from Constantes import archivos
import json

"""
Metodos del archivo tweetsNoEntrenados
"""
def guardarTweetNoEntrenado(tweet):    
    # Cargar el archivo JSON
    with open(archivos.TWEETSNOENTRENADOS_01, 'r') as file:
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
    """
    Lee un archivo JSON con tweets y devuelve un string con los tweets concatenados,
    separados por un punto (.).
    
    Args:
        ruta_json (str): Ruta al archivo JSON.

    Returns:
        str: Tweets concatenados separados por un punto.
    """    

    # Leer el archivo JSON
    with open(archivos.TWEETSNOENTRENADOS_01, 'r') as file:
        data = json.load(file)
    
    # Obtener la lista de tweets
    tweets = data.get("tweetsNoEntrenados", [])
    
    # Concatenar los tweets separados por un punto
    tweets_concatenados = ". \n\n".join(tweets)
    
    return tweets_concatenados



        
"""
Metodos del archivo tweetsEntrenados
"""
def guardarTweetEntrenado(tweet):
    # Cargar el archivo JSON
    with open(archivos.TWEETSENTRENADOS_01, 'r') as file:
        data = json.load(file)

    # Agregar un nuevo seguidor    
    data["tweetsEntrenados"].append(tweet)

    # Guardar los cambios en el archivo JSON
    with open(archivos.TWEETSENTRENADOS_01, 'w') as file:
        json.dump(data, file, indent=4)


def comprobarTweetRepetido(tweet):
    with open(archivos.TWEETSENTRENADOS_01, 'r') as file:
        data = json.load(file)
                
    # Obtener la lista de tweets
    tweets = data.get("tweetsEntrenados", [])
    
     # Verificar si el tweet ya está en la lista de tweets entrenados
    if tweet in tweets:
        return True  
    else:
        return False 
