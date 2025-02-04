import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, georgia):
        super().__init__()
        self.screen = georgia.screen
        self.settings = georgia.settings
        self.screen_rect = georgia.screen.get_rect()

        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right + 20:
            self.x += self.settings.player_speed
        if self.moving_left and self.rect.left > -20:
            self.x -= self.settings.player_speed
        if self.moving_up and self.rect.top > -20:
            self.y -= self.settings.player_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom + 20:
            self.y += self.settings.player_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_player(self):
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

class Car(Sprite):
    def __init__(self, georgia):
        super().__init__()
        self.screen = georgia.screen
        self.settings = georgia.settings
        self.screen_rect = georgia.screen.get_rect()

        self.image = pygame.image.load('images/car.jpg')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def blitme(self):
        self.screen.blit(self.image, self.rect)