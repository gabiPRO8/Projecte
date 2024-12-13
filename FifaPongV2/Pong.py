import pygame
import time
from pygame.locals import *

pygame.init()

# Configuración de la ventana
size = 800, 600
ventana = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
ancho, alto = pygame.display.get_surface().get_size()

# Colores
colorfondo = 25, 235, 215
colortexto = 0, 233, 55

# Fuente
tipoletra = pygame.font.Font("fuentes/mifuente.otf", 30)

# Personajes (nombre, imagen, descripción, habilidad)
personajes = [
    {"nombre": "Ronaldinho", "imagen": pygame.image.load("imagenes/ronaldinho.png"), "descripcion": "Efecto al balón.", "habilidad": "efecto"},
    {"nombre": "Defensor", "imagen": pygame.image.load("imagenes/personaje2.png"), "descripcion": "Mayor tamaño.", "habilidad": "defensa"},
    {"nombre": "Agresivo", "imagen": pygame.image.load("imagenes/personaje3.png"), "descripcion": "Golpes más fuertes.", "habilidad": "ataque"},
    {"nombre": "Equilibrado", "imagen": pygame.image.load("imagenes/personaje4.png"), "descripcion": "Balanceado.", "habilidad": "equilibrio"},
]

# Función para mostrar la pantalla de selección de personajes
def seleccion_personajes():
    jugador1 = None
    jugador2 = None
    seleccionando_jugador = 1
    indice_seleccion = 0

    while True:
        ventana.fill(colorfondo)
        
        # Mostrar título
        titulo = tipoletra.render(f"Jugador {seleccionando_jugador}: Selecciona tu personaje", True, (255, 255, 255))
        ventana.blit(titulo, (ancho // 2 - titulo.get_width() // 2, 50))
        
        # Mostrar personaje actual
        personaje = personajes[indice_seleccion]
        imagen_personaje = pygame.transform.scale(personaje["imagen"], (150, 150))
        ventana.blit(imagen_personaje, (ancho // 2 - 75, alto // 2 - 150))
        nombre = tipoletra.render(personaje["nombre"], True, (255, 255, 255))
        descripcion = tipoletra.render(personaje["descripcion"], True, (255, 255, 255))
        ventana.blit(nombre, (ancho // 2 - nombre.get_width() // 2, alto // 2))
        ventana.blit(descripcion, (ancho // 2 - descripcion.get_width() // 2, alto // 2 + 40))
        
        # Mostrar controles
        controles = tipoletra.render("Flechas: Cambiar, Enter: Seleccionar", True, (255, 255, 255))
        ventana.blit(controles, (ancho // 2 - controles.get_width() // 2, alto - 50))
        
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

# Carga de imágenes y rectángulos
pelota_original = pygame.image.load("imagenes/ball.png")
pelota_rect = pelota_original.get_rect(center=(400, 300))

jugador1 = pygame.image.load("imagenes/bate.png")
jugador1_rect = jugador1.get_rect(midleft=(50, alto // 2))

jugador2 = pygame.image.load("imagenes/palazul.png")
jugador2_rect = jugador2.get_rect(midright=(ancho - 50, alto // 2))

# Fondo
fondo = pygame.image.load("imagenes/fondo.png")
fondo = pygame.transform.scale(fondo, (ancho, alto))

# Sonidos
choqueSonido = pygame.mixer.Sound("sonidos/sfx_zap.ogg")

# Puntuación
puntosJugador1 = 0
puntosJugador2 = 0

# Velocidad de la pelota
velocidad_pelota = [3, 3]
aceleracion = 0.2  # Incremento de velocidad al ser golpeada

# Reloj para limitar los FPS
reloj = pygame.time.Clock()

# Constante para el máximo de puntos
PUNTOS_MAXIMOS = 5

# Selección de personajes antes del inicio del juego
jugador1_seleccion, jugador2_seleccion = seleccion_personajes()

# Habilidad específica de Ronaldinho
def aplicar_efecto():
    return 2  # Cambio de dirección en Y para simular curvatura

# Bucle principal del juego
run = True
while run:
    pelota_rect = pelota_rect.move(velocidad_pelota)
    
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False
    
    # Colisión con paredes verticales (goles)
    if pelota_rect.left <= 0 or pelota_rect.right >= ancho:
        if pelota_rect.left <= 0:
            puntosJugador2 += 1
        if pelota_rect.right >= ancho:
            puntosJugador1 += 1

        if puntosJugador1 == PUNTOS_MAXIMOS or puntosJugador2 == PUNTOS_MAXIMOS:
            run = False
            break

        mensaje = tipoletra.render("¡Gol!", True, (255, 255, 255))
        ventana.blit(fondo, (0, 0))
        ventana.blit(mensaje, (ancho // 2 - 50, alto // 2 - 20))
        pygame.display.flip()
        time.sleep(2)
        pelota_rect = pelota_original.get_rect(center=(400, 300))
        velocidad_pelota = [3, 3]

    if pelota_rect.top <= 0 or pelota_rect.bottom >= alto:
        velocidad_pelota[1] = -velocidad_pelota[1]

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and jugador1_rect.top > 0:
        jugador1_rect.move_ip(0, -5)
    if keys[pygame.K_DOWN] and jugador1_rect.bottom < alto:
        jugador1_rect.move_ip(0, 5)

    if keys[pygame.K_w] and jugador2_rect.top > 0:
        jugador2_rect.move_ip(0, -5)
    if keys[pygame.K_s] and jugador2_rect.bottom < alto:
        jugador2_rect.move_ip(0, 5)

    # Colisión de la pelota con jugadores
    if jugador1_rect.colliderect(pelota_rect):
        choqueSonido.play()
        velocidad_pelota[0] = -velocidad_pelota[0] + aceleracion
        if jugador1_seleccion["habilidad"] == "efecto":
            velocidad_pelota[1] += aplicar_efecto()

    if jugador2_rect.colliderect(pelota_rect):
        choqueSonido.play()
        velocidad_pelota[0] = -velocidad_pelota[0] - aceleracion
        if jugador2_seleccion["habilidad"] == "efecto":
            velocidad_pelota[1] += aplicar_efecto()

    ventana.blit(fondo, (0, 0))
    textojugador1 = tipoletra.render(f"Jugador 1: {puntosJugador1}", True, colortexto)
    textojugador2 = tipoletra.render(f"Jugador 2: {puntosJugador2}", True, colortexto)
    ventana.blit(textojugador1, (20, 20))
    ventana.blit(textojugador2, (ancho // 2 + 20, 20))
    ventana.blit(pelota_original, pelota_rect)
    ventana.blit(jugador1, jugador1_rect)
    ventana.blit(jugador2, jugador2_rect)

    pygame.display.flip()
    reloj.tick(60)

ventana.fill(colorfondo)
if puntosJugador1 == PUNTOS_MAXIMOS:
    mensaje_final = "¡Jugador 1 gana!"
else:
    mensaje_final = "¡Jugador 2 gana!"

mensaje = tipoletra.render(mensaje_final, True, (255, 255, 255))
ventana.blit(mensaje, (ancho // 2 - 100, alto // 2 - 20))
pygame.display.flip()
time.sleep(3)

pygame.quit()