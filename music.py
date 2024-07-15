import pygame
from pygame import mixer

class Music:
    def __init__(self, georgia):
        pygame.mixer.music.load("sounds/bg_sound.mp3")
        pygame.mixer.music.set_volume(0.5)

    def play_audio(self):
        pygame.mixer.music.play(-1)