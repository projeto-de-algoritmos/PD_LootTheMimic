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
from src.game.game_scene.item import Item

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

    def render_items(self, backpack_items, screen, start_x=50, start_y=50, gap=10):
        for index, item in enumerate(backpack_items):
            item.render(screen, (start_x, start_y + index * (100 + gap)))

    def run(self):
        self.state = GameState.PLAYING
        self.knapsack = Knapsack(self.window)
        items = self.item_list

        pprint("\nItens in chest:")
        pprint(items)

        pprint("\nKnapsack solve:")
        pprint(self.knapsack.solve_dynamic_programming(items, 40))

        backpack_items = [Item(item) for item in items]

        while self.state == GameState.PLAYING:
            self.render_items(backpack_items, self.window)
            clock.tick(15)
            pygame.display.flip()

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in backpack_items:
                        if item.button.is_over(pygame.mouse.get_pos()):
                            print(f"Button for {item.name} was clicked.")
                            # You can add the item to the backpack here
                        