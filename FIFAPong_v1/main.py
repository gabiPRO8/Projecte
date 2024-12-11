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
    paddle1 = Paddle(30, HEIGHT // 2 - 50, 10, jugador1_data.height, RED, jugador1_data.speed, jugador1_data)
    paddle2 = Paddle(WIDTH - 40, HEIGHT // 2 - 50, 10, jugador2_data.height, BLUE, jugador2_data.speed, jugador2_data)
    barra1 = BarraHabilidad(50, HEIGHT - 10, 200, 10, 3)  # Barra inferior izquierda
    barra2 = BarraHabilidad(WIDTH - 250, HEIGHT - 10, 200, 10, 3)  # Barra inferior derecha

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
                if event.key == pygame.K_a:  # Activar habilidad para la barra izquierda
                    paddle1.jugador.habilidad=True
                    barra1.empezar_recarga()
                if event.key == pygame.K_l:  # Activar habilidad para la barra derecha
                    paddle2.jugador.habilidad=True
                    barra2.empezar_recarga()

        paddle1.move(pygame.K_w, pygame.K_s)
        paddle2.move(pygame.K_UP, pygame.K_DOWN)
        barra1.actualizar()
        barra2.actualizar()
        ball.move()
        ball.check_collision(paddle1, paddle2)
        score.update(ball)

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
