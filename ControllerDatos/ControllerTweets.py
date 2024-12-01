import json
import re
from Constantes import archivos

"""
Métodos del archivo tweetsNoEntrenados
"""
def guardarTweetNoEntrenado(tweet):
    tweet = limpiarTexto(tweet)   
    
    # Cargar el archivo JSON
    with open(archivos.TWEETSNOENTRENADOS_01, 'r', encoding="utf-8") as file:
        data = json.load(file)

    # Agregar un nuevo tweet  
    data["tweetsNoEntrenados"].append(tweet)

    # Guardar los cambios en el archivo JSON
    with open(archivos.TWEETSNOENTRENADOS_01, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)  # Asegúrate de que los caracteres no sean convertidos

def borrarDatosTweetNoEntrenado():
    data = {
        "tweetsNoEntrenados": []  # Lista vacía para borrar los tweets no entrenados
    }

    with open(archivos.TWEETSNOENTRENADOS_01, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)  # Asegúrate de que los caracteres no sean convertidos
        
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
Métodos del archivo tweetsEntrenados
"""
def guardarTweetEntrenado(tweet):
    # Cargar el archivo JSON
    with open(archivos.TWEETSENTRENADOS_01, 'r', encoding="utf-8") as file:
        data = json.load(file)

    # Agregar un nuevo tweet    
    data["tweetsEntrenados"].append(tweet)

    # Guardar los cambios en el archivo JSON
    with open(archivos.TWEETSENTRENADOS_01, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)  # Asegúrate de que los caracteres no sean convertidos


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
Métodos de uso global
"""

def limpiarTexto(texto):
    # Elimina URLs
    texto = re.sub(r"http\S+", "", texto)
    # Elimina menciones (@usuario)
    texto = re.sub(r"@\w+", "", texto)
    # Elimina caracteres no alfabéticos pero dejando los caracteres especiales como emojis y varios símbolos
    texto = re.sub(r"[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s\ud83c-\ud83e!\"#$%&'()*+,-./0123456789:;<=>?@[\]^_`{|}~¡¿¥©®™§°±∑π∞≠≤≥←↑→↓∩∪⊆⊂⊇⊃⊥⊗⊙⋯⊕ℂℕℝℤ∀∃∑∈∉≈≡≪≫∫∮]", "", texto)
    # Elimina saltos de línea y otros caracteres de control como tabulaciones
    texto = re.sub(r"[\n\t\r]", " ", texto)  # Reemplaza saltos de línea, tabulaciones y retorno de carro por espacios
    # Convierte a minúsculas
    texto = texto.lower()
    return texto


