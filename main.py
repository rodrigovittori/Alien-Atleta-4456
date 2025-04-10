#pgzero
""" NOTA 1: El código de este proyecto está publicado en el repo:
            > https://github.com/rodrigovittori/Alien-Atleta-4456/
    
    NOTA 2: Los assets de este proyecto fueron tomados del sitio web de Kenney,
            pueden obtener más modelos en: https://kenney.nl/assets/platformer-pack-redux
            y revisar la colección completa en: https://kenney.nl/assets/series:Platformer%20Pack  
    
    ---------------------------------------------------------------------------------------------------

    [M6.L3] - Actividad #9 y #10: Homework/Tareas
    Objetivo: Agregar el primer obstáculo

    NOTA: Nosotros ya lo resolvimos, nos vemos la clase que viene :D
    
    TAREA: En base a lo que apredieron con el engranaje y los cristales,
           modifiquen el código para que la caja y nuestro personaje NO puedan salir
           de la pantalla de juego. """


WIDTH = 600   # Ancho de la ventana (en px)
HEIGHT = 300   # Alto de la ventana (en px)

TITLE = "Juego del Alien Atleta y sus piruetas" # Título para la ventana del juego
FPS = 30      # Número de fotogramas por segundo

""" > Vamos a crear nuestro personaje :D """
fondo =     Actor("background")          # Nuestro fondo NO tiene posición porque queremos que ocupe TODA la pantalla
personaje = Actor("alien", (50, 240))    # Nuestro personaje SI la tiene, las coordenadas se registran en pos(x, y)
caja =      Actor("box", ((WIDTH - 50), 265) )

# draw() como su nombre lo indica es el método de pgzero que dibuja objetos en pantalla
def draw(): 
    fondo.draw()
    personaje.draw()
    caja.draw()

def update(dt): # update(dt) es el bucle ppal de nuestro juego, dt significa delta time (tiempo en segundos entre cada frame)
    # > https://pygame-zero.readthedocs.io/en/stable/hooks.html#update
    # Podemos traducir "update" como "actualizar", es decir, en este método contendremos el código que produzca cambios en nuestro juego
    
    # Mover personaje:
    personaje.x += 5       # mover el personaje 5 px a la derecha en cada frame
    personaje.angle -= 5   # para las piruetas :V
    
    # Mover la caja:
    caja.x -= 5            # mover la caja 5 px a la izquierda en cada frame
    caja.angle += 5        # roto la caja 5 grados cada frame