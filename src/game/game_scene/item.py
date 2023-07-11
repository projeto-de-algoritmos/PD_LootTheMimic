import pygame


class Button:
    def __init__(self, text, color, x, y, width, height):
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pygame.font.Font(
            None, 24
        )  # you can adjust the size as per your need

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        text_surface = self.font.render(
            self.text, True, (0, 0, 0)
        )  # assuming black color for button text
        screen.blit(
            text_surface,
            (
                self.x + (self.width - text_surface.get_width()) / 2,
                self.y + (self.height - text_surface.get_height()) / 2,
            ),
        )

    def is_over(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if (
            self.x < pos[0] < self.x + self.width
            and self.y < pos[1] < self.y + self.height
        ):
            return True
        return False


class Item:
    WIDTH = 700
    HEIGHT = 100

    def __init__(self, item_dict):
        self.name = item_dict["name"]
        self.weight = item_dict["weight"]
        self.value = item_dict["value"]
        # self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), f"../../assets/{self.name}.png")
        self.font = pygame.font.Font(None, 32)
        self.button = Button("Add", (0, 255, 0), 0, 0, 60, 30)

    def render(self, screen, pos):
        # define the rectangle
        rect = pygame.Rect(pos[0], pos[1], self.WIDTH, self.HEIGHT)

        # draw the rectangle
        pygame.draw.rect(
            screen, (255, 255, 255), rect, 2
        )  # assuming white color for rectangle

        # blit the image onto the screen
        # screen.blit(pygame.transform.scale(self.image, (80, 80)), (pos[0]+10, pos[1]+10))  # 10 pixels padding

        # render the item properties
        name_surface = self.font.render(
            self.name, True, (255, 255, 255)
        )  # assuming white color for text
        weight_surface = self.font.render(
            f"Weight: {str(self.weight)}", True, (255, 255, 255)
        )
        value_surface = self.font.render(
            f"Value: {str(self.value)}", True, (255, 255, 255)
        )

        # blit the properties onto the screen
        screen.blit(name_surface, (pos[0] + 100, pos[1] + 10))
        screen.blit(weight_surface, (pos[0] + 100, pos[1] + 40))
        screen.blit(value_surface, (pos[0] + 100, pos[1] + 70))

        # update the button position and draw it
        self.button.x = pos[0] + (
            self.WIDTH * 0.8
        )  # Adjust position according to your design
        self.button.y = pos[1] + 35  # Adjust position according to your design
        self.button.draw(screen)

    def render_backpack(self, screen, pos):
        # define the rectangle
        rect = pygame.Rect(pos[0], pos[1], self.WIDTH, self.HEIGHT * 0.5)

        # draw the rectangle
        pygame.draw.rect(
            screen, (255, 255, 255), rect, 2
        )  # assuming white color for rectangle

        # render the item properties
        name_surface = self.font.render(
            self.name, True, (255, 255, 255)
        )  # assuming white color for text
        weight_surface = self.font.render(
            f"Weight: {str(self.weight)}", True, (255, 255, 255)
        )
        value_surface = self.font.render(
            f"Value: {str(self.value)}", True, (255, 255, 255)
        )

        # blit the properties onto the screen
        screen.blit(name_surface, (pos[0] + 50, pos[1] + 15))
        screen.blit(weight_surface, (pos[0] + 400, pos[1] + 15))
        screen.blit(value_surface, (pos[0] + 550, pos[1] + 15))
