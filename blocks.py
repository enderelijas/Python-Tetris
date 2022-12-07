import pygame
from random import choice

class Block():
    def __init__(self):
        self.shapes = [
            [(0, 0), (1, 0), (2, 0), (3, 0)],
            [(0, 0), (1, 0), (0, 1), (1, 1)],
            [(0, 0), (1, 0), (2, 0), (2, 1)],
            [(0, 0), (1, 0), (2, 0), (1, 1)]
        ]
        self.colors = [
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255)
        ]

    def get_random_color(self):
        colors = self.colors

        return choice(colors)

    def draw(self, surface, block_size):
        shape = choice(self.shapes)
        color = Block().get_random_color()

        for x, y in shape:
            print(f'x: {x} and y: {y}')
            pygame.draw.rect(surface, color, pygame.Rect(x, y, block_size, block_size))
    