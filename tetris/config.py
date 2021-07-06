import pygame as pg

# scale unit
unit = 6 # 這是尺寸的基礎單位，基本上範圍是 3~10
# 如果畫面太小或太大可以優先調這個

# size
grid = 6*unit
background_color = (33, 47, 60)
rows = 20
columns = 10

width = columns * grid + 50*unit
height = rows * grid

# others
fps = 60
difficulty = 20  # 調整降下的速度，數字越大會越慢
score_count = {
    1: 40,
    2: 100,
    3: 300,
    4: 1200
}
font = ('Comic Sans MS', int(100 * (unit / 10)**1.5))
score_pos = (columns * grid + 10*unit, height // 2)
line_pos = (columns * grid + 10*unit, height // 2 + font[1])
next_piece_pos = (columns * grid + 22*unit, height // 2 - 30*unit)

# shapes: S, Z, I, O, J, L, T

'''
shape_format = {
    'S': [['.....',
           '.....',
           '..00.',
           '.00..',
           '.....'],
          ['.....',
           '..0..',
           '..00.',
           '...0.',
           '.....']],

    'Z': [['.....',
           '.....',
           '.00..',
           '..00.',
           '.....'],
          ['.....',
           '..0..',
           '.00..',
           '.0...',
           '.....']],

    'I': [['..0..',
           '..0..',
           '..0..',
           '..0..',
           '.....'],
          ['.....',
           '0000.',
           '.....',
           '.....',
           '.....']],

    'O': [['.....',
           '.....',
           '.00..',
           '.00..',
           '.....']],

    'J': [['.....',
           '.0...',
           '.000.',
           '.....',
           '.....'],
          ['.....',
           '..00.',
           '..0..',
           '..0..',
           '.....'],
          ['.....',
           '.....',
           '.000.',
           '...0.',
           '.....'],
          ['.....',
           '..0..',
           '..0..',
           '.00..',
           '.....']],

    'L': [['.....',
           '...0.',
           '.000.',
           '.....',
           '.....'],
          ['.....',
           '..0..',
           '..0..',
           '..00.',
           '.....'],
          ['.....',
           '.....',
           '.000.',
           '.0...',
           '.....'],
          ['.....',
           '.00..',
           '..0..',
           '..0..',
           '.....']],

    'T': [['.....',
           '..0..',
           '.000.',
           '.....',
           '.....'],
          ['.....',
           '..0..',
           '..00.',
           '..0..',
           '.....'],
          ['.....',
           '.....',
           '.000.',
           '..0..',
           '.....'],
          ['.....',
           '..0..',
           '.00..',
           '..0..',
           '.....']]
}
'''

shapes = {
    'S': [
        [(0, 0), (0, 1), (1, -1), (1, 0)],
        [(-1, 0), (0, 0), (0, 1), (1, 1)],
    ],
    'Z': [
        [(0, -1), (0, 0), (1, 0), (1, 1)],
        [(-1, 0), (0, -1), (0, 0), (1, -1)],
    ],
    'I': [
        [(-2, 0), (-1, 0), (0, 0), (1, 0)],
        [(-1, -2), (-1, -1), (-1, 0), (-1, 1)],
    ],
    'O': [
        [(0, -1), (0, 0), (1, -1), (1, 0)],
    ],
    'J': [
        [(-1, -1), (0, -1), (0, 0), (0, 1)],
        [(-1, 0), (-1, 1), (0, 0), (1, 0)],
        [(1, 1), (0, -1), (0, 0), (0, 1)],
        [(-1, 0), (1, -1), (0, 0), (1, 0)],
    ],
    'L': [
        [(-1, 1), (0, -1), (0, 0), (0, 1)],
        [(-1, 0), (0, 0), (1, 0), (1, 1)],
        [(1, -1), (0, -1), (0, 0), (0, 1)],
        [(-1, 0), (0, 0), (1, 0), (-1, -1)],
    ],
    'T': [
        [(-1, 0), (0, -1), (0, 0), (0, 1)],
        [(-1, 0), (1, 0), (0, 0), (0, 1)],
        [(1, 0), (0, -1), (0, 0), (0, 1)],
        [(-1, 0), (0, -1), (0, 0), (1, 0)],
    ],
}

SHADOW = (192, 192, 192)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (231, 76, 60)
PURPLE = (108, 52, 131)
BLUE = (40, 116, 166)
GREEN = (17, 122, 101)
YELLOW = (244, 208, 63)
LIGHT_PURPLE = (195, 155, 211)

shape_colors = {
    'S': GREEN,
    'Z': RED,
    'I': YELLOW,
    'O': BLUE,
    'J': PURPLE,
    'L': WHITE,
    'T': LIGHT_PURPLE
}
