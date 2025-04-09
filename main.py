#pgzero
""" [M6.L3] - Actividad 1: "Introducción"
    Nota: NO enseñar archivos personalizados hasta el final de la clase """

""" En pgzero tendremos que crear nuestra ventana de juego, la que tiene su ancho (WIDTH) y su alto (HEIGHT) """

WIDTH = 770   # Ancho de la ventana (en px)
HEIGHT = 450  # Alto de la ventana  (en px)

""" Agreguemos un título a nuestra ventana de juego """
TITLE = "Introducción: Imágen"
FPS = 30  # Ponemos un "cap" o límite máximo de FPS

""" En pgzero trabajaremos con Actores (objetos que tienen una serie de atributos especiales)
    > https://pygame-zero.readthedocs.io/en/stable/builtins.html#actors 
    
    Para trabajar con ellos, deberemos definirlos dándoles un nombre y una imágen o sprite  """

fondo = Actor("picture") # Creamos un Actor con la imagen "picture.jpg"

""" Funciones de pgzero: La librería pgzero trae MUCHAS funcionalidades preparas, una de ellas es el hook draw
    que dibuja elementos en pantalla: https://pygame-zero.readthedocs.io/en/stable/hooks.html#draw   """

def draw():
    fondo.draw()