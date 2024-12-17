# Cargar imagen de inicio
import time
import pygame
HEIGHT, WIDTH = 600, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
LETTERING = pygame.font.Font("fuentes/Retro Gaming.ttf", 20)

imagen_inicio = pygame.image.load("imagenes/PortadaGrande.png")
imagen_inicio = pygame.transform.scale(imagen_inicio, (WIDTH, HEIGHT))

def mostrar_inicio(mostrando_inicio):
    # Mostrar imagen de inicio
    mensaje = "Pulsa espacio para jugar"
    color_mensaje = (255, 255, 255)
    rect_color = (0, 0, 0, 128)  # Color negro translúcido

    while mostrando_inicio:
        SCREEN.blit(imagen_inicio, (0, 0))
        # Crear rectángulo translúcido
        rect_surf = pygame.Surface((400, 50), pygame.SRCALPHA)
        rect_surf.fill(rect_color)
        rect_pos = (WIDTH // 2 - 200, HEIGHT // 2 + 100)
        SCREEN.blit(rect_surf, rect_pos)

        # Dibujar mensaje
        titulo = LETTERING.render(mensaje, True, color_mensaje)
        text_rect = titulo.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 125))
        SCREEN.blit(titulo, text_rect)

        pygame.display.flip()

        # Parpadeo del mensaje
        time.sleep(0.5)
        color_mensaje = (0, 0, 0) if color_mensaje == (255, 255, 255) else (255, 255, 255)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                mostrando_inicio = False
