from distutils.core import setup
import py2exe
import gc
import math
import os
from random import randint
import pyglet

import OpenGL
try:
    from OpenGL.GL import *
    from OpenGL.raw.GLU import gluOrtho2D
except:
    from OpenGL.platform.win32 import Win32Platform
    from OpenGL.GL import *
    from OpenGL.raw.GLU import gluOrtho2D

from functions import drawInfoLabel, getElpsTime, translateSeed
from game.GUI.Button import Button
from game.GUI.Editarea import Editarea
from game.GUI.GUI import GUI
from game.GUI.Sliderbox import Sliderbox
from game.entity.Player import Player
from game.sound.BlockSound import BlockSound
from game.sound.Sound import Sound
from game.Scene import Scene
from game.world.Biomes import getBiomeByTemp
from game.world.worldGenerator import worldGenerator

setup(
    console=['main.py'],
    packages=['gui', 'game', 'sounds', 'textures', 'particles']
)
