import pygame  # Importació necessària
import random

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

class Ball:
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.initial_speed_x = speed_x  
        self.initial_speed_y = speed_y

        self.speed_decay = 0.98  # Factor de reducción (98% de la velocidad anterior por frame)
        self.min_speed = 3  # Velocidad mínima

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    def move(self):
        # Reducir velocidad gradualmente
        self.speed_x *= self.speed_decay
        self.speed_y *= self.speed_decay

        # Limitar a una velocidad mínima
        if abs(self.speed_x) < self.min_speed:
            self.speed_x = self.min_speed if self.speed_x > 0 else -self.min_speed
        if abs(self.speed_y) < self.min_speed:
            self.speed_y = self.min_speed if self.speed_y > 0 else -self.min_speed

        # Actualizar posición
        self.x += self.speed_x
        self.y += self.speed_y

        # Rebotar en las paredes horizontales
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.speed_y *= -1

    def check_collision(self, paddle1, paddle2):
            
        if self.x - self.radius <= paddle1.rect.right and paddle1.rect.top < self.y < paddle1.rect.bottom:
            if paddle1.jugador.nombre=="Ronaldinho" and paddle1.jugador.habilidad==True:
                self.speed_x *= -1*(paddle1.jugador.power+3)
                self.speed_y *= -1
                paddle1.jugador.habilidad=False
            else: 
                self.speed_x *= -1*paddle1.jugador.power
                self.speed_y *= paddle1.jugador.power
        if self.x + self.radius >= paddle2.rect.left and paddle2.rect.top < self.y < paddle2.rect.bottom:
            if paddle2.jugador.nombre=="Ronaldinho" and paddle2.jugador.habilidad==True:
                self.speed_x *= -1*(paddle1.jugador.power+3)
                self.speed_y *= -1
                paddle2.jugador.habilidad==False
            else: 
                self.speed_x *= -1*paddle2.jugador.power
                self.speed_y *= paddle2.jugador.power

    def reset_ball(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed_x = random.choice([-4, 4])  # Trajectòria aleatòria
        self.speed_y = random.choice([-3, 3])