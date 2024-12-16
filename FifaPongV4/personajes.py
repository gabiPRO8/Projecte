from Jugador import Jugador
import pygame

# Configuración de colores y pantalla
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)
RETRO_GRAY = (169, 169, 169)

# Fuente para textos
pygame.font.init()
LETTERING = pygame.font.Font("fuentes/Retro Gaming.ttf", 30)

# Configuración de música y fondo
pygame.mixer.init()
pygame.mixer.music.load("sounds/pes6.wav")
pygame.mixer.music.play(-1)  # Reproducción en bucle
fondo = pygame.image.load("imagenes/SeleccionDePersonajes.jpg")
fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))

# Lista de personajes
personajes = [
    Jugador("Ronaldinho", speed=10, height=85, power=4.5, colour=GREEN, habilidad=False, recarga=10, imagen_path="imagenes/ronaldinho.png"),
    Jugador("Zidane", speed=8, height=90, power=5, colour=BLUE, habilidad=False, recarga=12, imagen_path="imagenes/zidane.png"),
    Jugador("Johan Cruyff", speed=9, height=70, power=4, colour=ORANGE, habilidad=False, recarga=10, imagen_path="imagenes/cruyff.png", habilidad_activada_time=3),
    Jugador("Casillas", speed=4, height=120, power=1.3, colour=RED, habilidad=False, recarga=5, imagen_path="imagenes/casillas.png", habilidad_activada_time=5)
]

def mostrar_barras(personaje, x, y):
    """Muestra barras gráficas para las estadísticas de un personaje."""
    stats = {
        "Velocidad": personaje.speed / 10,  # Normalización
        "Altura": personaje.height / 120,
        "Potencia": personaje.power / 5
    }
    for i, (stat, value) in enumerate(stats.items()):
        # Crear superficie semitransparente
        rect_surface = pygame.Surface((400, 40))
        rect_surface.set_alpha(128)  # Opacidad del 50%
        rect_surface.fill(BLACK)  # Color del rectángulo

        # Posicionar y dibujar el rectángulo
        rect_x = x
        rect_y = y + i * 40
        SCREEN.blit(rect_surface, (rect_x, rect_y))

        # Renderizar y dibujar el texto
        texto = LETTERING.render(f"{stat}:", True, WHITE)
        SCREEN.blit(texto, (x, y + i * 40))

        # Dibujar las barras
        pygame.draw.rect(SCREEN, WHITE, (x + 200, y + i * 40 + 17, 150, 10), 1)  # Marco de la barra más corto y delgado
        pygame.draw.rect(SCREEN, GREEN, (x + 200, y + i * 40 + 17, int(150 * value), 10))  # Barra más corta y delgada

def mostrar_mensaje_inicio():
    """Muestra un mensaje para comenzar el juego."""
    while True:
        SCREEN.fill(BLACK)
        mensaje = LETTERING.render("¡Dale al Space para jugar!", True, WHITE)
        SCREEN.blit(mensaje, (WIDTH // 2 - mensaje.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                return

def seleccion_personajes(personajes):
    """Permite a los jugadores seleccionar sus personajes simultáneamente."""
    jugador1 = None
    jugador2 = None
    indice_seleccion1 = 0
    indice_seleccion2 = 0
    jugador1_seleccionado = False
    jugador2_seleccionado = False

    while True:
        SCREEN.blit(fondo, (0, 0))

        # Mostrar título

        mensaje = "Selecciona tu personaje"
        mensaje_render = LETTERING.render(mensaje, True, WHITE)
        mensaje_rect = mensaje_render.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 250))

        # Crear rectángulo translúcido para el mensaje
        rect_surf_mensaje = pygame.Surface((mensaje_rect.width + 20, mensaje_rect.height + 10), pygame.SRCALPHA)
        rect_surf_mensaje.fill((0, 0, 0, 128))
        SCREEN.blit(rect_surf_mensaje, (mensaje_rect.x - 10, mensaje_rect.y - 5))
        SCREEN.blit(mensaje_render, mensaje_rect)

        #SCREEN.blit(titulo, (WIDTH // 2 - titulo.get_width() // 2, 50))
        

        # Mostrar personaje actual para jugador 1
        personaje1 = personajes[indice_seleccion1]
        imagen_personaje1 = pygame.transform.scale(personaje1.imagen, (150, 150))
        SCREEN.blit(imagen_personaje1, (WIDTH // 4 - 75, HEIGHT // 2 - 200))
        nombre1 = LETTERING.render(personaje1.nombre, True, WHITE)
        SCREEN.blit(nombre1, (WIDTH // 4 - nombre1.get_width() // 2, HEIGHT // 2 - 50))

        # Mostrar estadísticas gráficas para jugador 1
        mostrar_barras(personaje1, WIDTH // 4 - 200, HEIGHT // 2 + 50)

        # Mostrar personaje actual para jugador 2
        personaje2 = personajes[indice_seleccion2]
        imagen_personaje2 = pygame.transform.scale(personaje2.imagen, (150, 150))
        SCREEN.blit(imagen_personaje2, (3 * WIDTH // 4 - 75, HEIGHT // 2 - 200))
        nombre2 = LETTERING.render(personaje2.nombre, True, WHITE)
        SCREEN.blit(nombre2, (3 * WIDTH // 4 - nombre2.get_width() // 2, HEIGHT // 2 - 50))

        # Mostrar estadísticas gráficas para jugador 2
        mostrar_barras(personaje2, 3 * WIDTH // 4 - 200, HEIGHT // 2 + 50)
    
        pygame.display.flip()

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                # Controles para jugador 1
                if not jugador1_seleccionado:
                    if evento.key == pygame.K_d:
                        indice_seleccion1 = (indice_seleccion1 + 1) % len(personajes)
                    elif evento.key == pygame.K_a:
                        indice_seleccion1 = (indice_seleccion1 - 1) % len(personajes)
                    elif evento.key == pygame.K_w:
                        jugador1 = personajes[indice_seleccion1]
                        jugador1_seleccionado = True
                # Controles para jugador 2
                if not jugador2_seleccionado:
                    if evento.key == pygame.K_RIGHT:
                        indice_seleccion2 = (indice_seleccion2 + 1) % len(personajes)
                    elif evento.key == pygame.K_LEFT:
                        indice_seleccion2 = (indice_seleccion2 - 1) % len(personajes)
                    elif evento.key == pygame.K_UP:
                        jugador2 = personajes[indice_seleccion2]
                        jugador2_seleccionado = True


        if jugador1 and jugador2:
            mostrar_mensaje_inicio()
            return jugador1, jugador2
