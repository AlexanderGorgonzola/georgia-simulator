import pygame.font
import pygame

class Text:
    def __init__(self, georgia):
        self.screen = georgia.screen
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont("lucidaconsole", 40)
        self.font_2 = pygame.font.SysFont("lucidaconsole", 55)
        self.font_3 = pygame.font.SysFont("lucidaconsole", 35)
        self.text_color = (255,255,255)
        self.text = self.font.render("", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.task_1("HI")
        self.item_1("LOSER")

    def goat(self):
        self.text = self.font.render("You: STUPID GOAT", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom
    def cat(self):
        self.text = self.font.render("You: LET ME PET YOU JONAH", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom
    def dog(self):
        self.text = self.font.render("You: SWIM WITH ME MAXI", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom
    def chicken(self):
        self.text = self.font.render("Chicken: (screams)", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom
    def babu(self, talk):
        if talk == 0:
            self.text = self.font.render("Babu: Feed Chicken now (seeds aqired)", True, self.text_color)
        elif talk == 1:
            self.text = self.font.render("Babu: Go feed", True, self.text_color)
        elif talk == 2:
            self.text = self.font.render("Babu: Yippie!")

        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom
    def empty(self):
        self.text = self.font.render("", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom

    def head(self, screen):
        if screen == "start":
            self.text_2 = self.font_2.render("Field", True, self.text_color)
        elif screen == "house":
            self.text_2 = self.font_2.render("Main House", True, self.text_color)
        self.text_2_rect = self.text_2.get_rect()
        self.text_2_rect.midtop = self.screen_rect.midtop
    
    def task_1(self, message):
        self.task_one = self.font_3.render(f"1: {message}", True, (0,0,0))
        self.task_one_rect = self.task_one.get_rect()
        self.task_one_rect.center = self.screen_rect.center
        self.task_one_rect.top = self.screen_rect.top + 150

    def item_1(self, message):
        self.item_one = self.font_3.render(f"1: {message}", True, (0,0,0))
        self.item_one_rect = self.item_one.get_rect()
        self.item_one_rect.center = self.screen_rect.center
        self.item_one_rect.top = self.screen_rect.top + 150

    def draw_text(self):
        self.screen.blit(self.text, self.text_rect)
        self.screen.blit(self.text_2, self.text_2_rect)
    def draw_tasks(self):
        self.screen.blit(self.task_one, self.task_one_rect)
    def draw_items(self):
        self.screen.blit(self.item_one, self.item_one_rect)