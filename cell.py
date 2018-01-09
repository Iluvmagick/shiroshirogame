class Cell:
    def __init__(self, char, color, propreties = dict()):
        self.char = char
        self.propreties = propreties
        self.color = color

    def draw_char(self):
        return self.char

    def draw_color(self):
        return self.color

    def get_propreties(self):
        return self.propreties

    def get_text(self):
        """Returns the text, which would be displayed if the cursor is over this cell"""
        return "Just a cell"
