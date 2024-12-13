import time
import pygame
from BarraHabilidad import BarraHabilidad
from Paddle import Paddle
from Ball import Ball
from Score import Score
from personajes import seleccion_personajes, personajes

# Configuració inicial
pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
LETTERING = pygame.font.Font("fuentes/mifuente.otf", 30)
pygame.display.set_caption("Futbol Pong")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FPS = 60

def main():
    clock = pygame.time.Clock()
    ball = Ball(WIDTH // 2, HEIGHT // 2, 10, WHITE, 2, 2)
    score = Score()
    jugador1_data, jugador2_data= seleccion_personajes(personajes)
    paddle1 = Paddle(30, HEIGHT // 2 - 50, 10, jugador1_data.height, jugador1_data.colour, jugador1_data.speed, jugador1_data)
    paddle2 = Paddle(WIDTH - 40, HEIGHT // 2 - 50, 10, jugador2_data.height, jugador2_data.colour, jugador2_data.speed, jugador2_data)
    barra1 = BarraHabilidad(50, HEIGHT - 10, 200, 10, jugador1_data.recarga)  # Barra inferior izquierda
    barra2 = BarraHabilidad(WIDTH - 250, HEIGHT - 10, 200, 10, jugador2_data.recarga)  # Barra inferior derecha

    running = True
    start= True
    while running:
        if start==True:
            start=False
            barra1.empezar_recarga()
            barra2.empezar_recarga()

        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and barra1.cargando == False:  # Activar habilidad para la barra izquierda
                    paddle1.jugador.habilidad=True
                    paddle1.jugador.habilidad_activada_time = time.time()
                    barra1.empezar_recarga()
                if event.key == pygame.K_l and barra2.cargando == False:  # Activar habilidad para la barra derecha
                    paddle2.jugador.habilidad=True
                    paddle2.jugador.habilidad_activada_time = time.time()
                    barra2.empezar_recarga()

        paddle1.move(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, ball)
        paddle2.move(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, ball)
        barra1.actualizar()
        barra2.actualizar()
        ball.move()
        ball.check_collision(paddle1, paddle2)
        if score.update(ball):  # Verificar si el juego debe reiniciarse
            score.reset_game()
            jugador1_data, jugador2_data = seleccion_personajes(personajes)  # Volver a la selección de personajes
            paddle1 = Paddle(30, HEIGHT // 2 - 50, 10, jugador1_data.height, jugador1_data.colour, jugador1_data.speed, jugador1_data)
            paddle2 = Paddle(WIDTH - 40, HEIGHT // 2 - 50, 10, jugador2_data.height, jugador2_data.colour, jugador2_data.speed, jugador2_data)
            barra1 = BarraHabilidad(50, HEIGHT - 10, 200, 10, jugador1_data.recarga)  # Barra inferior izquierda
            barra2 = BarraHabilidad(WIDTH - 250, HEIGHT - 10, 200, 10, jugador2_data.recarga)  # Barra inferior derecha
            start = True

        paddle1.draw(SCREEN)
        paddle2.draw(SCREEN)
        ball.draw(SCREEN)
        score.draw(SCREEN)
        barra1.draw(SCREEN)
        barra2.draw(SCREEN)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()