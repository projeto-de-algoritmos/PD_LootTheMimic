import logging
import sys

import pygame
import argparse
from pygame.locals import *

from src.config import WINDOW_WIDTH, WINDOW_HEIGHT

from src.game.game_scene.game import GameScene
from src.game.game_scene.menu_scene import MenuScene

logging.basicConfig(level=logging.INFO)


ROUNDS = 5


class GameState:
    PLAYING = 1
    GAME_OVER = 2


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


def main():
    logging.info("Initializing pygame...")

    game_over_command = "menu"

    # parser = argparse.ArgumentParser()
    # parser.add_argument('--demo', action='store_true')
    # args = parser.parse_args()

    # true if --demo, false if not
    # print(args.demo)

    try:
        state = GameState.PLAYING
        pygame.init()

        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        overall_score = 0

        while state == GameState.PLAYING:
            # if game_over_command == 'menu':
            # menu = MenuScene(window)
            # difficulty = menu.run()

            for round in range(ROUNDS):
                print("Round", round + 1)
                game_scene = GameScene(window)
                overall_score += game_scene.run()

                print(f"Score: {overall_score}")

                state = GameState.GAME_OVER
                while state == GameState.GAME_OVER:
                    window.fill((0, 0, 0))

                    round_text = pygame.font.Font(None, 36).render(
                        f"Round: {round}/{ROUNDS}", True, (255, 255, 255)
                    )

                    window.blit(round_text, (100, 100))

                    score_text = pygame.font.Font(None, 36).render(
                        f"Your score: {overall_score}", True, (255, 255, 255)
                    )
                    window.blit(score_text, (WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.5))

                    continue_button = Button("continue", (200, 200))
                    continue_button.render(window)

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if continue_button.is_over(pygame.mouse.get_pos()):
                                state = GameState.PLAYING
                                continue

    except Exception as e:
        logging.exception(e)
        pygame.quit()
        raise e


if __name__ == "__main__":
    logging.info("Starting game...")
    main()
