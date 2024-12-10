import os
import json
import pygame
import random
from enum import Enum
from graphics import *
from constants import *


class GameState(Enum):
    INIT_0 = 1
    INIT_1 = 2
    INIT_2 = 3
    INIT_3 = 7
    PLAY = 4
    COURSES = 5
    STATUS = 6
    END = 8


category_scores = {
    "school": 0,
    "fun": 0,
    "rest": 0,
}

category_warning_count = {
    "school": 0,
    "fun": 0,
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
programIcon = pygame.image.load("icon.png")
pygame.display.set_icon(programIcon)
clock = pygame.time.Clock()

running = True
current_state = GameState.INIT_0
week = 0
day = "SUNDAY"

# Read JSON files
with open("data/courses.json") as f:
    courses = json.load(f)

with open("data/clubs.json") as f:
    clubs = json.load(f)

with open("data/global.json") as f:
    global_options = json.load(f)

with open("data/random.json") as f:
    random_options = json.load(f)

with open("data/warnings.json") as f:
    warnings = json.load(f)

# Game state
current_course_selection = []
current_club_selection = []
current_selection = []
courses_enrolled = False
screen_idx = 0
displaying_warning = False


def reset():
    global category_scores, category_warning_count, phil_scores, current_course_selection
    global current_club_selection, current_selection, courses_enrolled, choice
    global displaying_warning, week, day, current_state

    category_scores = {
        "school": 0,
        "fun": 0,
        "rest": 0,
    }

    category_warning_count = {
        "school": 0,
        "fun": 0,
        "rest": 0,
    }

    phil_scores = {
        "mengzi": 0,
        "xunzi": 0,
        "zhuangzi": 0,
        "shangyang": 0,
        "laozi": 0,
    }

    current_course_selection = []
    current_club_selection = []
    current_selection = []
    courses_enrolled = False
    choice = 0
    displaying_warning = False
    week = 0
    day = "SUNDAY"


while running:
    window.fill(Color.LINEN.value)
    if current_state == GameState.INIT_0:
        draw_title(window)
        draw_init_text_1(window)
        draw_next_button(window)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    current_state = GameState.INIT_1
    elif current_state == GameState.INIT_1:
        draw_title(window)
        draw_init_text_2(window)
        draw_next_button(window)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    current_state = GameState.INIT_2
    elif current_state == GameState.INIT_2:
        draw_title(window)
        draw_init_text_3(window)
        draw_interesting_button(window)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    current_state = GameState.INIT_3
    elif current_state == GameState.INIT_3:
        draw_title(window)
        draw_init_text_4(window)
        draw_next_button(window)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    current_state = GameState.PLAY
    elif current_state == GameState.PLAY:
        draw_top_scoreboard(window, category_scores)
        draw_time_counter(window, week, day)
        draw_bottom_scoreboard(window, phil_scores)
        if week == 0 or week == 8:
            # Join courses and clubs
            day = "SUNDAY"
            if not courses_enrolled:
                options = courses["fall" if week == 0 else "spring"]
                draw_interactive_selection(window, options, current_course_selection)
                done = get_keyboard_selection(current_course_selection, True, 2)
                if done:
                    for idx in current_course_selection:
                        course_scores = options["options"][idx - 1]["scores"]
                        update_scores(phil_scores, course_scores)
                        current_course_selection = []
                        courses_enrolled = True
            else:
                options = clubs["fall" if week == 0 else "spring"]
                draw_interactive_selection(window, options, current_club_selection)
                done = get_keyboard_selection(current_club_selection, True, 1)
                if done:
                    club_scores = options["options"][current_club_selection[0] - 1][
                        "scores"
                    ]
                    update_scores(phil_scores, club_scores)
                    current_club_selection = []
                    courses_enrolled = False
                    week += 1
                    day = "MONDAY"
        elif week <= 16:
            # Global options
            day = "MONDAY"
            if screen_idx <= 1:
                options = global_options[screen_idx]
                draw_interactive_selection(window, options, current_course_selection)
                # Show status if threshold exceeded
                if displaying_warning > 0:
                    warning_key = list(category_scores.keys())[displaying_warning - 1]
                    if (
                        category_scores[warning_key] < 0
                        and category_warning_count[warning_key] == 0
                    ) or (
                        category_scores[warning_key] < -5
                        and category_warning_count[warning_key] == 1
                    ):
                        draw_warning(
                            window,
                            warnings[warning_key][category_warning_count[warning_key]],
                            "GOT IT",
                        )
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if (
                                    event.key == pygame.K_RETURN
                                    or event.key == pygame.K_SPACE
                                ):
                                    category_warning_count[warning_key] += 1
                                    displaying_warning -= 1
                    elif (
                        category_scores[warning_key] <= -10
                        and category_warning_count[warning_key] == 2
                    ):
                        draw_warning(
                            window,
                            warnings[warning_key][category_warning_count[warning_key]],
                            "GAME OVER",
                        )
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if (
                                    event.key == pygame.K_RETURN
                                    or event.key == pygame.K_SPACE
                                ):
                                    current_state = GameState.INIT_0
                                    reset()
                    else:
                        displaying_warning -= 1

                    if displaying_warning == 0:
                        # Transition to the next randomization
                        screen_idx += 1
                        current_course_selection = []
                        random_event = random.choice(random_options)
                else:
                    random_event = random.choice(random_options)
                done = get_keyboard_selection(current_course_selection, True, 1)
                if done:
                    for idx in current_course_selection:
                        for key, score_dict in zip(
                            ["category_scores", "phil_scores"],
                            [category_scores, phil_scores],
                        ):
                            course_scores = options["options"][idx - 1][key]
                            update_scores(score_dict, course_scores)
                    displaying_warning = 3
            else:
                day = random_event["day"]
                draw_interactive_selection(window, random_event, current_selection)
                done = get_keyboard_selection(current_selection, True, 1)
                if done:
                    scores = options["options"][current_selection[0] - 1][key]
                    update_scores(phil_scores, scores)
                    week += 1
                    screen_idx = 0
                    current_selection = []
        else:
            current_state = GameState.END
    elif current_state == GameState.END:
        # End game
        draw_end_game(window, phil_scores=phil_scores, category_scores=category_scores)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    current_state = GameState.INIT_0
                    reset()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
