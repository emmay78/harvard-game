import pygame
from functools import partial
from constants import *
import ptext
import json
from typing import Dict, List, Optional

# INIT SCREENS


def draw_title(window: pygame.Surface) -> None:
    """
    Draws the Welcome title of the game.
    """
    font = FONT(32)
    text = font.render("WELCOME TO THE HARVARD GAME", True, Color.BLACK.value)

    box = pygame.draw.rect(window, Color.RED.value, (120, 61, 669, 88))
    window.blit(text, text.get_rect(center=box.center))


def draw_init_text_1(window: pygame.Surface) -> None:
    text = """Congratulations! You've been admitted to Harvard College. A transformative year-long experience awaits you."""
    ptext.drawbox(
        text,
        (75, 220, 766, 253),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )


def draw_init_text_2(window: pygame.Surface) -> None:
    text = """You've moved into your dorm: a double overlooking Harvard Yard. Your suitemates seem nice, and you hope they'll become good friends. You're looking forward to starting classes, joining clubs, and exploring the social scene, all while maintaining a healthy school-life balance."""
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


def draw_init_text_3(window: pygame.Surface) -> None:
    text = """...you can't help but feel like your forthcoming decisions are being watched over closely by spirits from the ancient past..."""

    ptext.drawbox(
        text,
        (72, 300, 763, 131),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )


def draw_init_text_4(window: pygame.Surface) -> None:
    text = """This is a keyboard-based game! Use the numbers on your keyboard to select options. Press ENTER or SPACE to confirm your selection."""

    ptext.drawbox(
        text,
        (72, 300, 763, 131),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )


def draw_next_button(window: pygame.Surface) -> None:
    font = FONT(30)
    text = font.render("GREAT NEWS! LET'S GO!", True, Color.BLACK.value)

    box = pygame.draw.rect(
        window, Color.SEAGREEN.value, (165, 543, 579, 58), border_radius=40
    )
    window.blit(text, text.get_rect(center=box.center))

    ptext.drawbox(
        "PRESS ENTER OR SPACE TO CONTINUE",
        (195, 616, 523, 32),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )


def draw_interesting_button(window: pygame.Surface) -> None:
    font = FONT(30)
    text = font.render("HM, INTERESTING...", True, Color.BLACK.value)

    box = pygame.draw.rect(
        window, Color.SEAGREEN.value, (165, 543, 579, 58), border_radius=40
    )
    window.blit(text, text.get_rect(center=box.center))

    ptext.drawbox(
        "PRESS ENTER OR SPACE TO CONTINUE",
        (195, 616, 523, 32),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )


# INFO BOARDS


def draw_top_scoreboard(window: pygame.Surface, scores: Dict[str, int]) -> None:
    # Bounding box
    pygame.draw.rect(window, Color.RED.value, (0, 0, 908, 62))

    # Scores
    ptext.drawbox(
        f"SCHOOL\t{scores['school']}",
        (80, 15, 250, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )
    ptext.drawbox(
        f"FUN\t{scores['fun']}",
        (335, 15, 250, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )
    ptext.drawbox(
        f"REST\t{scores['rest']}",
        (590, 15, 250, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )


def draw_bottom_scoreboard(window: pygame.Surface, scores: Dict[str, int]) -> None:
    # Bounding box
    pygame.draw.rect(window, Color.BLUE.value, (0, 637, 908, 75))

    # Scores
    ptext.drawbox(
        f"MENGZI\t{scores['mengzi']}",
        (30, 660, 140, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )

    ptext.drawbox(
        f"XUNZI\t{scores['xunzi']}",
        (200, 660, 120, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )

    ptext.drawbox(
        f"ZHUANGZI\t{scores['zhuangzi']}",
        (350, 660, 160, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )

    ptext.drawbox(
        f"LORD SHANG\t{scores['lord shang']}",
        (540, 660, 182, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )

    ptext.drawbox(
        f"LAOZI\t{scores['laozi']}",
        (760, 660, 110, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )


def draw_time_counter(window: pygame.Surface, week: int, day: int) -> None:
    ptext.drawbox(
        f"WEEK: {week}",
        (7, 76, 141, 35),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
        background=Color.YELLOW.value,
    )

    ptext.drawbox(
        f"SEMESTER: {"SPRING" if week > 10 else "FALL"}",
        (321, 76, 270, 35),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )

    ptext.drawbox(
        f"DAY: {day}",
        (700, 76, 189, 35),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
        background=Color.YELLOW.value,
    )


def draw_interactive_selection(
    window: pygame.Surface,
    options: Dict[str, List[Dict[str, str]]],
    selection: Optional[List[int]],
) -> None:
    def draw_button(x: int, y: int, idx: int, object: str) -> None:
        pygame.draw.rect(window, Color.GREEN.value, (x, y, 397, 71), border_radius=40)
        if len(object) < 25:
            ptext.draw(
                object,
                (x + 80, y + 22),
                color=Color.BLACK.value,
                fontname=PTEXT_FONT,
                fontsize=18,
                align="left",
            )
        else:
            ptext.drawbox(
                object,
                (x + 80, y + 10, 300, 50),
                align="left",
                color=Color.BLACK.value,
                fontname=PTEXT_FONT,
            )
        pygame.draw.rect(
            window,
            Color.GREY.value if idx not in selection else Color.RED.value,
            (x + 29, y + 17, 32, 32),
        )
        ptext.drawbox(
            str(idx),
            (x + 29, y + 17, 32, 32),
            align="center",
            color=Color.BLACK.value,
            fontname=PTEXT_FONT,
        )

    coordinates = [
        (30, 280),
        (30, 374),
        (30, 468),
        (483, 277),
        (483, 371),
        (483, 465),
    ]

    for idx, (object, (x, y)) in enumerate(zip(options["options"], coordinates)):
        draw_button(x, y, idx + 1, object["name"])

    ptext.drawbox(
        options["prompt"],
        (30, 120, 845, 110),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )
    select_class_2 = """USE THE NUMBERS ON THE KEYBOARD TO SELECT YOUR CHOICE"""
    ptext.drawbox(
        select_class_2,
        (104, 236, 700, 25),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )

    pygame.draw.rect(
        window, Color.SEAGREEN.value, (309, 564, 292, 44), border_radius=40
    )
    ptext.drawbox(
        "CONTINUE",
        (323, 570, 263, 31),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )
    ptext.drawbox(
        "PRESS ENTER OR SPACE",
        (620, 570, 180, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )


def draw_warning(window, message, button):
    pygame.draw.rect(window, Color.YELLOW.value, (212, 205, 487, 290), border_radius=25)

    ptext.drawbox(
        message,
        (237, 238, 435, 144),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )

    pygame.draw.rect(
        window, Color.SEAGREEN.value, (304, 397, 292, 44), border_radius=40
    )
    ptext.drawbox(
        button,
        (319, 403, 263, 31),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )
    ptext.drawbox(
        "PRESS ENTER OR SPACE",
        (298, 448, 307, 17),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )


def draw_end_game(window, phil_scores, category_scores):
    box = pygame.draw.rect(window, Color.RED.value, (112, 37, 669, 88))
    font = FONT(36)
    text = font.render("CONGRATULATIONS!", True, Color.BLACK.value)
    window.blit(text, text.get_rect(center=box.center))

    ptext.drawbox(
        "You've completed your first year at Harvard!",
        (117, 145, 674, 70),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )

    ptext.drawbox(
        f"SCHOOL\t{category_scores['school']}",
        (60, 242, 300, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )
    ptext.drawbox(
        f"FUN\t{category_scores['fun']}",
        (310, 242, 300, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )
    ptext.drawbox(
        f"REST\t{category_scores['rest']}",
        (550, 242, 300, 30),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )

    ptext.drawbox(
        "WOULD THE PHILOSOPHERS APPROVE OF THE CHOICES YOU'VE MADE?",
        (77, 290, 754, 85),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )

    sorted_scores = dict(
        sorted(phil_scores.items(), key=lambda item: item[1], reverse=True)
    )

    with open("data/end_messages.json") as f:
        messages = json.load(f)
        message = messages[list(sorted_scores.keys())[0]]

    ptext.drawbox(
        message,
        (29, 385, 847, 103),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )

    coordinates = [
        (70, 500),
        (360, 500),
        (630, 500),
        (252, 540),
        (510, 540),
    ]

    for idx, (phil, score) in enumerate(sorted_scores.items()):
        ptext.draw(
            f"{phil.upper()}\t{score}",
            coordinates[idx],
            fontsize=26,
            align="center",
            color=Color.BLACK.value if idx > 0 else Color.RED.value,
            fontname=PTEXT_FONT,
        )

    font = FONT(30)
    text = font.render("PLAY AGAIN", True, Color.BLACK.value)

    box = pygame.draw.rect(
        window, Color.SEAGREEN.value, (165, 600, 579, 58), border_radius=40
    )
    window.blit(text, text.get_rect(center=box.center))

    ptext.drawbox(
        "PRESS ENTER OR SPACE",
        (186, 673, 523, 22),
        align="center",
        color=Color.BLACK.value,
        fontname=PTEXT_FONT,
    )
