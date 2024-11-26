import numpy as np

chars = []
char_to_idx = {}
idx_to_char = {}
xEntradas = None
ySalidas = None

# Configuración
seqLength = 100  # Longitud de las secuencias
step = 1  # Paso entre secuencias

def getCantidadCaracteresUnicos():
    return len(chars)


def cargarProcesarTexto():
    global chars, char_to_idx, idx_to_char, xEntradas, ySalidas

    try:
        with open("iaTwitter/datos/dataset.txt", "r", encoding="utf-8") as f:
            text = f.read().lower()
    except FileNotFoundError:
        print("Error: El archivo 'dataset.txt' no se encuentra en el directorio actual.")
        exit()

    # Crear un diccionario de caracteres únicos
    chars = sorted(list(set(text)))
    char_to_idx = {char: idx for idx, char in enumerate(chars)}
    idx_to_char = {idx: char for idx, char in enumerate(chars)}

    # Dividir texto en secuencias
    sequences = []
    next_chars = []

    for i in range(0, len(text) - seqLength, step):
        sequences.append(text[i:i + seqLength])
        next_chars.append(text[i + seqLength])

    # Convertir secuencias a tensores de entrada (xEntradas) y salida (ySalidas)
    xEntradas = np.zeros((len(sequences), seqLength, len(chars)), dtype=np.bool_)
    ySalidas = np.zeros((len(sequences), len(chars)), dtype=np.bool_)

    for i, seq in enumerate(sequences):
        for t, char in enumerate(seq):
            xEntradas[i, t, char_to_idx[char]] = 1
        ySalidas[i, char_to_idx[next_chars[i]]] = 1

def generate_text(model, seed_text, length, temperature=1.0):
    global chars, char_to_idx, idx_to_char

    """
    Genera texto a partir de un modelo entrenado.
    
    Parameters:
    - model: el modelo entrenado.
    - seed_text: texto inicial para comenzar la generación.
    - length: cantidad de caracteres a generar.
    - temperature: controla la aleatoriedad en la predicción.
    """
    generated = seed_text
    for _ in range(length):
        # Crear un tensor de entrada basado en el texto actual
        x_pred = np.zeros((1, seqLength, len(chars)))
        for t, char in enumerate(seed_text[-seqLength:]):
            if char in char_to_idx:
                x_pred[0, t, char_to_idx[char]] = 1

        # Predecir el próximo carácter
        predictions = model.predict(x_pred, verbose=0)[0]
        predictions = np.log(predictions) / temperature
        exp_preds = np.exp(predictions)
        predictions = exp_preds / np.sum(exp_preds)

        next_index = np.random.choice(len(chars), p=predictions)
        next_char = idx_to_char[next_index]

        # Agregar el carácter generado al texto
        generated += next_char
        seed_text += next_char

    return generated