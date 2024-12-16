import random
import time
import pygame

WIDTH, HEIGHT = 800, 600
class Paddle:
    def __init__(self, x, y, width, height, color, speed, jugador):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = speed
        self.initial_x = x
        self.initial_y = y
        self.jugador = jugador

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, up_key, down_key, left_key, right_key, ball):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        # Movimiento horizontal (solo para Casillas)
        if self.jugador.nombre == "Casillas" and self.jugador.habilidad == True:
            if keys[left_key]:  # Movimiento a la izquierda
                self.rect.x -= self.speed
            if keys[right_key]:  # Movimiento a la derecha (mitad del campo)
                self.rect.x += self.speed
            if time.time() - self.jugador.habilidad_activada_time > 5:
                self.jugador.habilidad = False
                self.reset_paddle()
        # Controlar la pelota para Johan Cruyff
        if self.jugador.nombre == "Johan Cruyff" and self.jugador.habilidad == True and ball.contact == True:
            if self.rect.centerx > 400: #derecha
                ball.x = self.rect.centerx - self.rect.width // 2 - ball.radius
            else:
                ball.x = self.rect.centerx + self.rect.width // 2 + ball.radius
            
            ball.y = self.rect.centery
            if time.time() - self.jugador.habilidad_activada_time > 3:
                ball.contact = False
                self.jugador.habilidad = False
                if self.rect.centerx > 400: #derecha
                    ball.speed_x = 5
                else:
                    ball.speed_x = -5  # Chute más potente
                ball.speed_y = random.uniform(-2, 2)
    
    def reset_paddle(self):
        self.rect.x = self.initial_x
        self.rect.y = self.initial_y