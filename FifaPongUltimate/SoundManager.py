import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()

        # Sonidos generales
        self.goal_sound = pygame.mixer.Sound("sounds/gol.wav")
        self.background_music = pygame.mixer.Sound("sounds/pes6.wav")

        # Sonidos de impacto de jugadores
        self.player1_hit_sound = pygame.mixer.Sound("sounds/player1_hit.wav")
        self.player2_hit_sound = pygame.mixer.Sound("sounds/player2_hit.wav")

        # Sonidos de selección de personajes
        self.player_select_sounds = {
            "Ronaldinho": pygame.mixer.Sound("sounds/ronalinhosoccer.mp3"),
            "Zidane": pygame.mixer.Sound("sounds/Zidaneaudio.mp3"),
            "Johan Cruyff": pygame.mixer.Sound("sounds/johancruyff.mp3"),
            "Casillas": pygame.mixer.Sound("sounds/CasillasSanto.mp3")
        }


        # Configurar volúmenes de sonidos de selección específicos
        self.player_select_sounds["Ronaldinho"].set_volume(1)  # Volumen más bajo para Ronaldinho
        self.player_select_sounds["Zidane"].set_volume(0.9)      # Volumen más alto para Zidane
        self.player_select_sounds["Johan Cruyff"].set_volume(1)  # Volumen más alto para Cruyff
        self.player_select_sounds["Casillas"].set_volume(0.9)    # Volumen más alto para Casillas
        self.background_music.set_volume(0.4)  # Volumen más bajo para la música de fondo

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

    def play_player_select_sound(self, player_name):
        """Reproducir sonido de selección de personaje"""
        if player_name in self.player_select_sounds:
            self.player_select_sounds[player_name].play()
        else:
            print(f"Sonido de selección para {player_name} no encontrado.")