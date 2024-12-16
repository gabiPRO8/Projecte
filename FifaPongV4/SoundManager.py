import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        
        # Sonidos generales
        self.goal_sound = pygame.mixer.Sound("sounds/gol.wav")
        self.background_music = pygame.mixer.Sound("sounds/background_music.wav")
        # Sonidos de impacto de jugadores
        self.player1_hit_sound = pygame.mixer.Sound("sounds/player1_hit.wav")
        self.player2_hit_sound = pygame.mixer.Sound("sounds/player2_hit.wav")
        
        # Configurar volúmenes
        self.background_music.set_volume(0.1)  # Música de fondo muy bajita
        self.goal_sound.set_volume(0.5)  # Sonido de gol moderado
        self.player1_hit_sound.set_volume(0.7)  # Sonido de impacto del jugador 1
        self.player2_hit_sound.set_volume(0.7)  # Sonido de impacto del jugador 2

    def play_player1_hit_sound(self):
        """Reproducir sonido de impacto para el jugador 1"""
        self.player1_hit_sound.play()

    def play_player2_hit_sound(self):
        """Reproducir sonido de impacto para el jugador 2"""
        self.player2_hit_sound.play()

    def play_goal_sound(self):
        """Reproducir sonido de gol"""
        self.goal_sound.play()

    def play_background_music(self, loops=-1):
        """Reproducir música de fondo"""
        self.background_music.play(loops)

                    