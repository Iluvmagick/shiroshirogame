class Cell:
    def __init__(self, char, color, propreties = dict()):
        self.char = char
        self.propreties = propreties
        self.color = color

    def draw_char(self):
        return self.char

    def draw_color(self):
        return self.color

    def get_propreties():
        return self.propreties
