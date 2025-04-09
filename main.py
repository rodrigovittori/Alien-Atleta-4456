#pgzero
""" [M6.L3] - Actividad 3: "La función draw()"
    Objetivo: Que la clase muestre un mensaje personalizado con el método draw() """

WIDTH = 900    # Ancho de la pantalla (en px)
HEIGHT = 360   # Alto de la pantalla (en px)

TITLE = "MENSAJE PERSONALIZADO" # sin archivos
FPS = 30       # Tope/Límite de FPS (cuadros por segundo) a dibujar

string_mensaje = "¡Hola mamá!, estoy programando :D"

def draw():
    screen.fill((84, 192, 176))
    screen.draw.text(string_mensaje, center=(WIDTH/2, HEIGHT/2), color="white", background="black", fontsize = 48)