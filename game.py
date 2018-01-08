import gmap
import cell
import tdl
import random

def randcolor():
    return (random.randrange(256), random.randrange(256), random.randrange(256))

class Game:
    def __init__(self, console, game_map):
        self.console = console
        self.game_map = game_map

        self.map_top_x = 2
        self.map_top_y = 2
        self.map_fov_x = 0
        self.map_fov_y = 0
        self.map_fov_dx = 15
        self.map_fov_dy = 15

        self.cursor = [self.map_top_x, self.map_top_y]
        self.cursor_bg_color = (255, 255, 255)

    def draw_chunk(self, offset_x, offset_y, top_x, top_y, d_x, d_y):
        for i in range(top_x, top_x + d_x):
            for j in range(top_y, top_y + d_y):
                cell = self.game_map[(i, j)]
                self.console.draw_char(offset_x + i, offset_y + j,
                                       cell.draw_char(), cell.draw_color())

        cell = self.game_map[(self.cursor[0] - offset_x, self.cursor[1] - offset_y)]
        self.console.draw_char(self.cursor[0], self.cursor[1],
                               cell.draw_char(),
                               cell.draw_color(),
                               self.cursor_bg_color)
        tdl.flush()

    def map_init(self):
        for i in range(0, 15):
            for j in range(0, 15):
                self.game_map[(i, j)] = cell.Cell(char = '.', color = randcolor())

    def draw_map_interface(self):
        pass

    def move(self, x, y):
        self.cursor[0] = x
        self.cursor[1] = y

    def game_loop(self):
        self.map_init()

        while True:
            self.draw_chunk(self.map_top_x, self.map_top_y, self.map_fov_x,
                            self.map_fov_y, self.map_fov_dx, self.map_fov_dy)

            for event in tdl.event.get():
                if event.type == 'QUIT':
                    return
                elif event.type == 'KEYDOWN':
                    if event.char:
                        keychar = event.char[0]
                        if   keychar == 'a':
                            if not (self.cursor[0] == self.map_top_x):
                                 self.move(self.cursor[0] - 1, self.cursor[1])
                        elif keychar == 'd':
                            if not (self.cursor[0] == self.map_top_x + self.map_fov_dx - 1):
                                 self.move(self.cursor[0] + 1, self.cursor[1])
                        elif keychar == 'w':
                            if not (self.cursor[1] == self.map_top_y):
                                 self.move(self.cursor[0], self.cursor[1] - 1)
                        elif keychar == 's':
                            if not (self.cursor[1] == self.map_top_y + self.map_fov_dy - 1):
                                 self.move(self.cursor[0], self.cursor[1] + 1)
