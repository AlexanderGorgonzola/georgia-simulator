import pygame

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_length = 800
        self.main_image = pygame.image.load("images/bg.jpg")
        self.house_image = pygame.image.load("images/house_bg.jpg")

        self.player_speed = 0.4
        self.goat_speed = 0.5
        self.dog_speed = 0.7
        self.cat_speed = 1
        self.chicken_speed = 1.5