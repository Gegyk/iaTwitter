import numpy as np

chars = [
    # Puntuación y caracteres comunes
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', 
    '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', 
    '¡', '¿', '¥', '©', '®', '™', '§', '°', '±', '∑', 'π', '∞', '≠', '≤', '≥', 
    '±', '←', '↑', '→', '↓', '∩', '∪', '⊆', '⊂', '⊇', '⊃', '⊥', '⊗', '⊙', '⋯', 
    '⊕', 'ℂ', 'ℕ', 'ℝ', 'ℤ', 'ℕ', '∀', '∃', '∑', '∈', '∉', '∪', '∩', '≈', '≡',
    '≪', '≫', '⊗', '⊕', '⊥', '∠', '∠', '≤', '≥', '⊂', '⊃', '⊇', '⊆', '∫', '∮',

    # Caracteres de letras latinas (mayúsculas y minúsculas)
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','ñ', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','Ñ',
    
    # Caracteres con tildes
    'á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú', 'à', 'è', 'ì', 'ò', 'ù', 'À', 'È', 'Ì', 'Ò', 'Ù',

    # Emoticonos comunes
    '😀', '😁', '😂', '🤣', '😃', '😄', '😅', '😆', '😉', '😊', '😋', '😎', '😍', '😘',
    '😜', '😝', '😛', '😳', '👀', '💯', '🔥', '✨', '🌟', '💥', '💫', '🎉', '🎊', '🎈',
    '🎁', '🎂', '🍀', '🌱', '🌿', '🍃', '🌳', '🌴', '🌵', '🌷', '🌸', '🌺', '🌻', '🌼',
    '🌾', '🍇', '🍉', '🍊', '🍋', '🍌', '🍍', '🍎', '🍏', '🍐', '🍑', '🍒', '🍓', '🍔',
]


char_to_idx = {char: idx for idx, char in enumerate(chars)}
idx_to_char = {idx: char for idx, char in enumerate(chars)}
xEntradas = None
ySalidas = None

# Configuración
seqLength = 100  # Longitud de las secuencias
step = 1  # Paso entre secuencias

def getCantidadCaracteresUnicos():
    return len(chars)


def cargarProcesarTexto(texto):
    global chars, char_to_idx, idx_to_char, xEntradas, ySalidas

    # Dividir texto en secuencias
    sequences = []
    next_chars = []

    for i in range(0, len(texto) - seqLength, step):
        sequences.append(texto[i:i + seqLength])
        next_chars.append(texto[i + seqLength])

    # Convertir secuencias a tensores de entrada (xEntradas) y salida (ySalidas)
    xEntradas = np.zeros((len(sequences), seqLength, len(chars)), dtype=np.float32)
    ySalidas = np.zeros((len(sequences), len(chars)), dtype=np.float32)

    for i, seq in enumerate(sequences):
        for t, char in enumerate(seq):
            if char in char_to_idx:
                xEntradas[i, t, char_to_idx[char]] = 1
        ySalidas[i, char_to_idx[next_chars[i]]] = 1


def generate_text(model, seed_text, length, temperature=1.0):
    global chars, char_to_idx, idx_to_char
    
    # Asegurarse de que la longitud del seed sea >= seqLength
    seed_text = seed_text[-seqLength:]

    generated = seed_text
    for _ in range(length):
        # Crear un tensor de entrada basado en el texto actual
        x_pred = np.zeros((1, seqLength, len(chars)))

        # Rellenar el tensor x_pred con la codificación one-hot de los caracteres en el seed_text
        for t, char in enumerate(seed_text[-seqLength:]):
            if char in char_to_idx:
                x_pred[0, t, char_to_idx[char]] = 1
            else:
                # Si el carácter no está en el diccionario, podemos asignarlo a un valor predeterminado
                # Si no quieres usar 0 para caracteres no encontrados, puedes añadir un valor especial
                # para "caracteres desconocidos" o manejarlo de otra forma.
                x_pred[0, t, 0] = 1  # Este valor es arbitrario y debe coincidir con tu lógica de codificación.

        # Asegúrate de que `x_pred` tenga la forma adecuada antes de pasarlo al modelo
        assert x_pred.shape == (1, seqLength, len(chars)), f"Expected shape (1, {seqLength}, {len(chars)}), but got {x_pred.shape}"

        # Predecir el próximo carácter
        predictions = model.predict(x_pred, verbose=0)[0]
        predictions = np.log(predictions) / temperature
        exp_preds = np.exp(predictions)
        predictions = exp_preds / np.sum(exp_preds)

        # Elegir el siguiente carácter según la predicción
        next_index = np.random.choice(len(chars), p=predictions)
        next_char = idx_to_char[next_index]

        # Agregar el carácter generado al texto
        generated += next_char
        seed_text += next_char

    return generated
