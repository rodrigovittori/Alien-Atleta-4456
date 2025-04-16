#pgzero
""" NOTA 1: El código de este proyecto está publicado en el repo:
            > https://github.com/rodrigovittori/Alien-Atleta-4456/
    
    NOTA 2: Los assets de este proyecto fueron tomados del sitio web de Kenney,
            pueden obtener más modelos en: https://kenney.nl/assets/platformer-pack-redux
            y revisar la colección completa en: https://kenney.nl/assets/series:Platformer%20Pack  
    
    ---------------------------------------------------------------------------------------------------

    [M6.L4] - Actividad Nº 3: "Controles"
    Objetivo: Agregar controles para el movimiento del personaje
    Nota: EN ESTA ACTIVIDAD agregaremos los límites para evitar que se salga de la pantalla de juego

    Paso Nº 1) Crearemos un atributo "velocidad" en nuestro personaje
    Paso Nº 2) Modificamos el código en update() agregando condiciones de teclado y límites al PJ   
    
    NOTA: Modificaremos nuestro draw() para que se muestre en pantalla la posición en X de nuestro PJ
    NOTA 2: Agregamos un Rect() de pygame para mostrar la "hitbox" del PJ   """

WIDTH = 600   # Ancho de la ventana (en px)
HEIGHT = 300   # Alto de la ventana (en px)

TITLE = "Juego del Alien Atleta y sus piruetas" # Título para la ventana del juego
FPS = 30      # Número de fotogramas por segundo

""" > Vamos a crear nuestro personaje :D """
fondo =     Actor("background")          # Nuestro fondo NO tiene posición porque queremos que ocupe TODA la pantalla
personaje = Actor("alien", (50, 240))    # Nuestro personaje SI la tiene, las coordenadas se registran en pos(x, y)
personaje.velocidad = 5               # velocidad (en px) a la que avanza el personaje por cada frame

""" Nota: Si quisieramos facilitar la tarea de "reiniciar"/"resetear"
          la posición del personaje o los obstáculos/enemigos a su estado
          inicial, podemos hacerlo de la siguiente manera:

    Paso 1) Creamos un atributo del actor donde registramos su posición inicial:

            personaje.posInicial = personaje.pos # almacenamos la posición inicial

    Paso 2) Cuando querramos resetear la posición, usaremos:

            personaje.pos = personaje.posInicial """

caja =      Actor("box", ((WIDTH - 50), 265) )

# draw() como su nombre lo indica es el método de pgzero que dibuja objetos en pantalla
def draw(): 
    fondo.draw()
    personaje.draw()
    caja.draw()

    screen.draw.text(("X= " + str(personaje.x)), (30,30), background="white", color="black", fontsize=24)
    screen.draw.rect(personaje.collidebox, (255, 0, 255))

def update(dt): # update(dt) es el bucle ppal de nuestro juego, dt significa delta time (tiempo en segundos entre cada frame)
    # > https://pygame-zero.readthedocs.io/en/stable/hooks.html#update
    # Podemos traducir "update" como "actualizar", es decir, en este método contendremos el código que produzca cambios en nuestro juego
    
    # Actualizamos el personaje:

    personaje.collidebox = Rect((personaje.x - int(personaje.width / 2), personaje.y - int(personaje.height / 2)), (personaje.width, personaje.height))
    
    if ( (keyboard.right or keyboard.d) and ( personaje.x < ( WIDTH - int(personaje.width / 2) ) ) ):
        personaje.x += personaje.velocidad

    if ( (keyboard.left or keyboard.a) and ( personaje.x > int(personaje.width / 2) ) ):
        personaje.x -= personaje.velocidad
    
    ###################################################################################
    
    # Mover la caja:
    if (caja.x < 0):     # Si la caja salió de la ventana de juego...
        caja.x += WIDTH  # La llevamos a la otra punta de la pantalla
    else:
        # Si todavía no se escapa de la ventana...
        caja.x -= 5      # mover la caja 5 px a la izquierda en cada frame

    caja.angle = (caja.angle % 360) + 5  # rotamos la caja 5 grados cada frame