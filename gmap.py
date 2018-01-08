import cell

class Map_neighbour:
    def __call__(self,  coords):
        for i in range(-1, 2):
            for j in range(-1, 2):
                yield [coords[0] + i, coords[1] + j]

class Game_map:
    def __init__(self):
        self.map = dict()

    def __iter__(self):
        return iter(self.map)
    
    def __getitem__(self, coords):
        return self.map[coords]

    def __setitem__(self, coords, cell):
        self.map[coords] = cell

    def get_cell(self, coords):
        if coords in self.map:
            return self.map[coords]
        else:
            raise ValueError

    def check_cell(self, coords, cond):
        if coords in self.map:
            return cond(self.map[coords])
        else:
            raise ValueError

    def change_cell(self, coords, change):
        if coords in self.map:
            self.map[coords] = change(self.map[coords])
        else:
            raise ValueError

    def set_cell(self, coords, cell):
        self.map[coords] = cell

    #def neighbor_func(self, coords)

    def neighborhood(self, coords):
        if coords in self.map:
            neigh = Map_neighbour()
            for coords in neigh(coords):
                yield self.map[coords]
        else:
            raise ValueError
