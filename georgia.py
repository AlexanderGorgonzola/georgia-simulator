import pygame
import sys
from settings import Settings
from player import Player
from goat import Goat, Dog, Cat
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
        self.text = Text(self)
        self.music = Music(self)

        self.current_screen = 1
        self.goat_audio = pygame.mixer.Sound("sounds/goat_scream.mp3")
        self.dog_audio = pygame.mixer.Sound("sounds/dog_bark.mp3")
        self.cat_audio = pygame.mixer.Sound("sounds/cat sound.mp3")
        self.music.play_audio()
    def run_game(self):
        while True:
            self._check_events()
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
        if self.current_screen == 1:
            self.goat.update()
            self.dog.update()
            self.cat.update()
            goat_thing = self.goat.rect.collidepoint(self.player.x, self.player.y)
            dog_thing = self.dog.rect.collidepoint(self.player.x, self.player.y)
            cat_thing = self.cat.rect.collidepoint(self.player.x, self.player.y)
            if goat_thing:
                self._player_hit_goat()
            if dog_thing:
                self._player_hit_dog()
            if cat_thing:
                self._player_hit_cat()

    def _player_hit_goat(self):
        self.text.goat()
        self.goat_audio.play()
    def _player_hit_dog(self):
        self.text.dog()
        self.dog_audio.play()
    def _player_hit_cat(self):
        self.cat_audio.play()
        self.text.cat()

    def check_edge(self):
        if self.current_screen == 1 and self.player.rect.right >= 1210:
            self.current_screen = 2
            self.player.x = 600
            self.player.y = 400
        if self.current_screen == 2 and self.player.rect.left <= -10:
            self.current_screen = 1
            self.player.x = 600
            self.player.y = 400
    def _update_screen(self):
        self.screen.blit(self.settings.bg_image, (0,0))
        self.player.blitme()
        if self.current_screen == 1:
            self.goat.blitme()
            self.dog.blitme()
            self.cat.blitme()
        self.text.draw_text()
        pygame.display.flip()

if __name__ == "__main__":
    georgia = georgia()
    georgia.run_game()