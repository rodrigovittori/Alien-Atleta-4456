#pgzero
""" [M6.L3] - Actividad 2: "Ventana del Juego"
    Objetivo: presentar el sistema de pgzero a los alumnos """

WIDTH = 600   # Ancho de la ventana (en px)
HEIGHT = 300  # Alto de la ventana  (en px)

TITLE = "TÍTULO ÉPICO" # Título de nuestra ventana
FPS = 30  # Ponemos un "cap" o límite máximo de FPS

def draw():
    # NOTA: Ya NO tenemos picture.jpg, así que deberemos rellenar nuestra ventana,
    #       lo haremos a partir de nuestro screen: https://pygame-zero.readthedocs.io/en/stable/builtins.html#screen

    # Fill como la tortuga puede recibir una tupla (r, g, b), un código predefinido o el color en Hexadecimal
    # screen.fill("blue")           # Ejemplo con color predefinido
    screen.fill((255, 0, 255)) # Ejemplo RGB
    # screen.fill("#409428")        # Ejemplo con color predefinido
    
    screen.draw.text(TITLE, center=(WIDTH/2, HEIGHT/2), color="white", background="black", fontsize = 48)
    # MUCHO TEXTO :V -> https://pygame-zero.readthedocs.io/en/stable/builtins.html?highlight=text#Screen.draw.text
    #                -> https://pygame-zero.readthedocs.io/en/stable/ptext.html?highlight=text