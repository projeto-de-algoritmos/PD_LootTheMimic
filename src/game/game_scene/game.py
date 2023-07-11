import math
import random
import logging
import time
import sys
import os

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


class Button:
    def __init__(self, text, pos, size=(400, 50), color=(255, 223, 0)):  # Gold color
        self.text = text
        self.pos = pos
        self.size = size
        self.color = color
        self.font = pygame.font.Font(None, 36)

        self.rect = pygame.Rect(self.pos, self.size)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))  # Black text
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def is_over(self, pos):
        return self.rect.collidepoint(pos)


class GameState:
    PLAYING = 1
    GAME_OVER = 2


class GameScene:
    POOL_SIZE = 6

    ITEM_POOL = [
        {"name": "Estus Flask", "weight": 1, "value": 10},
        {"name": "Longsword", "weight": 5, "value": 20},
        {"name": "Greatshield of Artorias", "weight": 15, "value": 50},
        {"name": "Black Knight Greataxe", "weight": 12, "value": 40},
        {"name": "Havel's Helm", "weight": 20, "value": 60},
        {"name": "Crystal Magic Weapon", "weight": 2, "value": 30},
        {"name": "Silver Knight Straight Sword", "weight": 6, "value": 25},
        {"name": "Giant Dad Mask", "weight": 4, "value": 35},
        {"name": "Greatsword of Artorias", "weight": 14, "value": 45},
        {"name": "Dragon Tooth", "weight": 18, "value": 55},
        {"name": "Crown of Dusk", "weight": 3, "value": 15},
        {"name": "Balder Side Sword", "weight": 4, "value": 20},
        {"name": "Black Iron Helm", "weight": 16, "value": 55},
        {"name": "Chaos Zweihander", "weight": 10, "value": 35},
        {"name": "Mask of the Child", "weight": 2, "value": 10},
        {"name": "Quelaag's Furysword", "weight": 8, "value": 30},
        {"name": "Dark Wood Grain Ring", "weight": 1, "value": 15},
        {"name": "Silver Knight Helm", "weight": 12, "value": 40},
        {"name": "Black Bow of Pharis", "weight": 5, "value": 25},
        {"name": "Grass Crest Shield", "weight": 3, "value": 15},
    ]

    def __init__(self, window):
        self.window = window
        self.knapsack = Knapsack(window)

        self.score = 0

        self.item_list = self.generate_sample_itens()
        self.start_ticks = pygame.time.get_ticks()

        self.backpack = []
        self.backpack_font = pygame.font.Font(None, 36)
        self.backpack_capacity = 10

        self.submit_button = Button("Submit", (WINDOW_WIDTH * 0.7, WINDOW_HEIGHT * 0.9))
        self.menu_background = pygame.image.load(os.path.join(os.path.dirname(__file__), f"../../assets/mimic.jpg")).convert_alpha()


    def generate_sample_itens(self):
        return random.sample(self.ITEM_POOL, self.POOL_SIZE)

    def draw_hud(self):
        self.window.blit(self.hud_image, (0, 0))

    def render_items(self, backpack_items, screen, start_x=50, start_y=50, gap=10):
        for index, item in enumerate(backpack_items):
            item.render(screen, (start_x, start_y + index * (100 + gap)))

    def render_backpack(self, screen, start_x=950, start_y=100, gap=10):
        backpack_title = self.backpack_font.render(
            "Backpack", True, (255, 255, 255)
        )  # assuming white color for text
        screen.blit(
            backpack_title, (start_x, start_y - 50)
        )  # put it above the backpack items

        total_value = 0
        for index, item in enumerate(self.backpack):
            item.render_backpack(
                screen, (start_x, start_y + index * (80 + gap))
            )  # 100 is the height of the item rect and gap is the space between the items
            total_value += item.value  # summing up the total value

        # render the total value
        total_value_surface = self.backpack_font.render(
            f"Total Value: {total_value}", True, (255, 255, 255),
        )  # assuming white color for text
        backpack_capacity_surface = self.backpack_font.render(
            f"Capacity: {self.backpack_capacity}", True, (255, 255, 255),
        )
        screen.blit(
            total_value_surface,
            (start_x, start_y + len(self.backpack) * (80 + gap) + 10),
        )  # put it under the backpack items
        screen.blit(
            backpack_capacity_surface,
            (start_x, start_y + len(self.backpack) * (80 + gap) + 40),
        )

    def render_submit_button(self, screen):
        self.submit_button.render(screen)

    def run(self):
        score = 0
        self.state = GameState.PLAYING

        self.knapsack = Knapsack(self.window)
        items = self.item_list
        # random capacity 10 to 20
        self.backpack_capacity = random.randint(10, 20)

        pprint("\nItens in chest:")
        pprint(items)

        pprint("\nKnapsack solve:")
        max_score, solution = self.knapsack.solve_dynamic_programming(items, self.backpack_capacity)
        pprint(solution)
        converted_solution = [Item(item).name for item in solution]

        backpack_items = [Item(item) for item in items]

        while self.state == GameState.PLAYING:

            #background
            self.window.fill((0, 0, 0))
            self.menu_background.set_alpha(80)
            self.window.blit(self.menu_background, (0, 0))

            self.render_items(backpack_items, self.window)

            self.render_backpack(self.window)

            self.render_submit_button(self.window)

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
                            if item.name not in converted_solution:
                                pprint(item)
                                pprint('solution:')
                                pprint(converted_solution)
                                self.state = GameState.GAME_OVER
                                return 0
                            if item not in self.backpack:
                                score += item.value
                                self.backpack.append(item)

                    if self.submit_button.is_over(pygame.mouse.get_pos()):
                        print("Submit button was clicked.")
                        return score

        if self.state == GameState.GAME_OVER:
            print("Game over")
            self.window.fill((0, 0, 0))
            # self.draw_hud()

            game_over_text = pygame.font.Font(None, 36).render(
                "GAME OVER", True, (255, 255, 255)
            )
            self.window.blit(game_over_text, (WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.5))

            # draw ok button to restart game
            ok_button = Button("OK", (WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.6))
            ok_button.render(self.window)

            pygame.display.flip()

            while True:
                clock.tick(15)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if ok_button.is_over(pygame.mouse.get_pos()):
                            self.state = GameState.PLAYING
                            return 0
