import pygame
import time

class Countdown:
    def __init__(self, font, screen, duration=3):
        self.font = font
        self.screen = screen
        self.duration = duration

    def start(self):
        for i in range(self.duration, 0, -1):
            self.screen.fill((0, 0, 0))
            text = self.font.render(str(i), True, (255, 255, 255))
            self.screen.blit(text, (400 - text.get_width() // 2, 300 - text.get_height() // 2))
            pygame.display.flip()
            time.sleep(1)