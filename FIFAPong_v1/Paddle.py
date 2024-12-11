import time
import pygame

WIDTH, HEIGHT = 800, 600
class Paddle:
    def _init_(self, x, y, width, height, color, speed, power, jugador):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = speed
        self.power = power
        self.initial_x = x
        self.initial_y = y
        self.jugador = jugador

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, up_key, down_key, left_key, right_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        # Movimiento horizontal (solo para Ronaldinho)
        if self.jugador.nombre == "Ronaldinho" and self.jugador.habilidad:
            
            if keys[left_key] and self.rect.left > 0:  # Movimiento a la izquierda
                self.rect.x -= self.speed
            if keys[right_key] and self.rect.right < WIDTH // 2:  # Movimiento a la derecha (mitad del campo)
                self.rect.x += self.speed
            if time.time() - self.jugador.habilidad_activada_time > 5:
                self.jugador.habilidad = False
    
    def reset_paddle(self):
        """Restablece la posición de la raqueta a su ubicación inicial."""
        self.rect.x = self.initial_x
        self.rect.y = self.initial_y