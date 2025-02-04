import pygame
import sys
from settings import Settings
from player import Player, Car
from goat import Goat, Dog, Cat, Chicken, Babu, Gojo, Dad
from music import Music
from text import Text
from buttons import Buttons, Effect
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
        self.gojo = Gojo(self)
        self.dad = Dad(self)
        self.text = Text(self)
        self.music = Music(self)
        self.button = Buttons(self)
        self.effect = Effect(self)
        self.car = Car(self)

        self.current_screen = "start"
        self.hit = False #check whether player is talking or not
        self.task = False
        self.items = False
        self.map = False
        self.chicken_gone = False
        #this is used to track what part of speech each character is on#
        self.babu_talk = 0
        self.goat_talk = 0
        self.cat_talk = 0
        self.gojo_talk = 0
        self.dog_talk = 0
        self.dad_talk = 0
        self.car_talk = 0
        ##
        self.turn = "" #The real purpose of this vairable is for future debugging. Thats it :)
        self.tasks_left = ["feed goat", "feed cat"]
        self.items_left = []
        self.goat_audio = pygame.mixer.Sound("sounds/goat_scream.mp3")
        self.dog_audio = pygame.mixer.Sound("sounds/dog_bark.mp3")
        self.cat_audio = pygame.mixer.Sound("sounds/cat sound.mp3")
        self.chicken_audio = pygame.mixer.Sound("sounds/chicken_scream.mp3")
        self.game_won = False
        self.music.play_audio()
    def run_game(self):
        while True:
            if not self.game_won:
                self._check_events()
                if not self.hit and not self.task and not self.items and not self.map:
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_buttons(mouse_pos)

    def check_keydown(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_RIGHT:
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
                if self.turn == "babu" and self.babu_talk == 0:
                    self.babu_talk = 1
                    self.tasks_left.append("feed chikin")
                    self.items_left.append("seed")
                elif self.turn == "babu" and self.babu_talk == 2:
                    self.items_left.append("cheese")
                    self.babu_talk = 3

                self.turn = ""
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
    def _check_buttons(self, mouse_pos):
        task_button = self.button.task_rect.collidepoint(mouse_pos)
        item_button = self.button.storage_rect.collidepoint(mouse_pos)
        map_button = self.button.map_rect.collidepoint(mouse_pos)
        if task_button and not self.task:
            self.task = True
        elif task_button and self.task:
            self.task = False
        if item_button and not self.items:
            self.items = True
        elif item_button and self.items:
            self.items = False
        if map_button and not self.map:
            self.map = True
        elif map_button and self.map:
            self.map = False

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
        babu_thing = self.babu.rect.collidepoint(self.player.rect.x, self.player.rect.y)
        gojo_thing = self.gojo.rect.collidepoint(self.player.rect.x, self.player.rect.y)
        dad_thing = self.dad.rect.collidepoint(self.player.rect.x, self.player.rect.y)
        car_thing = self.car.rect.collidepoint(self.player.rect.x, self.player.rect.y)
        if self.current_screen == "start" and event == "space":
            if goat_thing:
                self._player_hit_goat()
                self.hit = True
                self.turn = "goat"
            if dog_thing:
                self._player_hit_dog()
                self.hit = True
                self.turn = "dog"
            if cat_thing:
                self._player_hit_cat()
                self.hit = True
                self.turn = "cat"
        if self.current_screen == "house" and event == "space":
            if not self.chicken_gone:
                if chicken_thing:
                    self._player_hit_chicken()
                    self.hit = True
                    self.turn = "chicken"
            if babu_thing:
                self._player_hit_babu()
                self.hit = True
                self.turn = "babu"
        if self.current_screen == "house_2" and event == "space":
            if gojo_thing:
                self._player_hit_gojo()
                self.hit = True
                self.turn = "gojo"
        if self.current_screen == "start_2" and event == "space":
            if dad_thing:
                self._player_hit_dad()
                self.hit = True
                self.turn = "dad"
        if self.current_screen == "parking" and event == "space":
            if car_thing:
                self._player_hit_car()
                self.hit = True
                self.turn = "car"

    def _player_hit_goat(self):
        if "cheese" in self.items_left:
            self.goat_talk = 1
            if self.items_left.index("cheese") == 0:
                self.text.item_1("NONE")
            elif self.items_left.index("cheese") == 1:
                self.text.item_2("NONE")
            elif self.items_left.index("cheese") == 2:
                self.text.item_3("NONE")
            elif self.items_left.index("cheese") == 3:
                self.text.item_4("NONE")

            if self.tasks_left.index("feed goat") == 0:
                self.text.task_2("NONE")
            elif self.tasks_left.index("feed goat") == 1:
                self.text.task_2("NONE")
            elif self.tasks_left.index("feed goat") == 2:
                self.text.task_3("NONE")
            elif self.tasks_left.index("feed goat") == 3:
                self.text.task_4("NONE")
                
            del self.items_left[self.items_left.index("cheese")]
            del self.tasks_left[self.tasks_left.index("feed goat")]
            self.items_left.append("milk")
            if self.items_left.index("milk") == 0:
                self.text.item_1("milk")
            elif self.items_left.index("milk") == 1:
                self.text.item_2("milk")
            elif self.items_left.index("milk") == 2:
                self.text.item_3("milk")
            elif self.items_left.index("milk") == 3:
                self.text.item_4("milk")
        else:
            if self.goat_talk == 1:
                self.goat_talk = 2
        self.text.goat(self.goat_talk)
        self.goat_audio.play()
    def _player_hit_dad(self):
        ######################################################################## final thing
        if self.goat_talk >= 1 and self.babu_talk >= 2 and self.cat_talk >= 1 and self.dog_talk >= 1 and self.gojo_talk >= 1 and self.dad_talk == 0:
            self.dad_talk = 1
            self.items_left.append("car key")
            self.text.item_1("car key")
        else:
            if self.dad_talk == 1:
                self.dad_talk = 2
        self.text.dad(self.dad_talk)
    def _player_hit_dog(self):
        if "bone" in self.items_left:
            self.dog_talk = 1
            if self.items_left.index("bone") == 0:
                self.text.item_1("NONE")
            elif self.items_left.index("bone") == 1:
                self.text.item_2("NONE")
            elif self.items_left.index("bone") == 2:
                self.text.item_3("NONE")
            elif self.items_left.index("bone") == 3:
                self.text.item_4("NONE")
            del self.items_left[self.items_left.index("bone")]
        else:
            if self.dog_talk == 1:
                self.dog_talk = 2
        self.text.dog(self.dog_talk)
        self.dog_audio.play()
    def _player_hit_cat(self):
        if "milk" in self.items_left:
            self.cat_talk = 1
            if self.items_left.index("milk") == 0:
                self.text.item_1("NONE")
            elif self.items_left.index("milk") == 1:
                self.text.item_2("NONE")
            elif self.items_left.index("milk") == 2:
                self.text.item_3("NONE")
            elif self.items_left.index("milk") == 3:
                self.text.item_4("NONE")
            
            if self.tasks_left.index("feed cat") == 0:
                self.text.task_1("NONE")
            elif self.tasks_left.index("feed cat") == 1:
                self.text.task_2("NONE")
            elif self.tasks_left.index("feed cat") == 2:
                self.text.task_3("NONE")
            elif self.tasks_left.index("feed cat") == 3:
                self.text.task_4("NONE")
            
            del self.items_left[self.items_left.index("milk")]
            del self.tasks_left[self.tasks_left.index("feed cat")]
            self.items_left.append("purple")
            if self.items_left.index("purple") == 0:
                self.text.item_1("purple")
            elif self.items_left.index("purple") == 1:
                self.text.item_2("purple")
            elif self.items_left.index("purple") == 2:
                self.text.item_3("purple")
            elif self.items_left.index("purple") == 3:
                self.text.item_4("purple")
        else:
            if self.cat_talk == 1:
                self.cat_talk = 2
        self.cat_audio.play()
        self.text.cat(self.cat_talk)
    def _player_hit_chicken(self):
        self.text.chicken()
        if self.babu_talk == 1:
            self.babu_talk = 2
            if self.tasks_left.index("feed chikin") == 0:
                self.text.task_1("NONE")
            elif self.tasks_left.index("feed chikin") == 1:
                self.text.task_2("NONE")
            if self.tasks_left.index("feed chikin") == 2:
                self.text.task_3("NONE")
            elif self.tasks_left.index("feed chikin") == 3:
                self.text.task_4("NONE")

            if self.items_left.index("seed") == 0:
                self.text.item_1("NONE")
            elif self.items_left.index("seed") == 1:
                self.text.item_2("NONE")
            if self.items_left.index("seed") == 2:
                self.text.item_3("NONE")
            elif self.items_left.index("seed") == 3:
                self.text.item_4("NONE")
                
            del self.tasks_left[self.tasks_left.index("feed chikin")]
            del self.items_left[self.items_left.index("seed")]
            self.chicken_gone = True
        self.chicken_audio.play()
    def _player_hit_babu(self):
        self.text.babu(self.babu_talk)
    def _player_hit_car(self):
        if "car key" in self.items_left:
            self.car_talk = 1
            self.game_won = True
            self.current_screen = "victory"
        self.text.car(self.car_talk)
    def _player_hit_gojo(self):
        self.text.gojo(self.gojo_talk)
        if "purple" in self.items_left and "give ? gojo" in self.tasks_left:
            self.gojo_talk = 1
            if self.items_left.index("purple") == 0:
                self.text.item_1("NONE")
            elif self.items_left.index("purple") == 1:
                self.text.item_2("NONE")
            elif self.items_left.index("purple") == 2:
                self.text.item_3("NONE")
            elif self.items_left.index("purple") == 3:
                self.text.item_4("NONE")
            
            if self.tasks_left.index("give ? gojo") == 0:
                self.text.task_1("NONE")
                self.text.task_3("NONE")
            elif self.tasks_left.index("give ? gojo") == 1:
                self.text.task_2("NONE")
            elif self.tasks_left.index("give ? gojo") == 2:
                self.text.task_3("NONE")
            elif self.tasks_left.index("give ? gojo") == 3:
                self.text.task_4("NONE")
            
            del self.items_left[self.items_left.index("purple")]
            del self.tasks_left[self.tasks_left.index("give ? gojo")]
            self.items_left.append("bone")
            if self.items_left.index("bone") == 0:
                self.text.item_1("bone")
            elif self.items_left.index("bone") == 1:
                self.text.item_2("bone")
            elif self.items_left.index("bone") == 2:
                self.text.item_3("bone")
            elif self.items_left.index("bone") == 3:
                self.text.item_4("bone")
        else:
            if self.gojo_talk == 1:
                self.gojo_talk = 2
            elif self.gojo_talk == 0 and "give ? gojo" not in self.tasks_left:
                self.tasks_left.append("give ? gojo")
                if self.tasks_left.index("give ? gojo") == 0:
                    self.text.task_1("give ? gojo")
                elif self.tasks_left.index("give ? gojo") == 1:
                    self.text.task_2("give ? gojo")
                elif self.tasks_left.index("give ? gojo") == 2:
                    self.text.task_3("give ? gojo")
                elif self.tasks_left.index("give ? gojo") == 3:
                    self.text.task_4("give ? gojo")

    def check_edge(self):
        if self.current_screen == "start" and self.player.rect.right >= 1210:
            self.current_screen = "house"
            self.player.x = 600
            self.player.y = 400
        elif self.current_screen == "start" and self.player.rect.top <= -10:
            self.current_screen = "start_2"
            self.player.x = 600
            self.player.y = 400
        elif self.current_screen == "start_2" and self.player.rect.bottom >= 810:
            self.current_screen = "start"
            self.player.x = 600
            self.player.y = 400
        elif self.current_screen == "house" and self.player.rect.left <= -10:
            self.current_screen = "start"
            self.player.x = 600
            self.player.y = 400
        elif self.current_screen == "house" and self.player.rect.top <= -10:
            self.current_screen = "house_2"
            self.player.x = 600
            self.player.y = 400
        elif self.current_screen == "house_2" and self.player.rect.bottom >= 810:
            self.current_screen = "house"
            self.player.x = 600
            self.player.y = 400
        elif self.current_screen == "start" and self.player.rect.left <= -10:
            self.current_screen = "parking"
            self.player.x = 600
            self.player.y = 400
        elif self.current_screen == "parking" and self.player.rect.right >= 1210:
            self.current_screen = "start"
            self.player.x = 600
            self.player.y = 400
    def _update_screen(self):
        if not self.game_won:
            if self.current_screen == "start" or self.current_screen == "start_2":
                self.screen.blit(self.settings.main_image, (0,0))
            elif self.current_screen == "house" or self.current_screen == "house_2":
                self.screen.blit(self.settings.house_image, (0,0))
            elif self.current_screen == "parking":
                self.screen.blit(self.settings.parking_image, (0,0))

            if self.current_screen == "start":
                self.goat.blitme()
                self.dog.blitme()
                self.cat.blitme()
            elif self.current_screen == "start_2":
                self.dad.blitme()
            elif self.current_screen == "house":
                if not self.chicken_gone:
                    self.chicken.blitme()
                self.babu.blitme()
            elif self.current_screen == "house_2":
                self.gojo.blitme()
            elif self.current_screen == "parking":
                self.car.blitme()
            self.player.blitme()
            self.text.head(self.current_screen)
            self.button.show_buttons()
            self.text.draw_text()
            if self.task:
                self.effect.draw_effect()
                if len(self.tasks_left) > 0:
                    if "feed chikin" in self.tasks_left:
                        if self.tasks_left.index("feed chikin") == 0:
                            self.text.task_1(self.tasks_left[0])
                        if self.tasks_left.index("feed chikin") == 1:
                            self.text.task_2(self.tasks_left[1])
                        if self.tasks_left.index("feed chikin") == 2:
                            self.text.task_3(self.tasks_left[2])
                        if self.tasks_left.index("feed chikin") == 3:
                            self.text.task_4(self.tasks_left[3])
                self.text.draw_tasks()
            if self.items:
                self.effect.draw_item()
                if len(self.items_left) > 0:
                    if "seed" in self.items_left:
                        if self.items_left.index("seed") == 0:
                            self.text.item_1(self.items_left[0])
                        elif self.items_left.index("seed") == 1:
                            self.text.item_2(self.items_left[1])
                        elif self.items_left.index("seed") == 2:
                            self.text.item_3(self.items_left[2])
                        elif self.items_left.index("seed") == 3:
                            self.text.item_4(self.items_left[3])

                    if "cheese" in self.items_left:
                        if self.items_left.index("cheese") == 0:
                            self.text.item_1(self.items_left[0])
                        elif self.items_left.index("cheese") == 1:
                            self.text.item_2(self.items_left[1])
                        elif self.items_left.index("cheese") == 2:
                            self.text.item_3(self.items_left[2])
                        elif self.items_left.index("cheese") == 3:
                            self.text.item_4(self.items_left[3])
                self.text.draw_items()
            if self.map:
                self.effect.draw_map()
            if self.player.rect.right >= 1100 and self.current_screen == "start":
                self.text.leaving("field right")
            elif self.player.rect.left <= 100 and self.current_screen == "house":
                self.text.leaving("main house left")
            elif self.player.rect.top <= 100 and self.current_screen == "house":
                self.text.leaving("main house up")
            elif self.player.rect.bottom >= 790 and self.current_screen == "house_2":
                self.text.leaving("main house_2 down")
            elif self.player.rect.left <= 100 and self.current_screen == "start":
                self.text.leaving("field left")
            elif self.player.rect.right >= 1100 and self.current_screen == "parking":
                self.text.leaving("parking right")
            elif self.player.rect.top <= 100 and self.current_screen == "start":
                self.text.leaving("start top")
            elif self.player.rect.bottom >= 790 and self.current_screen == "start_2":
                self.text.leaving("start_2 bottom")
            else:
                self.text.leaving("")
            self.text.draw_leaving()
        else:
            self.screen.blit(self.settings.victory_image, (0,0))
        pygame.display.flip()

if __name__ == "__main__":
    georgia = georgia()
    georgia.run_game()