#pgzero
""" NOTA 1: El código de este proyecto está publicado en el repo:
            > https://github.com/rodrigovittori/Alien-Atleta-4456/
    
    NOTA 2: Los assets de este proyecto fueron tomados del sitio web de Kenney,
            pueden obtener más modelos en: https://kenney.nl/assets/platformer-pack-redux
            y revisar la colección completa en: https://kenney.nl/assets/series:Platformer%20Pack  
    
    ---------------------------------------------------------------------------------------------------

    [M6.L4] - Actividad Nº 5: "Salto"
    Objetivo: Agregar la lógica necesaria para implementar un salto

    NOTA: La actividad Nº 4 NO FORMA PARTE del proyecto

    Paso Nº 1) Vamos a crear las variables necesarias para el sistema de salto: COOLDOWN_SALTO, timer_salto y altura_salto
                NOTA: Por la implementación elegida por el grupo creamos un nuevo atributo que registra la posición inicial del PJ
    Paso Nº 2) Agregamos actualizaciones de timers en update()
    Paso Nº 3) Agregamos texto en draw() para saber cuando nuestro PJ esta LISTO para saltar
    Paso Nº 4) Agregamos la lógica de control de salto (en on_key_down)
    Paso Nº 5) Creamos una función invocable (sin parámetros) que controla la segunda parte de la animación de salto   """

WIDTH = 600   # Ancho de la ventana (en px)
HEIGHT = 300   # Alto de la ventana (en px)

TITLE = "Juego del Alien Atleta y sus piruetas" # Título para la ventana del juego
FPS = 30      # Número de fotogramas por segundo

""" > Vamos a crear nuestro personaje :D """
fondo =     Actor("background")          # Nuestro fondo NO tiene posición porque queremos que ocupe TODA la pantalla

caja =      Actor("box", ((WIDTH - 50), 265) )

personaje = Actor("alien", (50, 240))    # Nuestro personaje SI la tiene, las coordenadas se registran en pos(x, y)
personaje.velocidad = 5                  # velocidad (en px) a la que avanza el personaje por cada frame

personaje.COOLDOWN_SALTO = 1             # tiempo de recarga habilidad salto (en segundos)
personaje.timer_salto = 0                # tiempo que debe pasar (en segundos) antes de que nuestro personaje pueda saltar nuevamente
personaje.altura_salto = int(personaje.height * 1.6) # El personaje saltará 1.6 veces su altura

personaje.posInicial = personaje.pos  # almacenamos la posición inicial del PJ

############################################################################################################

# draw() como su nombre lo indica es el método de pgzero que dibuja objetos en pantalla
def draw(): 
    fondo.draw()
    personaje.draw()
    caja.draw()

    # Indicador de salto:
    if (personaje.timer_salto <= 0):
        screen.draw.text("¡LISTO!", midleft=(20,20), color = (0, 255, 0), fontsize=24)
    else:
        screen.draw.text(str(personaje.timer_salto), midleft=(20,20), color = "red", fontsize=24)    
    
    screen.draw.rect(personaje.collidebox, (255, 0, 255)) # Dibujamos collidebox del PJ
    # INDICADOR DE POS DEL PJ EN EJE X: # screen.draw.text(("X= " + str(personaje.x)), (30,30), background="white", color="black", fontsize=24)

def update(dt): # update(dt) es el bucle ppal de nuestro juego, dt significa delta time (tiempo en segundos entre cada frame)
    # > https://pygame-zero.readthedocs.io/en/stable/hooks.html#update
    # Podemos traducir "update" como "actualizar", es decir, en este método contendremos el código que produzca cambios en nuestro juego
    
    """   #######################
         # CAMBIOS AUTOMATICOS #
        #######################   """

    personaje.timer_salto -= dt # restamos al timer del cooldown de salto del persoanje el tiempo desde el último frame
    personaje.collidebox = Rect((personaje.x - int(personaje.width / 2), personaje.y - int(personaje.height / 2)), (personaje.width, personaje.height))
    
    """   ################
         # LEER TECLADO #
        ################   """
    
    if ( (keyboard.right or keyboard.d) and ( personaje.x < ( WIDTH - int(personaje.width / 2) ) ) ):
        personaje.x += personaje.velocidad

    if ( (keyboard.left or keyboard.a) and ( personaje.x > int(personaje.width / 2) ) ):
        personaje.x -= personaje.velocidad

    # Salto: lo implementamos en OnKeyDown(key)
    
    ###################################################################################
    
    # Mover la caja:
    if (caja.x < 0):     # Si la caja salió de la ventana de juego...
        caja.x += WIDTH  # La llevamos a la otra punta de la pantalla
    else:
        # Si todavía no se escapa de la ventana...
        caja.x -= 5      # mover la caja 5 px a la izquierda en cada frame

    caja.angle = (caja.angle % 360) + 5  # rotamos la caja 5 grados cada frame

def on_key_down(key): # Este método se activa al presionar una tecla
    # https://pygame-zero.readthedocs.io/en/stable/hooks.html?highlight=on_key_down#on_key_down

    if (
         (keyboard.space or keyboard.w or keyboard.up) and   # Parte 1 de la cond: presionar tecla
         (personaje.timer_salto <= 0)                  and   # Parte 2 de la cond: timer listo
         (personaje.y > personaje.height)                    # Parte 3 de la cond: el PJ NO ha salido de la pantalla
       ):
        
        personaje.timer_salto = personaje.COOLDOWN_SALTO                 # Reseteamos cooldown
        #personaje.y -= personaje.altura_salto                           # El PJ "salta" (cambiamos su altura)
        #animate(personaje, tween="bounce_end", duration = 2, y = 240)   # Activamos la animación de caída

        temp_anim = animate(personaje, tween="decelerate", duration = (personaje.COOLDOWN_SALTO / 2), y = (personaje.y - personaje.altura_salto))   # PRIMERO ANIMACIÓN
        temp_anim.on_finished = bajarAlien

def bajarAlien():
    animate(personaje, tween="accelerate", duration = (personaje.COOLDOWN_SALTO / 2), y = personaje.posInicial[1])   # BAJAR ALIEN