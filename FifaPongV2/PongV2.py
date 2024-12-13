import pygame
import time
from pygame.locals import *

pygame.init()

# Configuración general
size = 800, 600
ventana = pygame.display.set_mode(size)
pygame.display.set_caption("Pong Mejorado")
ancho, alto = pygame.display.get_surface().get_size()

# Colores y fuente
colorfondo = (25, 235, 215)
colortexto = (0, 233, 55)
tipoletra = pygame.font.Font("fuentes/mifuente.otf", 30)

# Velocidad base de la pelota
VELOCIDAD_BASE = 3
ACELERACION_BASE = 0.2

# Clase Jugador
class Jugador:
    def __init__(self, nombre, velocidad, tamaño, potencia, habilidad, imagen_path):
        self.nombre = nombre
        self.velocidad = velocidad
        self.tamaño = tamaño
        self.potencia = potencia
        self.habilidad = habilidad
        self.imagen = pygame.image.load(imagen_path)
        self.rect = self.imagen.get_rect()

    def mover(self, direccion, limites):
        if direccion == "arriba" and self.rect.top > 0:
            self.rect.move_ip(0, -self.velocidad)
        elif direccion == "abajo" and self.rect.bottom < limites:
            self.rect.move_ip(0, self.velocidad)

# Clase Pelota
import math

class Pelota:
    def __init__(self, velocidad, imagen_path):
        self.velocidad = velocidad
        self.imagen = pygame.image.load(imagen_path)
        self.rect = self.imagen.get_rect(center=(ancho // 2, alto // 2))
        self.direccion = [VELOCIDAD_BASE, VELOCIDAD_BASE]
        self.parabolica = False  # Indica si la trayectoria es parabólica
        self.a = 0  # Coeficiente de curvatura de la parábola
        self.h = 0  # Vértice en el eje X
        self.k = 0  # Vértice en el eje Y
        self.signo = 1  # Controla la dirección del efecto parabólico (arriba/abajo)

    def activar_parabolica(self, jugador):
        # Calcula los parámetros de la parábola según el golpe
        self.parabolica = True
        self.h = self.rect.centerx
        self.k = self.rect.centery
        self.signo = -1 if jugador.rect.centery > alto // 2 else 1  # Define si la parábola sube o baja
        self.a = 8 * self.signo  # Curvatura ajustable

    def mover(self):
        if self.parabolica:
            # Movimiento parabólico
            self.rect.x += self.direccion[0]
            desplazamiento_x = self.rect.centerx - self.h
            self.rect.y = self.a * (desplazamiento_x ** 2) + self.k

            # Verifica si la parábola debe detenerse (cuando salga del área)
            if self.rect.top <= 0 or self.rect.bottom >= alto or desplazamiento_x > 200:
                self.parabolica = False  # Detenemos la curvatura

        else:
            # Movimiento lineal estándar
            self.rect.x += self.direccion[0]
            self.rect.y += self.direccion[1]

    def verificar_colisiones(self, jugador1, jugador2):
        # Colisión con paredes horizontales
        if self.rect.top <= 0 or self.rect.bottom >= alto:
            self.direccion[1] = -self.direccion[1]
        
        # Colisión con jugadores
        if self.rect.colliderect(jugador1.rect):
            self.direccion[0] = -self.direccion[0] + jugador1.potencia * ACELERACION_BASE
            if jugador1.habilidad == "efecto":
                self.activar_parabolica(jugador1)

        if self.rect.colliderect(jugador2.rect):
            self.direccion[0] = -self.direccion[0] - jugador2.potencia * ACELERACION_BASE
            if jugador2.habilidad == "efecto":
                self.activar_parabolica(jugador2)


# class Pelota:
#     def __init__(self, velocidad, imagen_path):
#         self.velocidad = velocidad
#         self.imagen = pygame.image.load(imagen_path)
#         self.rect = self.imagen.get_rect(center=(ancho // 2, alto // 2))
#         self.direccion = [VELOCIDAD_BASE, VELOCIDAD_BASE]
#         self.curvatura = 0  # Magnitud de la curvatura (eje Y)

#     def mover(self):
#         # Movimiento normal con curvatura en el eje Y
#         self.rect.x += self.direccion[0]
#         self.rect.y += self.direccion[1] + self.curvatura

#         # Gradualmente reduce la curvatura hacia 0 (decadencia natural)
#         if self.curvatura > 0:
#             self.curvatura -= 0.1
#         elif self.curvatura < 0:
#             self.curvatura += 0.1

#     def verificar_colisiones(self, jugador1, jugador2):
#         # Colisión con paredes horizontales
#         if self.rect.top <= 0 or self.rect.bottom >= alto:
#             self.direccion[1] = -self.direccion[1]
        
#         # Colisión con jugadores
#         if self.rect.colliderect(jugador1.rect):
#             self.direccion[0] = -self.direccion[0] + jugador1.potencia * ACELERACION_BASE
#             if jugador1.habilidad == "efecto":
#                 self.curvatura = 1000  # Aplica curvatura en el eje Y 

#         if self.rect.colliderect(jugador2.rect):
#             self.direccion[0] = -self.direccion[0] - jugador2.potencia * ACELERACION_BASE
#             if jugador2.habilidad == "efecto":
#                 self.curvatura = -1000  # Aplica curvatura en el eje Y (opuesta)

# Función de selección de personajes
def seleccion_personajes(personajes):
    jugador1 = None
    jugador2 = None
    seleccionando = 1
    indice = 0

    while True:
        ventana.fill(colorfondo)
        titulo = tipoletra.render(f"Jugador {seleccionando}: Selecciona tu personaje", True, (255, 255, 255))
        ventana.blit(titulo, (ancho // 2 - titulo.get_width() // 2, 50))

        personaje = personajes[indice]
        imagen = pygame.transform.scale(personaje["imagen"], (150, 150))
        ventana.blit(imagen, (ancho // 2 - 75, alto // 2 - 150))
        nombre = tipoletra.render(personaje["nombre"], True, (255, 255, 255))
        descripcion = tipoletra.render(personaje["descripcion"], True, (255, 255, 255))
        ventana.blit(nombre, (ancho // 2 - nombre.get_width() // 2, alto // 2))
        ventana.blit(descripcion, (ancho // 2 - descripcion.get_width() // 2, alto // 2 + 40))
        
        controles = tipoletra.render("Flechas: Cambiar, Enter: Seleccionar", True, (255, 255, 255))
        ventana.blit(controles, (ancho // 2 - controles.get_width() // 2, alto - 50))
        
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    indice = (indice + 1) % len(personajes)
                elif evento.key == pygame.K_LEFT:
                    indice = (indice - 1) % len(personajes)
                elif evento.key == pygame.K_RETURN:
                    if seleccionando == 1:
                        jugador1 = personajes[indice]
                        seleccionando = 2
                    else:
                        jugador2 = personajes[indice]
                        return jugador1, jugador2

# Lógica principal del juego
def main():
    # Crear jugadores y pelota
    pelota = Pelota([VELOCIDAD_BASE, VELOCIDAD_BASE], "imagenes/ball.png")
    
    # Lista de personajes
    personajes = [
        {"nombre": "Ronaldinho", "velocidad": 5, "tamaño": 100, "potencia": 1, "habilidad": "efecto", "imagen": "imagenes/ronaldinho.png"},
        {"nombre": "Defensor", "velocidad": 3, "tamaño": 150, "potencia": 0.5, "habilidad": "bloqueo", "imagen": "imagenes/personaje2.png"},
        {"nombre": "Agresivo", "velocidad": 4, "tamaño": 90, "potencia": 2, "habilidad": "ataque", "imagen": "imagenes/personaje3.png"},
        {"nombre": "Equilibrado", "velocidad": 4, "tamaño": 100, "potencia": 1, "habilidad": "equilibrio", "imagen": "imagenes/personaje4.png"}
    ]

    # Selección de personajes
    jugador1_data, jugador2_data = seleccion_personajes(personajes)
    jugador1 = Jugador(**jugador1_data)
    jugador2 = Jugador(**jugador2_data)
    jugador1.rect.midleft = (50, alto // 2)
    jugador2.rect.midright = (ancho - 50, alto // 2)
    print(jugador1.habilidad)

    # Bucle principal
    run = True
    reloj = pygame.time.Clock()
    while run:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False

        # Movimiento de jugadores
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            jugador1.mover("arriba", alto)
        if keys[pygame.K_s]:
            jugador1.mover("abajo", alto)
        if keys[pygame.K_UP]:
            jugador2.mover("arriba", alto)
        if keys[pygame.K_DOWN]:
            jugador2.mover("abajo", alto)

        # Actualizar pelota
        pelota.mover()
        pelota.verificar_colisiones(jugador1, jugador2)

        # Dibujar elementos
        ventana.fill(colorfondo)
        ventana.blit(pelota.imagen, pelota.rect)
        ventana.blit(jugador1.imagen, jugador1.rect)
        ventana.blit(jugador2.imagen, jugador2.rect)
        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
