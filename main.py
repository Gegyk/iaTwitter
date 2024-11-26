from texto import texto as Texto
from modelo import modelo as Modelo


Texto.cargarProcesarTexto()

Modelo.crearModelo(Texto.seqLength, Texto.getCantidadCaracteresUnicos())

Modelo.entrenarModelo(Texto.xEntradas, Texto.ySalidas)


seed = "escribe un texto sobre tus opiniones"
generated_text = Texto.generate_text(Modelo.model, seed, length=100, temperature=0.4)

print("\n=== Texto Generado ===\n")
print(generated_text)
