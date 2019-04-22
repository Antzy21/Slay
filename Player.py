from Province import Province

player_colors = [(0, 0, 205),
                 (205, 0, 0),
                 (0, 205, 205),
                 (0, 205, 0),
                 (205, 0, 205)]

class Player():
    provinces = []

    def __init__(self, number):
        self.color = player_colors[number]
        self.number = number

    def new_province(self, *args):
        self.provinces.append(Province(self.number, len(self.provinces), args))

        

