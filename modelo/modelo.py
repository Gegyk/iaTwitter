from Constantes import archivos
from ControllerDatos import ControllerTweets as ContTweet
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense

model = None

def entrenarModelo(x, y):
    global model
    
    EPOCHS = 20
    BATCH_SIZE = 128

    model.fit(x, y, batch_size=BATCH_SIZE, epochs=EPOCHS)
    
    model.save(archivos.MODELOENTRENADO_01)
    
    ContTweet.borrarDatosTweetNoEntrenado()

def crearModelo(seqLength, numChars):
    global model

    model = Sequential()
    model.add(LSTM(256, input_shape=(seqLength, numChars), return_sequences=True))
    model.add(LSTM(256))    
    model.add(Dense(numChars, activation="softmax"))

    model.compile(optimizer="adam", loss="categorical_crossentropy")
    model.summary()

def getModeloEntrenado():
    global model
    model = load_model(archivos.MODELOENTRENADO_01)

