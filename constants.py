from functools import partial
import pygame
from enum import Enum

FONT = partial(pygame.font.Font, "fonts/Pixelify_Sans/static/PixelifySans-Regular.ttf")
BOLD_FONT = partial(
    pygame.font.Font, "fonts/Pixelify_Sans/static/PixelifySans-Bold.ttf"
)
PTEXT_FONT = "fonts/Pixelify_Sans/static/PixelifySans-Regular.ttf"
PTEXT_BOLD_FONT = "fonts/Pixelify_Sans/static/PixelifySans-Bold.ttf"


class Color(Enum):
    RED = (255, 51, 102)
    BLACK = (1, 22, 39)
    BLUE = (32, 164, 243)
    LINEN = (241, 234, 226)
    GREEN = (177, 214, 144)
    SEAGREEN = (46, 196, 182)
    GREY = (217, 217, 217)
    


courses = [
    "Some kind of plant biology course.",
    "CS 1240. Data Structures and Algorithms.",
    "GenEd 1091. Classical Chinese Political & Ethical Theory. Puett.",
    "Some government course about forms of government.",
    "Latin 1. Introductory Latin. Livingston",
    "Humanities 20. Colloquium in the Visual Arts. Lippit + 4.",
]
