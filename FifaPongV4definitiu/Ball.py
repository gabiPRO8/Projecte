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
    def __init__(self, x, y, radius, color, speed_x, speed_y, spin=False):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.initial_speed_x = speed_x  
        self.initial_speed_y = speed_y
        self.spin = spin
        self.contact = False

        self.speed_decay = 0.98  # Factor de reducción (98% de la velocidad anterior por frame)
        self.min_speed = 3  # Velocidad mínima

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    def move(self,sound_manager=None):
        self.speed_decay = 0.98
        # Reducir velocidad gradualmente
        if self.spin:
            self.speed_decay = 0.95
            self.speed_y *= self.speed_decay

            # Limitar a una velocidad mínima
            if abs(self.speed_x) < self.min_speed:
                self.speed_x = self.min_speed if self.speed_x > 0 else -self.min_speed

            # Rebotar en las paredes horizontales
            if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
                self.speed_y *= -1
        else:
            self.speed_x *= self.speed_decay
            self.speed_y *= self.speed_decay

            # Limitar a una velocidad mínima
            if abs(self.speed_y) < self.min_speed:
                self.speed_y = self.min_speed if self.speed_y > 0 else -self.min_speed
            if abs(self.speed_x) < self.min_speed:
                self.speed_x = self.min_speed if self.speed_x > 0 else -self.min_speed

            # Rebotar en las paredes horizontales
            if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
                self.speed_y *= -1

        # Actualizar posición
        self.x += self.speed_x
        self.y += self.speed_y


    def check_collision(self, paddle1, paddle2,sound_manager=None):
        # jugador 1 (izquierda) chuta
        if self.x - self.radius <= paddle1.rect.right and paddle1.rect.top < self.y < paddle1.rect.bottom:
            if sound_manager:
                sound_manager.play_player1_hit_sound()
            if paddle1.jugador.nombre == "Johan Cruyff" and paddle1.jugador.habilidad == True:
                self.spin = False
                # habilidad cruyff: controlar la pelota
                self.contact = True
                self.speed_x = 0
                self.speed_y = 0

            elif paddle1.jugador.nombre == "Ronaldinho" and paddle1.jugador.habilidad == True:
                # habilidad ronnie: meter efecto a la pelota
                self.spin = True
                self.speed_x *= -1 * (paddle1.jugador.power)
                self.speed_y *= -1 * (paddle1.jugador.power + 1.5) * random.uniform(0.7, 1.7)
                paddle1.jugador.habilidad = False
            elif paddle1.jugador.nombre == "Zidane" and paddle1.jugador.habilidad == True:
                self.spin = False
                # habilidad zizou: trallazo
                self.speed_x *= -1 * (paddle1.jugador.power + 9)
                self.speed_y = 0.5 * random.choice([-1, 1])
                paddle1.jugador.habilidad = False
            elif paddle1.jugador.nombre == "Casillas" and paddle1.jugador.habilidad == True:
                self.spin = False
                #habilidad casillas: 
                self.speed_x = abs(paddle1.speed)+1.5
                self.speed_y = 1 * random.choice([-1, 1])
                
            else:
                self.spin = False
                self.speed_x *= -1 * paddle1.jugador.power
                self.speed_y *= paddle1.jugador.power

        # jugador 2 (derecha) chuta
        if self.x + self.radius >= paddle2.rect.left and paddle2.rect.top < self.y < paddle2.rect.bottom:
            if sound_manager:
                sound_manager.play_player2_hit_sound()
            if paddle2.jugador.nombre == "Johan Cruyff" and paddle2.jugador.habilidad == True:
                self.spin = False
                # habilidad cruyff: controlar la pelota
                self.contact = True
                self.speed_x = 0
                self.speed_y = 0

            elif paddle2.jugador.nombre == "Ronaldinho" and paddle2.jugador.habilidad == True:
                # habilidad ronnie
                self.spin = True
                self.speed_x *= -1 * (paddle2.jugador.power)
                self.speed_y *= -1 * (paddle2.jugador.power + 1.5) * random.uniform(0.7, 1.7)
                paddle2.jugador.habilidad = False
            elif paddle2.jugador.nombre == "Zidane" and paddle2.jugador.habilidad == True:
                self.spin = False
                # habilidad zizou
                self.speed_x *= -1 * (paddle2.jugador.power + 9)
                self.speed_y = 0.5 * random.choice([-1, 1])
                paddle2.jugador.habilidad = False
            elif paddle2.jugador.nombre == "Casillas" and paddle2.jugador.habilidad == True:
                self.spin = False
                # habilidad casillas
                self.speed_x = -abs(paddle2.speed)-1.5
                self.speed_y = 1 * random.choice([-1, 1])
            else:
                self.spin = False
                self.speed_x *= -1 * paddle2.jugador.power
                self.speed_y *= paddle2.jugador.power

    def reset_ball(self):
        self.spin=False
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed_x = random.choice([-4, 4])  # Trajectòria aleatòria
        self.speed_y = random.choice([-3, 3])