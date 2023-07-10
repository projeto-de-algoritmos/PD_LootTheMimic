import math
import random
import logging
import time

from pprint import pprint
import pygame

from src.config import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)
from src.game.game_scene.menu_scene import MenuScene
from src.game.knapsack import Knapsack


clock = pygame.time.Clock()


class GameState:
    PLAYING = 1
    SPAWNING = 2


class GameScene:
    POOL_SIZE = 6

    ITEM_POOL = [
        {"name": "Estus Flask", "weight": 1, "value": 10},
        {"name": "Longsword", "weight": 5, "value": 20},
        {"name": "Greatshield of Artorias", "weight": 15, "value": 50},
        {"name": "Black Knight Greataxe", "weight": 12, "value": 40},
        {"name": "Havel's Set", "weight": 20, "value": 60},
        {"name": "Crystal Magic Weapon", "weight": 2, "value": 30},
        {"name": "Silver Knight Straight Sword", "weight": 6, "value": 25},
        {"name": "Giant Dad Mask", "weight": 4, "value": 35},
        {"name": "Greatsword of Artorias", "weight": 14, "value": 45},
        {"name": "Dragon Tooth", "weight": 18, "value": 55},
        {"name": "Crown of Dusk", "weight": 3, "value": 15},
        {"name": "Balder Side Sword", "weight": 4, "value": 20},
        {"name": "Black Iron Set", "weight": 16, "value": 55},
        {"name": "Chaos Zweihander", "weight": 10, "value": 35},
        {"name": "Mask of the Child", "weight": 2, "value": 10},
        {"name": "Quelaag's Furysword", "weight": 8, "value": 30},
        {"name": "Dark Wood Grain Ring", "weight": 1, "value": 15},
        {"name": "Silver Knight Armor Set", "weight": 12, "value": 40},
        {"name": "Black Bow of Pharis", "weight": 5, "value": 25},
        {"name": "Grass Crest Shield", "weight": 3, "value": 15},
    ]

    def __init__(self, window):
        self.window = window
        self.knapsack = Knapsack(window)

        self.score = 0

        self.item_list = self.generate_sample_itens()
        self.start_ticks = pygame.time.get_ticks()

    def generate_sample_itens(self):
        return random.sample(self.ITEM_POOL, self.POOL_SIZE)

    def draw_hud(self):
        self.window.blit(self.hud_image, (0, 0))

    def run(self):
        self.state = GameState.PLAYING
        self.knapsack = Knapsack(self.window)
        itens = self.item_list

        pprint("\nItens in chest:")
        pprint(itens)

        pprint("\nKnapsack solve:")
        pprint(self.knapsack.solve_dynamic_programming(itens, 40))

        while self.state == GameState.PLAYING:
            clock.tick(15)
            pygame.time.delay(100)
