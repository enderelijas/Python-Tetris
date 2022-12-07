import pygame, sys
from blocks import Block

width = 600
height = 600
#screen = pygame.display.set_mode((width, height))

block_size = 10

black = 0, 0, 0

# gameloop

y = height
x = width / 2

x_change = 0
y_change = -10

def game_loop():
    while True:
        screen.fill(black)
        clock = pygame.time.Clock()

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit()

            if (event.type == pygame.KEYDOWN):
                if (event.type == pygame.K_LEFT):
                    x_change = -10
                elif (event.type == pygame.K_RIGHT):
                    x_change = 10

        pygame.display.update()

#game_loop()


print(Block().draw())