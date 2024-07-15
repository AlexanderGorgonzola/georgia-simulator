import pygame
class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_length = 800
        self.bg_image = pygame.image.load("images/bg.jpg")

        self.player_speed = 0.4