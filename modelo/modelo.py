from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense

model = None

def entrenarModelo(x, y):
    global model
    
    EPOCHS = 5
    BATCH_SIZE = 128

    model.fit(x, y, batch_size=BATCH_SIZE, epochs=EPOCHS)

def crearModelo(seqLength, numChars):
    global model

    model = Sequential()
    model.add(LSTM(256, input_shape=(seqLength, numChars), return_sequences=True))
    model.add(LSTM(256))    
    model.add(Dense(numChars, activation="softmax"))

    model.compile(optimizer="adam", loss="categorical_crossentropy")
    model.summary()

def getModelo():
    global model
    model = load_model("modelo_entrenado.h5")

