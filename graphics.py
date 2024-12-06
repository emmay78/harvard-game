import pygame
from functools import partial
from constants import *
import ptext

# INIT SCREENS


def draw_title(window):
    """
    Draws the Welcome title of the game.
    """
    font = FONT(36)
    text = font.render("WELCOME TO THE HARVARD GAME", True, Color.BLACK.value)

    box = pygame.draw.rect(window, Color.RED.value, (120, 61, 669, 88))
    window.blit(text, text.get_rect(center=box.center))


def draw_init_text_1(window):
    text = """Congratulations! You’ve been admitted to Harvard College. A transformative year-long experience awaits you."""
    ptext.drawbox(
        text,
        (75, 220, 766, 253),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )


def draw_init_text_2(window):
    text = """You've moved into your dorm: a double overlooking Harvard Yard. Your suitemates seem nice, and you hope they’ll become good friends. You’re looking forward to starting classes, joining clubs, and exploring the social scene, all while maintaining a healthy school-life balance."""
    ptext.drawbox(
        "SEVERAL  MONTHS LATER...",
        (116, 200, 674, 50),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )
    ptext.drawbox(
        text,
        (68, 279, 771, 216),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )


def draw_init_text_3(window):
    text = """...you can’t help but feel like your forthcoming decisions are being watched over closely by spirits from the ancient past..."""

    ptext.drawbox(
        text,
        (72, 300, 763, 131),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )


def draw_next_button(window):
    font = FONT(30)
    text = font.render("GREAT NEWS! LET'S GO!", True, Color.BLACK.value)

    box = pygame.draw.rect(
        window, Color.SEAGREEN.value, (165, 543, 579, 58), border_radius=40
    )
    window.blit(text, text.get_rect(center=box.center))

    ptext.drawbox(
        "PRESS ENTER TO CONTINUE",
        (186, 616, 523, 22),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )


def draw_interesting_button(window):
    font = FONT(30)
    text = font.render("HM, INTERESTING...", True, Color.BLACK.value)

    box = pygame.draw.rect(
        window, Color.SEAGREEN.value, (165, 543, 579, 58), border_radius=40
    )
    window.blit(text, text.get_rect(center=box.center))

    ptext.drawbox(
        "PRESS ENTER TO CONTINUE",
        (186, 616, 523, 22),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )


# INFO BOARDS


def draw_top_scoreboard(window, scores):
    # Bounding box
    pygame.draw.rect(window, Color.RED.value, (0, 0, 908, 62))

    # Scores
    ptext.drawbox(
        f"SCHOOL\t{scores['school']}",
        (21, 15, 250, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )
    ptext.drawbox(
        f"FUN\t{scores['fun']}",
        (241, 15, 250, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )
    ptext.drawbox(
        f"CLUBS\t{scores['clubs']}",
        (456, 15, 250, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )
    ptext.drawbox(
        f"REST\t{scores['rest']}",
        (673, 15, 250, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )


def draw_bottom_scoreboard(window, scores):
    # Bounding box
    pygame.draw.rect(window, Color.BLUE.value, (0, 637, 908, 75))

    # Scores
    ptext.drawbox(
        f"MENGZI\t{scores['mengzi']}",
        (30, 660, 150, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )

    ptext.drawbox(
        f"XUNZI\t{scores['xunzi']}",
        (180, 660, 182, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )

    ptext.drawbox(
        f"ZHUANGZI\t{scores['zhuangzi']}",
        (360, 660, 182, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )

    ptext.drawbox(
        f"SHANG YANG\t{scores['shangyang']}",
        (555, 660, 182, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )

    ptext.drawbox(
        f"LAOZI\t{scores['laozi']}",
        (730, 660, 182, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )


def draw_time_counter(window, week, day):
    ptext.drawbox(
        f"WEEK: {week}",
        (7, 76, 141, 35),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_BOLD_FONT,
    )

    ptext.drawbox(
        f"DAY: {day}",
        (700, 76, 189, 35),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_BOLD_FONT,
    )


def draw_course_selection(window, selection):
    def draw_button(x, y, idx, course):
        box = pygame.draw.rect(
            window, Color.GREEN.value, (x, y, 397, 71), border_radius=40
        )
        ptext.drawbox(
            course,
            (x + 99, y + 13, 260, 38),
            align="center",
            color=Color.BLACK.value,
            fontname=PTEXT_FONT,
        )
        num_box = pygame.draw.rect(
            window,
            Color.GREY.value if idx not in selection else Color.RED.value,
            (x + 29, y + 17, 32, 32),
        )
        ptext.drawbox(
            str(idx),
            (x + 29, y + 17, 32, 32),
            align="center",
            color=Color.BLACK.value,
            fontname=PTEXT_BOLD_FONT,
        )

    coordinates = [
        (30, 280),
        (30, 374),
        (30, 468),
        (483, 277),
        (483, 371),
        (483, 465),
    ]

    for idx, (course, (x, y)) in enumerate(zip(courses, coordinates)):
        draw_button(x, y, idx + 1, course)

    select_class = """You need to select your classes for the semester. Which classes will you take? Select 4 from the following. None have any prerequisites."""
    ptext.drawbox(
        select_class,
        (26, 127, 849, 100),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )
    select_class_2 = """USE THE KEYBOARD TO SELECT YOUR CHOICE"""
    ptext.drawbox(
        select_class_2,
        (204, 238, 500, 17),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )

    pygame.draw.rect(
        window, Color.SEAGREEN.value, (309, 564, 292, 44), border_radius=40
    )
    ptext.drawbox(
        "ENROLL",
        (323, 570, 263, 31),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )
    ptext.drawbox(
        "PRESS ENTER",
        (604, 577, 163, 17),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )
