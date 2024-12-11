import pygame
import time

# Configuración inicial de Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Barra de Carga de Habilidad")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FPS = 60

class BarraHabilidad:
    def __init__(self, x, y, width, height, tiempo_recarga):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.tiempo_recarga = tiempo_recarga  # Tiempo necesario para recargar completamente (en segundos)
        self.progreso = 0  # Progreso actual (0 a 1)
        self.cargando = False  # Indica si se está recargando
        self.inicio_recarga = None
        self.activar=False

    def empezar_recarga(self):
        """Inicia la recarga de la habilidad."""
        if not self.cargando:
            self.cargando = True
            self.inicio_recarga = time.time()  # Marca el tiempo inicial de recarga

    def actualizar(self):
        """Actualiza el estado de la barra según el tiempo transcurrido."""
        if self.cargando:
            tiempo_transcurrido = time.time() - self.inicio_recarga
            self.progreso = min(tiempo_transcurrido / self.tiempo_recarga, 1)  # Asegura que no pase de 1
            if self.progreso >= 1:
                self.cargando = False  # Recarga completa

    def draw(self, screen):
        """Dibuja la barra en la pantalla."""
        # Dibujar fondo de la barra
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
        # Dibujar progreso (barra verde)
        ancho_progreso = int(self.width * self.progreso)
        pygame.draw.rect(screen, GREEN, (self.x, self.y, ancho_progreso, self.height))

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_a:  # Activar habilidad para la barra izquierda
#                 barra_izquierda.empezar_recarga()
#             if event.key == pygame.K_l:  # Activar habilidad para la barra derecha
#                 barra_derecha.empezar_recarga()

#     # Actualizar
#     SCREEN.fill(BLACK)
#     barra_izquierda.actualizar()
#     barra_derecha.actualizar()

#     # Dibujar
#     barra_izquierda.dibujar(SCREEN)
#     barra_derecha.dibujar(SCREEN)

#     pygame.display.flip()
#     clock.tick(FPS)