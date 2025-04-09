#pgzero
# [M6.L3] - Actividad Extra: Mini-clicker

WIDTH = 300  # Ancho de la ventana (en px)
HEIGHT = 300 # Alto de la ventana  (en px)

TITLE = "Clicker" # Título de la ventana de juego
FPS = 30 # Fotogramas por segundo
contador = 0

def draw():
    screen.fill((32, 191, 107))
    screen.draw.text(str(contador), center=(150, 150), color="white", fontsize = 96)
    
def on_mouse_down(button, pos):
    global contador
    if button == mouse.LEFT:
        contador = contador + 1
        
    elif button == mouse.RIGHT:
        contador = contador - 1