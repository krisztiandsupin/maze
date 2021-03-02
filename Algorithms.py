import pygame

import Settings
from Color import Color
from Text import Text
import Functions
from Settings import screen as screen_settings

screen_size = screen_settings.screen_size

algorithm_display = pygame.display.set_mode(screen_size)
#gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Maze')
pygame.init()

text_color = Color.navy
text_color_light = Color.navy_light
text_size = 50


def settings():
    algorithm_display.fill(Color.white)
    text_title = Text((screen_size[0] // 2, int(screen_size[1] * 0.1)), 'Algorithms', int(text_size * 1.5), text_color, text_color_light)
    text_title.show(algorithm_display)

    while True:
        Functions.update_delay(1000)

        Settings.back_to_menu = True
        break
