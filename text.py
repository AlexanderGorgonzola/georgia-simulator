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
        self.task_1("feed goat")
        self.task_2("feed cat")
        self.task_3("NONE")
        self.task_4("NONE")

        self.item_1("NONE")
        self.item_2("NONE")
        self.item_3("NONE")
        self.item_4("NONE")
        self.leaving("")

    def goat(self, turn):
        if turn == 0:
            self.text = self.font.render("You: NO CHEESE FOR YOU", True, self.text_color)
        elif turn == 1:
            self.text = self.font.render("You: CHEESE FOR YOU (milk aquired)", True, self.text_color)
        elif turn == 2:
            self.text = self.font.render("You: STUPID GOAT", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom
    def cat(self, turn):
        if turn == 0:
            self.text = self.font.render("Jonah: GIVE MILK NOW", True, self.text_color)
        elif turn == 1:
            self.text = self.font.render("You: HERE MILK (purple aquired)", True, self.text_color)
        elif turn == 2:
            self.text = self.font.render("You: LET ME PET YOU JONAH", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom
    def dog(self, turn):
        if turn == 0:
            self.text = self.font.render("Maxi: BONE NOW", True, self.text_color)
        elif turn == 1:
            self.text = self.font.render("You: HERE BONE", True, self.text_color)
        elif turn == 2:
            self.text = self.font.render("You: SWIM WITH ME MAXI", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom
    def chicken(self):
        self.text = self.font.render("Chicken: (screams)", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom
    def babu(self, talk):
        if talk == 0:
            self.text = self.font.render("Old Man: Feed Chicken now (seeds aqired)", True, self.text_color)
        elif talk == 1:
            self.text = self.font.render("Old Man: Go feed", True, self.text_color)
        elif talk == 2:
            self.text = self.font.render("Old Man: Yippie! (cheese aqurid)", True, self.text_color)
        elif talk == 3:
            self.text = self.font.render("Old Man: Yippie!", True, self.text_color)

        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom
    def gojo(self, turn):
        if turn == 0:
            self.text = self.font.render("Go/Jo: I need purple soap", True, self.text_color)
        elif turn == 1:
            self.text = self.font.render("You: HERE PURPLE (bone aquired)", True, self.text_color)
        elif turn == 2:
            self.text = self.font.render("Go/Jo: Got any stiches?", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom
    def dad(self, turn):
        if turn == 0:
            self.text = self.font.render("Dad: I will give keys soon", True, self.text_color)
        elif turn == 1:
            self.text = self.font.render("You: GIVE KEYS (keys aquireddddddd)", True, self.text_color)
        elif turn == 2:
            self.text = self.font.render("Dad: Go drive car now", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom
    def car(self, turn):
        if turn == 0:
            self.text = self.font.render("Car: I need keys to leave", True, self.text_color)
        elif turn == 1:
            self.text = self.font.render("You: LET ME LEAVE CAR", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom
    def empty(self):
        self.text = self.font.render("", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom

    def head(self, screen):
        if screen == "start" or screen == "start_2":
            self.text_2 = self.font_2.render("Field", True, self.text_color)
        elif screen == "house" or screen == "house_2":
            self.text_2 = self.font_2.render("Main House", True, self.text_color)
        elif screen == "parking":
            self.text_2 = self.font_2.render("Parking", True, self.text_color)
        self.text_2_rect = self.text_2.get_rect()
        self.text_2_rect.midtop = self.screen_rect.midtop
    
    def task_1(self, message):
        self.task_one = self.font_3.render(f"1: {message}", True, (0,0,0))
        self.task_one_rect = self.task_one.get_rect()
        self.task_one_rect.center = self.screen_rect.center
        self.task_one_rect.top = self.screen_rect.top + 150
    def task_2(self, message):
        self.task_two = self.font_3.render(f"2: {message}", True, (0,0,0))
        self.task_two_rect = self.task_two.get_rect()
        self.task_two_rect.center = self.screen_rect.center
        self.task_two_rect.top = self.screen_rect.top + 200
    def task_3(self, message):
        self.task_three = self.font_3.render(f"3: {message}", True, (0,0,0))
        self.task_three_rect = self.task_one.get_rect()
        self.task_three_rect.center = self.screen_rect.center
        self.task_three_rect.top = self.screen_rect.top + 250
    def task_4(self, message):
        self.task_four = self.font_3.render(f"4: {message}", True, (0,0,0))
        self.task_four_rect = self.task_four.get_rect()
        self.task_four_rect.center = self.screen_rect.center
        self.task_four_rect.top = self.screen_rect.top + 300

    def item_1(self, message):
        self.item_one = self.font_3.render(f"1: {message}", True, (0,0,0))
        self.item_one_rect = self.item_one.get_rect()
        self.item_one_rect.center = self.screen_rect.center
        self.item_one_rect.top = self.screen_rect.top + 150
    def item_2(self, message):
        self.item_two = self.font_3.render(f"2: {message}", True, (0,0,0))
        self.item_two_rect = self.item_two.get_rect()
        self.item_two_rect.center = self.screen_rect.center
        self.item_two_rect.top = self.screen_rect.top + 200
    def item_3(self, message):
        self.item_three = self.font_3.render(f"3: {message}", True, (0,0,0))
        self.item_three_rect = self.item_three.get_rect()
        self.item_three_rect.center = self.screen_rect.center
        self.item_three_rect.top = self.screen_rect.top + 250
    def item_4(self, message):
        self.item_four = self.font_3.render(f"4: {message}", True, (0,0,0))
        self.item_four_rect = self.item_four.get_rect()
        self.item_four_rect.center = self.screen_rect.center
        self.item_four_rect.top = self.screen_rect.top + 300

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
        elif message == "main house_2 down":
            self.leave = self.font_2.render("v House", True, self.text_color)
            self.leave_rect = self.leave.get_rect()
            self.leave_rect.midbottom = self.screen_rect.midbottom
        elif message == "field right":
            self.leave = self.font_2.render("House -->", True, self.text_color)
            self.leave_rect = self.leave.get_rect()
            self.leave_rect.midright = self.screen_rect.midright
        elif message == "field left":
            self.leave = self.font_2.render("<-- parking", True, self.text_color)
            self.leave_rect = self.leave.get_rect()
            self.leave_rect.midleft = self.screen_rect.midleft
        elif message == "parking right":
            self.leave = self.font_2.render("field -->", True, self.text_color)
            self.leave_rect = self.leave.get_rect()
            self.leave_rect.midright = self.screen_rect.midright
        elif message == "start top":
            self.leave = self.font_2.render("^ Field", True, self.text_color)
            self.leave_rect = self.leave.get_rect()
            self.leave_rect.midtop = self.screen_rect.midtop
            self.leave_rect.left = self.screen_rect.left + 100
        elif message == "start_2 bottom":
            self.leave = self.font_2.render("v Field", True, self.text_color)
            self.leave_rect = self.leave.get_rect()
            self.leave_rect.midbottom = self.screen_rect.midbottom
        elif message == "":
            self.leave = self.font_2.render("", True, self.text_color)
            self.leave_rect = self.leave.get_rect()
            
        

    def draw_text(self):
        self.screen.blit(self.text, self.text_rect)
        self.screen.blit(self.text_2, self.text_2_rect)
    def draw_tasks(self):
        self.screen.blit(self.task_one, self.task_one_rect)
        self.screen.blit(self.task_two, self.task_two_rect)
        self.screen.blit(self.task_three, self.task_three_rect)
        self.screen.blit(self.task_four, self.task_four_rect)
    def draw_items(self):
        self.screen.blit(self.item_one, self.item_one_rect)
        self.screen.blit(self.item_two, self.item_two_rect)
        self.screen.blit(self.item_three, self.item_three_rect)
        self.screen.blit(self.item_four, self.item_four_rect)
    def draw_leaving(self):
        self.screen.blit(self.leave, self.leave_rect)