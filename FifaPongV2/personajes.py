
from Jugador import Jugador
import pygame

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
LETTERING = pygame.font.Font("fuentes/mifuente.otf", 30)

personajes=[
    Jugador("Ronaldinho", speed=10, height=85, power=4.5, colour=GREEN, habilidad=False, recarga=10, imagen_path="imagenes/ronaldinho.png"),
    Jugador("Zidane", speed=8, height=90, power=5, colour=BLUE, habilidad=False, recarga=12, imagen_path="imagenes/zidane.png"),
    Jugador("Johan Cruyff", speed=9, height=70, power=4, colour=ORANGE, habilidad=False, recarga=10, imagen_path="imagenes/cruyff.png", habilidad_activada_time=3),
    Jugador("Casillas", speed=4, height=120, power=1.3, colour=RED, habilidad=False, recarga=5, imagen_path="imagenes/casillas.png", habilidad_activada_time=5)
]

def seleccion_personajes(personajes):
    jugador1 = None
    jugador2 = None
    seleccionando_jugador = 1
    indice_seleccion = 0

    while True:
        SCREEN.fill(BLACK)
        
        # Mostrar título
        titulo = LETTERING.render(f"Jugador {seleccionando_jugador}: Selecciona tu personaje", True, (255, 255, 255))
        SCREEN.blit(titulo, (WIDTH // 2 - titulo.get_width() // 2, 50))
        
        # Mostrar personaje actual
        personaje = personajes[indice_seleccion]
        imagen_personaje = pygame.transform.scale(personaje.imagen, (150, 150))
        SCREEN.blit(imagen_personaje, (WIDTH // 2 - 75, HEIGHT // 2 - 150))
        nombre = LETTERING.render(personaje.nombre, True, (255, 255, 255))
        SCREEN.blit(nombre, (WIDTH // 2 - nombre.get_width() // 2, HEIGHT // 2))

        # Mostrar controles
        controles = LETTERING.render("Flechas: Cambiar, Enter: Seleccionar", True, (255, 255, 255))
        SCREEN.blit(controles, (WIDTH // 2 - controles.get_width() // 2, HEIGHT - 50))
        
        pygame.display.flip()

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    indice_seleccion = (indice_seleccion + 1) % len(personajes)
                elif evento.key == pygame.K_LEFT:
                    indice_seleccion = (indice_seleccion - 1) % len(personajes)
                elif evento.key == pygame.K_RETURN:
                    if seleccionando_jugador == 1:
                        jugador1 = personajes[indice_seleccion]
                        seleccionando_jugador = 2
                    else:
                        jugador2 = personajes[indice_seleccion]
                        return jugador1, jugador2