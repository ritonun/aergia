import pygame

if pygame.version.vernum < (2, 1, 2):
    print("Warning ! This game is made for pygame version {}! You are on an older version.".
          format(pygame.version.vernum))

from .var import *  # noqa
from .debug import *  # noqa
from .graphics import *  # noqa
from .tools import *  # noqa
from .effect import *  # noqa
from .app import *  # noqa
