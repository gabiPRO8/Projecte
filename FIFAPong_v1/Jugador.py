import pygame

class Jugador:
    def __init__(self, nombre, speed, height, power, habilidad, imagen_path, habilidad_activada_time=None):
        self.nombre = nombre
        self.speed = speed
        self.height = height
        self.power = power
        self.habilidad = habilidad
        self.habilidad_activada_time = habilidad_activada_time
        self.imagen = pygame.image.load(imagen_path)
        self.rect = self.imagen.get_rect()

    def mover(self, direccion, limites):
        if direccion == "arriba" and self.rect.top > 0:
            self.rect.move_ip(0, -self.velocidad)
        elif direccion == "abajo" and self.rect.bottom < limites:
            self.rect.move_ip(0, self.velocidad)