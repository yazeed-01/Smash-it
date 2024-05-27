import pygame.mixer 
import pygame
import random
import math
import sys
import pygame.font
from random import randint


pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SMASH IT")

FPS = 60
BALL_RADIUS = 10
lives = 3


