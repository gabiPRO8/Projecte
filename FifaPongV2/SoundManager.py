import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.goal_sound = pygame.mixer.Sound("sounds/gol.wav")  # Ruta al so del gol

    def play_goal_sound(self):
        self.goal_sound.play()