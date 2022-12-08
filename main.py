import pygame, sys
from blocks import Block

width = 600
height = 600
#screen = pygame.display.set_mode((width, height))

block_size = 10

class Tetris():
    level = 2
    score = 0
    state = "start"
    field = []
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 20
    figure = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.state = "start"

        for i in range(height):
            new_line = []
            for x in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_figure(self):
        self.figure = Block(3, 0)

    def intersects(self):
        intersection = False
        for i in range(4):
            for x in range(4):
                if (i * 4 + x in self.figure.image()):
                    if ((i + self.figure.y > self.height - 1) or (x + self.figure.x > self.width - 1) or (x + self.figure.x < 0) or (self.field[i + self.figure.y][j + self.figure.x] > 0)):
                        intersection = True
        return intersection

    def freeze(self):
        for i in range(4):
            for x in range(4):
                if i * 4 + x in self.figure.image():
                    self.field[i + self.figure.y][x + self.figure.x] = self.figure.color

    def break_lines(self):
      lines = 0
      for i in range(1, self.height):
          zeros = 0
          for j in range(self.width):
              if self.field[i][j] == 0:
                  zeros += 1
          if zeros == 0:
              lines += 1
              for i1 in range(i, 1, -1):
                  for j in range(self.width):
                      self.field[i1][j] = self.field[i1 - 1][j]
      self.score += lines ** 2
      self.break_lines()
      self.new_figure()
      if self.intersects():
          game.state = "gameover"

    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation

# gameloop
pygame.init()

black = 0, 0, 0
size = (400, 500)
screen = pygame.display.set_mode(size)


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