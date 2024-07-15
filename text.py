import pygame.font
import pygame

class Text:
    def __init__(self, georgia):
        self.screen = georgia.screen
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont("lucidaconsole", 50)
        self.text_color = (255,255,255)
        self.text = self.font.render("", True, self.text_color)
        self.text_rect = self.text.get_rect()

    def goat(self):
        self.text = self.font.render("STUPID GOAT", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.screen_rect.center
    def cat(self):
        self.text = self.font.render("DON'T TOUCH JONAH", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.screen_rect.center
    def dog(self):
        self.text = self.font.render("SWIM WITH ME MAXI", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.screen_rect.center

    def draw_text(self):
        self.screen.blit(self.text, self.text_rect)