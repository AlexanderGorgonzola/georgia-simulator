import pygame
import sys
from settings import Settings
from player import Player
from goat import Goat, Dog, Cat, Chicken, Babu
from music import Music
from text import Text
class georgia:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_length))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_length = self.screen.get_rect().height
        pygame.display.set_caption("Georgia Simulator")
        self.player = Player(self)
        self.goat = Goat(self)
        self.dog = Dog(self)
        self.cat = Cat(self)
        self.chicken = Chicken(self)
        self.babu = Babu(self)
        self.text = Text(self)
        self.music = Music(self)

        self.current_screen = "start"
        self.hit = False
        self.goat_audio = pygame.mixer.Sound("sounds/goat_scream.mp3")
        self.dog_audio = pygame.mixer.Sound("sounds/dog_bark.mp3")
        self.cat_audio = pygame.mixer.Sound("sounds/cat sound.mp3")
        self.chicken_audio = pygame.mixer.Sound("sounds/chicken_scream.mp3")
        self.music.play_audio()
    def run_game(self):
        while True:
            self._check_events()
            if not self.hit:
                self._update_animals()
                self.player.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup(event)

    def check_keydown(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.player.moving_right = True
            self.check_edge()
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
            self.check_edge()
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = True
        elif event.key == pygame.K_UP:
            self.player.moving_up = True
        elif event.key == pygame.K_SPACE:
            if self.hit:
                self.hit = False
                self.text.empty()
            else:
                self._check_animals("space")

    def check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False
        elif event.key == pygame.K_UP:
            self.player.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = False
    
    def _update_animals(self):
        if self.current_screen == "start":
            self.goat.update()
            self.dog.update()
            self.cat.update()
        elif self.current_screen == "house":
            self.chicken.update()

    def _check_animals(self, event):
        goat_thing = self.goat.rect.collidepoint(self.player.rect.x, self.player.rect.y)
        dog_thing = self.dog.rect.collidepoint(self.player.rect.x, self.player.rect.y)
        cat_thing = self.cat.rect.collidepoint(self.player.rect.x, self.player.rect.y)
        chicken_thing = self.chicken.rect.collidepoint(self.player.rect.x, self.player.rect.y)
        if self.current_screen == "start" and event == "space":
            if goat_thing:
                self._player_hit_goat()
                self.hit = True
            if dog_thing:
                self._player_hit_dog()
                self.hit = True
            if cat_thing:
                self._player_hit_cat()
                self.hit = True
        if self.current_screen == "house" and event == "space":
            if chicken_thing:
                self._player_hit_chicken()
                self.hit = True

    def _player_hit_goat(self):
        self.text.goat()
        self.goat_audio.play()
    def _player_hit_dog(self):
        self.text.dog()
        self.dog_audio.play()
    def _player_hit_cat(self):
        self.cat_audio.play()
        self.text.cat()
    def _player_hit_chicken(self):
        self.chicken_audio.play()
        self.text.chicken()

    def check_edge(self):
        if self.current_screen == "start" and self.player.rect.right >= 1210:
            self.current_screen = "house"
            self.player.x = 600
            self.player.y = 400
        if self.current_screen == "house" and self.player.rect.left <= -10:
            self.current_screen = "start"
            self.player.x = 600
            self.player.y = 400
    def _update_screen(self):
        if self.current_screen == "start":
            self.screen.blit(self.settings.main_image, (0,0))
        elif self.current_screen == "house":
            self.screen.blit(self.settings.house_image, (0,0))

        if self.current_screen == "start":
            self.goat.blitme()
            self.dog.blitme()
            self.cat.blitme()
        elif self.current_screen == "house":
            self.chicken.blitme()
            self.babu.blitme()
        self.player.blitme()
        self.text.head(self.current_screen)
        self.text.draw_text()
        pygame.display.flip()

if __name__ == "__main__":
    georgia = georgia()
    georgia.run_game()