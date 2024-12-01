from Constantes import archivos
from Texto import texto as Texto
from Modelo import modelo as Modelo
from Twitter import TwitterApi as TwApi
from ControllerDatos import ControllerTweets as ContTweets
from ControllerDatos import ControllerSiguiendo as ContSeg
import os
import time

while True:
    cuentaSeguida =  ContSeg.getSeguidorAleatorio()    
    tweets = TwApi.getUltimoTweet(cuentaSeguida)

    if tweets != None:
        for tweet in tweets:
            if not ContTweets.comprobarTweetRepetido(tweet.text):
                ContTweets.guardarTweetNoEntrenado(tweet.text)
                ContTweets.guardarTweetEntrenado(tweet.text)


    Texto.cargarProcesarTexto(ContTweets.getTweetsNoEntrenadosText())

    if os.path.exists(archivos.MODELOENTRENADO_01):
        print("Modelo ya entrenado recogido...")
        Modelo.getModeloEntrenado()
    else:
        print("Modelo nuevo creado...")
        #Modelo.crearModelo(Texto.seqLength, Texto.getCantidadCaracteresUnicos())

    Modelo.entrenarModelo(Texto.xEntradas, Texto.ySalidas)
    
    seed = "que tal tu dia:  "
    generated_text = Texto.generate_text(Modelo.model, seed, length=800, temperature=0.5)

    print("\n=== Texto Generado ===\n")
    print(generated_text)
    
    time.sleep(8*60*60)    


"""
    seed = "escribe un texto sobre tus opiniones"
    generated_text = Texto.generate_text(Modelo.model, seed, length=100, temperature=0.4)

    print("\n=== Texto Generado ===\n")
    print(generated_text)
"""