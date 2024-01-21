import timeit

import pygame
import pyglet

pyglet.font.add_file('font.ttf')
mainFont = pyglet.font.load('font.ttf')

pygame.init()

monitor = pygame.display.Info()
WIDTH = 927  # monitor.current_w
HEIGHT = 566  # monitor.current_h
MAX_FPS = float("inf")
PAUSE = True
IN_MENU = True
MC_VERSION = "1.0"
clock = pygame.time.Clock()

FOV = 100
RENDER_DISTANCE = 100

CHUNKS_RENDER_DISTANCE = 900
CHUNK_SIZE = (4, 60, 4)
