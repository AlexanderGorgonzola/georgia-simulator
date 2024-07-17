import pygame.font
import pygame

class Text:
    def __init__(self, georgia):
        self.screen = georgia.screen
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont("lucidaconsole", 40)
        self.font_2 = pygame.font.SysFont("lucidaconsole", 55)
        self.font_3 = pygame.font.SysFont("lucidaconsole", 55)
        self.text_color = (255,255,255)
        self.text = self.font.render("", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.task_1("NONE")
        self.task_2("NONE")
        self.item_1("NONE")
        self.item_2("NONE")
        self.leaving("")

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
            self.text = self.font.render("Babu: Yippie!", True, self.text_color)

        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom
    def empty(self):
        self.text = self.font.render("", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom

    def head(self, screen):
        if screen == "start":
            self.text_2 = self.font_2.render("Field", True, self.text_color)
        elif screen == "house" or screen == "house_2":
            self.text_2 = self.font_2.render("Main House", True, self.text_color)
        self.text_2_rect = self.text_2.get_rect()
        self.text_2_rect.midtop = self.screen_rect.midtop
    
    def task_1(self, message):
        self.task_one = self.font_3.render(f"1: {message}", True, (0,0,0))
        self.task_one_rect = self.task_one.get_rect()
        self.task_one_rect.center = self.screen_rect.center
        self.task_one_rect.top = self.screen_rect.top + 150
    def task_2(self, message):
        self.task_two = self.font_3.render(f"2: {message}", True, (0,0,0))
        self.task_two_rect = self.task_one.get_rect()
        self.task_two_rect.center = self.screen_rect.center
        self.task_two_rect.top = self.screen_rect.top + 200

    def item_1(self, message):
        self.item_one = self.font_3.render(f"1: {message}", True, (0,0,0))
        self.item_one_rect = self.item_one.get_rect()
        self.item_one_rect.center = self.screen_rect.center
        self.item_one_rect.top = self.screen_rect.top + 150
    def item_2(self, message):
        self.item_two = self.font_3.render(f"2: {message}", True, (0,0,0))
        self.item_two_rect = self.item_one.get_rect()
        self.item_two_rect.center = self.screen_rect.center
        self.item_two_rect.top = self.screen_rect.top + 200

    def leaving(self, message):
        if message == "main house left":
            self.leave = self.font_2.render("<-- Field", True, self.text_color)
            self.leave_rect = self.leave.get_rect()
            self.leave_rect.midleft = self.screen_rect.midleft
        elif message == "main house up":
            self.leave = self.font_2.render("^ House", True, self.text_color)
            self.leave_rect = self.leave.get_rect()
            self.leave_rect.midtop = self.screen_rect.midtop
            self.leave_rect.left = self.screen_rect.left + 100
        elif message == "field right":
            self.leave = self.font_2.render("House -->", True, self.text_color)
            self.leave_rect = self.leave.get_rect()
            self.leave_rect.midright = self.screen_rect.midright
        elif message == "":
            self.leave = self.font_2.render("", True, self.text_color)
            self.leave_rect = self.leave.get_rect()
            
        

    def draw_text(self):
        self.screen.blit(self.text, self.text_rect)
        self.screen.blit(self.text_2, self.text_2_rect)
    def draw_tasks(self):
        self.screen.blit(self.task_one, self.task_one_rect)
        self.screen.blit(self.task_two, self.task_two_rect)
    def draw_items(self):
        self.screen.blit(self.item_one, self.item_one_rect)
        self.screen.blit(self.item_two, self.item_two_rect)
    def draw_leaving(self):
        self.screen.blit(self.leave, self.leave_rect)