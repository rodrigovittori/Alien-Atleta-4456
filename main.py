#pgzero
""" NOTA 1: El código de este proyecto está publicado en el repo:
            > https://github.com/rodrigovittori/Alien-Atleta-4456/
    
    NOTA 2: Los assets de este proyecto fueron tomados del sitio web de Kenney,
            pueden obtener más modelos en: https://kenney.nl/assets/platformer-pack-redux
            y revisar la colección completa en: https://kenney.nl/assets/series:Platformer%20Pack  
    
    ---------------------------------------------------------------------------------------------------

    [M7.L2] - Actividad #2: "Funciones de movimiento"
    # Objetivo: Migrar la lógica de movimiento de los enemigos a una función avocada a ello

    Paso Nº 1) Creamos una función actualizar_enemigos()
    Paso Nº 2) Creamos también las funciones: mover_personaje(), detectar_colisiones(), reiniciar_juego()

    Nota 3: Seguimos sin imágen/sprite "hurt"

    Nota 4: CUIDADO: Si intentamos dibujar texto_colision con un valor vacío, nos devuelve el siguiente error:
           > ExternalError:
                InvalidStateError:
                    Failed to execute 'drawImage' on 'CanvasRenderingContext2D':
                        The image argument is a canvas element with a width or height of 0.
---------------------------------------------------------------------------------------------------

NOTA: Les quedan las actividades adicionales y tenemos un bug ya que nuestro PJ puede saltar mientras
      sigue en el aire. Nos vemos la próxima semana :D    """

############################################# [VENTANA PGZERO] #############################################
WIDTH = 600   # Ancho de la ventana (en px)
HEIGHT = 300   # Alto de la ventana (en px)

TITLE = "Juego del Alien Atleta y sus piruetas" # Título para la ventana del juego
FPS = 30      # Número de fotogramas por segundo

################################################# [ACTORES] #################################################

fondo =            Actor("background")   # Nuestro fondo NO tiene posición porque queremos que ocupe TODA la pantalla
cartel_game_over = Actor("GO")           # Splash Screen de Game Over

""" > Vamos a crear nuestro personaje :D """
personaje = Actor("alien", (50, 240))    # Nuestro personaje SI la tiene, las coordenadas se registran en pos(x, y)
personaje.velocidad = 5                  # velocidad (en px) a la que avanza el personaje por cada frame

personaje.COOLDOWN_SALTO = 1             # tiempo de recarga habilidad salto (en segundos)
personaje.timer_salto = 0                # tiempo que debe pasar (en segundos) antes de que nuestro personaje pueda saltar nuevamente
personaje.altura_salto = int(personaje.height * 1.6) # El personaje saltará 1.6 veces su altura

""" Nota: Para evitar que al agacharse se anule la animación de salto DEBERÍAMOS implementar un check para prevenirlo """
personaje.timer_agachado = 0.0           # Tiempo restante (en segundos) antes de poner de pie al personaje
personaje.esta_agachado = False          # Valor que controla si debemos permanecer agachados o no

personaje.posInicial = personaje.pos     # almacenamos la posición inicial del PJ

######################################### [ ENEMIGOS / OBSTÁCULOS ] #########################################

caja =      Actor("box", ( (WIDTH - 50), 265) )
abeja =     Actor("bee", ( (WIDTH + 200), 150) )

############################################### [ VARIABLES ] ###############################################

game_over = False    # Vble que registra si nuestra partida ha finalizado o no
puntuacion = 0       # Cantidad de enemigos esquivados
texto_colision = ""  # texto que se muestra por pantalla para informar s/colision letal
nva_imagen = "alien" # Sprite que tendrá nuestro PJ el PRÓXIMO frame (se actualiza durante update())

#############################################################################################################

"""  #####################
    # FUNCIONES PROPIAS #
   #####################  """

def actualizar_enemigos():
    global puntuacion
        
    # ENEMIGO Nº 1: CAJA
    
    caja.collidebox = Rect((caja.x - int(caja.width / 2), caja.y - int(caja.height / 2)), (caja.width, caja.height))
        
    if (caja.x < 0):     # Si la caja salió de la ventana de juego...
        caja.x += WIDTH  # La llevamos a la otra punta de la pantalla
        puntuacion += 1  # Aumento en 1 el contador de enemigos esquivados
    else:
        # Si todavía no se escapa de la ventana...
        caja.x -= 5      # mover la caja 5 px a la izquierda en cada frame
        caja.angle = (caja.angle % 360) + 5  # rotamos la caja 5 grados cada frame
    
    """ ########################################################################### """
        
    # ENEMIGO Nº 2: ABEJA
    
    abeja.collidebox = Rect((abeja.x - int(abeja.width / 2), abeja.y - int(abeja.height / 2)), (abeja.width, abeja.height))
    
    # NOTA: La abeja DEBERÍA tener un movimiento más complejo (creo que es una tarea adicional) con un patrón zigzagueante
        
    if (abeja.x < 0):       # Si la abeja salió de la ventana de juego...
        abeja.x += WIDTH    # La llevamos a la otra punta de la pantalla
        puntuacion += 1     # Aumento en 1 el contador de enemigos esquivados
    else:
        # Si todavía no se escapa de la ventana...
        abeja.x -= 5     # mover la abeja 5 px a la izquierda en cada frame

###########################################################################

def detectar_colisiones():
    # > https://www.pygame.org/docs/ref/rect.html#pygame.Rect.colliderect
    global nva_imagen, game_over, texto_colision
    
    if ( personaje.colliderect(caja) ):
        if (nva_imagen != "hurt"):
            # nva_imagen = "hurt"
            # NOTA: Si queremos implementar un sistema de "daño" en lugar de una muerte instantánea, éste es el lugar :D
            game_over = True # En caso de colisión, terminamos el juego
            texto_colision = "¡Entrega letal!"
                
    elif ( personaje.colliderect(abeja) ):
        if (nva_imagen != "hurt"):
            # nva_imagen = "hurt"
            # NOTA: Si queremos implementar un sistema de "daño" en lugar de una muerte instantánea, éste es el lugar :D
            game_over = True # En caso de colisión, terminamos el juego
            texto_colision = "¡Eres alérgico a las abejas!"

###########################################################################

def reiniciar_juego():
    global game_over, puntuacion, texto_colision, nva_imagen
    
    game_over = False
    puntuacion = 0
    texto_colision = ""
    # Reseteamos personaje
    personaje.pos = personaje.posInicial
    personaje.timer_salto = 0
    personaje.timer_agachado = 0.0
    personaje.esta_agachado = False
    personaje.velocidad = 5
    nva_imagen = "alien"
    # Nota: Si hacemos que la velocidad de los enemigos escale con el tiempo, la reseteamos
    # Reseteamos caja
    caja.pos = (WIDTH - 50, 265)
    caja.angle = 0
    # Reseteamos abeja
    abeja.pos = (WIDTH + 200, 150)

###########################################################################

def mover_personaje():
    global nva_imagen
    
    # Movimiento lateral
    if ( (keyboard.right or keyboard.d) and ( personaje.x < ( WIDTH - int(personaje.width / 2) ) ) and (not personaje.esta_agachado) ):
        personaje.x += personaje.velocidad
        nva_imagen = "right"
    
    if ( (keyboard.left or keyboard.a) and ( personaje.x > int(personaje.width / 2) ) and (not personaje.esta_agachado) ):
        personaje.x -= personaje.velocidad
        nva_imagen = "left"
    
    # Salto: lo implementamos en OnKeyDown(key)
    
    # Agacharse
    if (keyboard.down or keyboard.s):
        personaje.y = 260    # Bajamos el pj
        nva_imagen = "duck"
        personaje.timer_agachado = 0.1 # tiempo que nuestro PJ seguirá agachado DESPUÉS de soltar la tecla
        personaje.esta_agachado = True

# draw() como su nombre lo indica es el método de pgzero que dibuja objetos en pantalla
def draw():

    if (game_over):
        # Si bien en este caso el cartel de Game Over cubre TODA la pantalla, 
        # sería mejor solamente agregar el texto "GAME OVER" y dibujar el fondo
        fondo.draw() 
        cartel_game_over.draw()
        # Nota: modificamos la altura del otro mensaje para mostrar más info:
        screen.draw.text(("Enemigos esquivados: " + str(puntuacion)), center= (int(WIDTH/2), 2* int(HEIGHT/3)), color = "yellow", fontsize = 24)
        screen.draw.text("Presiona [Enter] para reiniciar", center= (int(WIDTH/2), 4* int(HEIGHT/5)), color = "white", fontsize = 32)
        screen.draw.text(texto_colision, center= (int(WIDTH/2), int(HEIGHT/5)), color = "red", background = "black", fontsize = 24)

    else:
        fondo.draw()
        personaje.draw()
        caja.draw()
        abeja.draw()

        # Indicador de salto:
        if (personaje.timer_salto <= 0):
            screen.draw.text("¡LISTO!", midleft=(20,20), color = (0, 255, 0), fontsize=24)
        else:
            screen.draw.text(str(personaje.timer_salto), midleft=(20,20), color = "red", fontsize=24)    
        
        screen.draw.rect(personaje.collidebox, (255, 0, 255)) # Dibujamos collidebox del PJ
        # INDICADOR DE POS DEL PJ EN EJE X: # screen.draw.text(("X= " + str(personaje.x)), (30,30), background="white", color="black", fontsize=24)
        screen.draw.rect(caja.collidebox, (255, 0, 0)) # Dibujamos collidebox de la caja
        screen.draw.rect(abeja.collidebox, (255, 0, 0)) # Dibujamos collidebox de la abeja

        # Indicador puntuación
        screen.draw.text(("Enemigos esquivados: " + str(puntuacion)), midright=(WIDTH-20, 20), color ="black", background="white", fontsize=24)

def update(dt): # update(dt) es el bucle ppal de nuestro juego, dt significa delta time (tiempo en segundos entre cada frame)
    # > https://pygame-zero.readthedocs.io/en/stable/hooks.html#update
    # Podemos traducir "update" como "actualizar", es decir, en este método contendremos el código que produzca cambios en nuestro juego

    global nva_imagen

    if (game_over):
        # En caso de game_over:
        if (keyboard.enter):
            reiniciar_juego()
            
    else:
        """   >>> CAMBIOS AUTOMÁTICOS <<<   """
        personaje.collidebox = Rect((personaje.x - int(personaje.width / 2), personaje.y - int(personaje.height / 2)), (personaje.width, personaje.height))
        personaje.timer_salto -= dt    # restamos al timer del cooldown de salto del persoanje el tiempo desde el último frame
        personaje.timer_agachado -= dt # restamos al timer para resetar la altura del persoanje el tiempo desde el último frame
    
        if ((personaje.timer_agachado <= 0) and (personaje.esta_agachado)):
            personaje.y = personaje.posInicial[1]   # Reseteamos la altura del PJ 
            personaje.esta_agachado = False         # Indicamos que el PJ ya NO está agachado
    
        nva_imagen = "alien"           # variable local que almacena el próximo sprite a renderizar
                                       # "alien": quieto / "left": mov. izq. / "right" : mov. dcha.
        mover_personaje()
        actualizar_enemigos()
        detectar_colisiones()
        """ >>> POST INPUT <<< """
        personaje.image = nva_imagen # Actualizamos el sprite del personaje
    
def on_key_down(key): # Este método se activa al presionar una tecla
    # https://pygame-zero.readthedocs.io/en/stable/hooks.html?highlight=on_key_down#on_key_down

    if (not game_over):
        
        if (
             (keyboard.space or keyboard.w or keyboard.up) and   # Parte 1 de la cond: presionar tecla
             (personaje.timer_salto <= 0)                  and   # Parte 2 de la cond: timer listo
             (personaje.y > personaje.height)              and   # Parte 3 de la cond: el PJ NO ha salido de la pantalla
             (not personaje.esta_agachado)                       # Parte 4 de la cond: el PJ NO está agachado
           ):
            
            personaje.timer_salto = personaje.COOLDOWN_SALTO                 # Reseteamos cooldown
            #personaje.y -= personaje.altura_salto                           # El PJ "salta" (cambiamos su altura)
            #animate(personaje, tween="bounce_end", duration = 2, y = 240)   # Activamos la animación de caída
    
            temp_anim = animate(personaje, tween="decelerate", duration = (personaje.COOLDOWN_SALTO / 2), y = (personaje.y - personaje.altura_salto))
            temp_anim.on_finished = bajarAlien

def bajarAlien():
    animate(personaje, tween="accelerate", duration = (personaje.COOLDOWN_SALTO / 2), y = personaje.posInicial[1])   # BAJAR ALIEN