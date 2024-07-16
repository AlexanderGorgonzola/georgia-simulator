import pygame
from pygame.sprite import Sprite
from pygame.locals import *
class Goat(Sprite):
    def __init__(self, georgia):
        super().__init__()
        self.screen = georgia.screen
        self.screen_rect = georgia.screen.get_rect()
        self.settings = georgia.settings
        self.image = pygame.image.load("images/goat.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.bottom = self.screen_rect.bottom - 60
        self.speed = self.settings.goat_speed

    def update(self):
        self.x += self.speed
        if self.x >= 1100:
            self.x = 1100
            self.speed *= -1
        elif self.x <= 0:
            self.x = 0
            self.speed *= -1
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Dog(Sprite):
    def __init__(self, georgia):
        super().__init__()
        self.screen = georgia.screen
        self.screen_rect = georgia.screen.get_rect()
        self.settings = georgia.settings
        self.image = pygame.image.load("images/dog.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.rect.midbottom = self.screen_rect.midtop
        self.rect.top = self.screen_rect.top + 70
        self.speed = self.settings.dog_speed

    def update(self):
        self.x -= self.speed
        if self.x >= 1100:
            self.x = 1100
            self.speed *= -1
        elif self.x <= 0:
            self.x = 0
            self.speed *= -1
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
class Cat(Sprite):
    def __init__(self, georgia):
        super().__init__()
        self.screen = georgia.screen
        self.screen_rect = georgia.screen.get_rect()
        self.settings = georgia.settings
        self.image = pygame.image.load("images/cat.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.rect.midleft = self.screen_rect.midleft
        self.rect.left = self.screen_rect.left + 20
        self.speed = self.settings.cat_speed

    def update(self):
        self.y += self.speed
        if self.y >= 750:
            self.y = 750
            self.speed *= -1
        elif self.y <= 0:
            self.y = 0
            self.speed *= -1
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Chicken(Sprite):
    def __init__(self, georgia):
        super().__init__()
        self.screen = georgia.screen
        self.screen_rect = georgia.screen.get_rect()
        self.settings = georgia.settings
        self.image = pygame.image.load("images/chicken.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.rect.midleft = self.screen_rect.midleft
        self.rect.right = self.screen_rect.right - 20
        self.speed = self.settings.chicken_speed

    def update(self):
        self.y += self.speed
        if self.y >= 750:
            self.y = 750
            self.speed *= -1
        elif self.y <= 0:
            self.y = 0
            self.speed *= -1
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Babu(Sprite):
    def __init__(self, georgia):
        super().__init__()
        self.screen = georgia.screen
        self.screen_rect = georgia.screen.get_rect()
        self.settings = georgia.settings
        self.image = pygame.image.load("images/babu.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.rect.center = self.screen_rect.center
        self.rect.right = self.screen_rect.right - 100

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Gojo(Sprite):
    def __init__(self, georgia):
        super().__init__()
        self.screen = georgia.screen
        self.screen_rect = georgia.screen.get_rect()
        self.settings = georgia.settings
        self.image = pygame.image.load("images/gojo.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.rect.center = self.screen_rect.center
        self.rect.top = self.screen_rect.top + 300

    def blitme(self):
        self.screen.blit(self.image, self.rect)