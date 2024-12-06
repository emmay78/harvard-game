import os
import pygame
from enum import Enum
from graphics import *
from constants import *


class GameState(Enum):
    INIT_0 = 1
    INIT_1 = 2
    INIT_2 = 3
    PLAY = 4
    COURSES = 5
    STATUS = 6


category_scores = {
    "school": 0,
    "fun": 0,
    "clubs": 0,
    "rest": 0,
}

phil_scores = {
    "mengzi": 0,
    "xunzi": 0,
    "zhuangzi": 0,
    "shangyang": 0,
    "laozi": 0,
}


os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()
window = pygame.display.set_mode((908, 712))
pygame.display.set_caption("The Harvard Game")
clock = pygame.time.Clock()

running = True
current_state = GameState.INIT_0
week = 1
day = "MONDAY"

course_selection = []

colors = [(0, 0, 255), (169, 221, 214), (122, 139, 153), (145, 173, 194)]
color = colors[0]
while running:
    window.fill(Color.LINEN.value)
    if current_state == GameState.INIT_0:
        draw_title(window)
        draw_init_text_1(window)
        draw_next_button(window)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    current_state = GameState.INIT_1
    elif current_state == GameState.INIT_1:
        draw_title(window)
        draw_init_text_2(window)
        draw_next_button(window)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    current_state = GameState.INIT_2
    elif current_state == GameState.INIT_2:
        draw_title(window)
        draw_init_text_3(window)
        draw_interesting_button(window)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    current_state = GameState.COURSES
    elif current_state == GameState.COURSES:
        draw_top_scoreboard(window, category_scores)
        draw_time_counter(window, week, day)
        draw_bottom_scoreboard(window, phil_scores)
        if week == 1:
            draw_course_selection(window, course_selection)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        if 1 not in course_selection and len(course_selection) < 4:
                            course_selection.append(1)
                        elif 1 in course_selection:
                            course_selection.remove(1)
                    elif event.key == pygame.K_2:
                        if 2 not in course_selection and len(course_selection) < 4:
                            course_selection.append(2)
                        elif 2 in course_selection:
                            course_selection.remove(2)
                    elif event.key == pygame.K_3:
                        if 3 not in course_selection and len(course_selection) < 4:
                            course_selection.append(3)
                        elif 3 in course_selection:
                            course_selection.remove(3)
                    elif event.key == pygame.K_4:
                        if 4 not in course_selection and len(course_selection) < 4:
                            course_selection.append(4)
                        elif 4 in course_selection:
                            course_selection.remove(4)
                    elif event.key == pygame.K_5:
                        if 5 not in course_selection and len(course_selection) < 4:
                            course_selection.append(5)
                        elif 5 in course_selection:
                            course_selection.remove(5)
                    elif event.key == pygame.K_6:
                        if 6 not in course_selection and len(course_selection) < 4:
                            course_selection.append(6)
                        elif 6 in course_selection:
                            course_selection.remove(6)
                    elif event.key == pygame.K_RETURN:
                        current_state = GameState.PLAY
    elif current_state == GameState.PLAY:
        draw_top_scoreboard(window, category_scores)
        draw_time_counter(window, week, day)
        draw_bottom_scoreboard(window, phil_scores)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
