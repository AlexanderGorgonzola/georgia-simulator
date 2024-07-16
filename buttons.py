import pygame
import pygame.font

class Buttons:
    def __init__(self, georgia):
        self.screen = georgia.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = georgia.settings
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont("lucidaconsole", 45)
        self.prep_task()
        self.prep_storage()

    def prep_task(self):
        self.task = pygame.image.load("images/task_button.png")
        self.task_rect = self.task.get_rect()
        self.task_rect.left = self.screen_rect.left + 30
        self.task_rect.bottom = self.screen_rect.bottom - 30
    def prep_storage(self):
        self.storage = pygame.image.load("images/storage_button.png")
        self.storage_rect = self.storage.get_rect()
        self.storage_rect.left = self.screen_rect.left + 30
        self.storage_rect.bottom = self.screen_rect.bottom - 140
    def show_buttons(self):
        self.screen.blit(self.task, self.task_rect)
        self.screen.blit(self.storage, self.storage_rect)

class Effect:
    def __init__(self, georgia):
        self.settings = georgia.settings
        self.screen = georgia.screen
        self.screen_rect = self.screen.get_rect()
        self.prep_task()
        self.prep_item()
        
    def prep_task(self):
        self.task = pygame.image.load("images/tasks.png")
        self.task_rect = self.task.get_rect()
        self.task_rect.center = self.screen_rect.center
    def prep_item(self):
        self.item = pygame.image.load("images/items.png")
        self.item_rect = self.item.get_rect()
        self.item_rect.center = self.screen_rect.center
    
    def draw_effect(self):
        self.screen.blit(self.task, self.task_rect)
    def draw_item(self):
        self.screen.blit(self.item, self.item_rect)