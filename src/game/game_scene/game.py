import math
import random
import logging
import time

import pygame

from src.config import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)

from src.game.game_scene.game import GameScene
from src.game.game_scene.menu_scene import MenuScene
from src.game.knapsack import Knapsack


class GameScene:

    def __init__(self, window, difficulty):
        self.window = window
        self.knapsack = Knapsack(window, difficulty)

        self.difficulty = difficulty
        self.score = 0

        self.item_list = self.generate_sample_itens()
        
        # load image texture
        crt_texture = pygame.image.load(ASSETS_DIR + 'crt_scanlines.png').convert_alpha()
        crt_texture.set_alpha(100)
        self.crt_texture = pygame.transform.scale(crt_texture, (WINDOW_WIDTH, WINDOW_HEIGHT))

        # load hud image
        hud_image = pygame.image.load(ASSETS_DIR + 'hud.png').convert_alpha()
        self.hud_image = pygame.transform.scale(hud_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    def generate_sample_itens(self):
        item_list = [
            {'name': 'Estus Flask', 'weight': 1, 'value': 10},
            {'name': 'Longsword', 'weight': 5, 'value': 20},
            {'name': 'Greatshield of Artorias', 'weight': 15, 'value': 50},
            {'name': 'Black Knight Greataxe', 'weight': 12, 'value': 40},
            {'name': 'Havel\'s Set', 'weight': 20, 'value': 60},
            {'name': 'Crystal Magic Weapon', 'weight': 2, 'value': 30},
            {'name': 'Silver Knight Straight Sword', 'weight': 6, 'value': 25},
            {'name': 'Giant Dad Mask', 'weight': 4, 'value': 35},
            {'name': 'Greatsword of Artorias', 'weight': 14, 'value': 45},
            {'name': 'Dragon Tooth', 'weight': 18, 'value': 55},
            {'name': 'Crown of Dusk', 'weight': 3, 'value': 15},
            {'name': 'Balder Side Sword', 'weight': 4, 'value': 20},
            {'name': 'Black Iron Set', 'weight': 16, 'value': 55},
            {'name': 'Chaos Zweihander', 'weight': 10, 'value': 35},
            {'name': 'Mask of the Child', 'weight': 2, 'value': 10},
            {'name': 'Quelaag\'s Furysword', 'weight': 8, 'value': 30},
            {'name': 'Dark Wood Grain Ring', 'weight': 1, 'value': 15},
            {'name': 'Silver Knight Armor Set', 'weight': 12, 'value': 40},
            {'name': 'Black Bow of Pharis', 'weight': 5, 'value': 25},
            {'name': 'Grass Crest Shield', 'weight': 3, 'value': 15},
        ]

        return item_list
        
    def draw_hud(self):
        self.window.blit(self.hud_image, (0, 0))

    