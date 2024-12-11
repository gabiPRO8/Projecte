import pygame
from Countdown import Countdown
from SoundManager import SoundManager 

# Configuració inicial
pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Futbol Pong")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FPS = 60
LETTERING = pygame.font.Font("fuentes/mifuente.otf", 30)

sound = SoundManager()
count = Countdown(LETTERING,SCREEN)

class Score:
    def __init__(self):
        self.player1 = 0
        self.player2 = 0
        self.font = pygame.font.Font(None, 74)

    def draw(self, screen):
        score_text = f"{self.player1} - {self.player2}"
        text = self.font.render(score_text, True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 20))

    def update(self, ball):
        if ball.x - ball.radius <= 0:  # Gol del jugador 2
            self.player2 += 1
            ball.x, ball.y = WIDTH // 2, HEIGHT // 2
            ball.reset_ball()
            sound.play_goal_sound()
            count.start()
            ball.reset_ball()

        if ball.x + ball.radius >= WIDTH:  # Gol del jugador 1
            self.player1 += 1
            ball.x, ball.y = WIDTH // 2, HEIGHT // 2
            ball.reset_ball()
            sound.play_goal_sound()
            count.start()
            ball.reset_ball()