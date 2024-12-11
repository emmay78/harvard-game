from functools import partial
import pygame
from enum import Enum

PTEXT_FONT = "fonts/Retro Gaming.ttf"

FONT = partial(pygame.font.Font, PTEXT_FONT)


class Color(Enum):
    RED = (255, 51, 102)
    BLACK = (1, 22, 39)
    BLUE = (32, 164, 243)
    LINEN = (241, 234, 226)
    GREEN = (177, 214, 144)
    SEAGREEN = (46, 196, 182)
    GREY = (217, 217, 217)
    YELLOW = (255, 180, 0)


def update_scores(scores, add):
    for k, v in add.items():
        scores[k] += v


def get_keyboard_selection(list, transition_state, num_selections=2):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                if 1 not in list and len(list) < num_selections:
                    list.append(1)
                elif 1 in list:
                    list.remove(1)
                if num_selections == 1:
                    list.clear()
                    list.append(1)
            elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                if 2 not in list and len(list) < num_selections:
                    list.append(2)
                elif 2 in list:
                    list.remove(2)
                if num_selections == 1:
                    list.clear()
                    list.append(2)
            elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                if 3 not in list and len(list) < num_selections:
                    list.append(3)
                elif 3 in list:
                    list.remove(3)
                if num_selections == 1:
                    list.clear()
                    list.append(3)
            elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                if 4 not in list and len(list) < num_selections:
                    list.append(4)
                elif 4 in list:
                    list.remove(4)
                if num_selections == 1:
                    list.clear()
                    list.append(4)
            elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                if 5 not in list and len(list) < num_selections:
                    list.append(5)
                elif 5 in list:
                    list.remove(5)
                if num_selections == 1:
                    list.clear()
                    list.append(5)
            elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                if 6 not in list and len(list) < num_selections:
                    list.append(6)
                elif 6 in list:
                    list.remove(6)
                if num_selections == 1:
                    list.clear()
                    list.append(6)
            elif (
                event.key == pygame.K_RETURN
                or event.key == pygame.K_SPACE
                or event.key == pygame.K_KP_ENTER
            ) and len(list) == num_selections:
                return transition_state


def get_single_keyboard_selection():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                return 1
            elif event.key == pygame.K_2:
                return 2
            elif event.key == pygame.K_3:
                return 3
            elif event.key == pygame.K_4:
                return 4
            elif event.key == pygame.K_5:
                return 5
            elif event.key == pygame.K_6:
                return 6
