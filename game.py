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
        # where to draw map
        self.map_top = (3, 3)
        self.map_fov = (0, 0)
        self.map_fov_d = (16, 16)
        # where to draw interface
        self.chunk_interface = (1, 1)
        self.map_info = (self.map_top[0] + self.map_fov_d[0] + 5, self.map_top[1])
        # cursor
        self.cursor = [self.map_top[0], self.map_top[1]]
        self.cursor_bg_color = (255, 255, 255)

    def get_cell_under_cursor(self):
        return self.game_map[(self.cursor[0] - self.map_top[0], self.cursor[1] - self.map_top[1])]

    def draw_chunk(self, offset, top, d):
        for i in range(top[0], top[0] + d[0]):
            for j in range(top[1], top[1] + d[1]):
                cell = self.game_map[(i, j)]
                self.console.draw_char(offset[0] + i, offset[1] + j,
                                       cell.draw_char(), cell.draw_color())

        cell = self.get_cell_under_cursor()
        self.console.draw_char(self.cursor[0], self.cursor[1],
                               cell.draw_char(),
                               cell.draw_color(),
                               self.cursor_bg_color)
        tdl.flush()

    def map_init(self):
        for i in range(0, self.map_fov_d[0]):
            for j in range(0, self.map_fov_d[1]):
                self.game_map[(i, j)] = cell.Cell(char = '.', color = randcolor())

    def draw_map_interface(self):
        # draw the map position
        chunk = str(self.map_fov[0]) + ", " + str(self.map_fov[1])
        chunk_str = "Current chunk top is : (" + chunk + ")"
        self.console.draw_str(self.chunk_interface[0], self.chunk_interface[1], chunk_str)

        map_fov = str(self.map_fov_d[0]) + ", " + str(self.map_fov_d[1])
        map_str = "You can see (" + map_fov + ") south and east"
        self.console.draw_str(self.chunk_interface[0], self.chunk_interface[1] + 1, map_str)
        # draw tile information
        cell = self.get_cell_under_cursor()
        self.console.draw_str(self.map_info[0], self.map_info[1], cell.get_text())

        tdl.flush()

    def move(self, x, y):
        self.cursor[0] = x
        self.cursor[1] = y

    def game_loop(self):
        self.map_init()

        while True:
            self.draw_chunk(self.map_top, self.map_fov, self.map_fov_d)
            self.draw_map_interface()

            for event in tdl.event.get():
                if event.type == 'QUIT':
                    return
                elif event.type == 'KEYDOWN':
                    if event.char:
                        keychar = event.char[0]
                        key = event.key
                        if   keychar == 'a':
                            if not (self.cursor[0] == self.map_top[0]):
                                 self.move(self.cursor[0] - 1, self.cursor[1])
                        elif keychar == 'd':
                            if not (self.cursor[0] == self.map_top[0] + self.map_fov_d[0] - 1):
                                 self.move(self.cursor[0] + 1, self.cursor[1])
                        elif keychar == 'w':
                            if not (self.cursor[1] == self.map_top[1]):
                                 self.move(self.cursor[0], self.cursor[1] - 1)
                        elif keychar == 's':
                            if not (self.cursor[1] == self.map_top[1] + self.map_fov_d[1] - 1):
                                 self.move(self.cursor[0], self.cursor[1] + 1)

                        if key == 'ESCAPE':
                            exit()
