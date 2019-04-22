from random import randint

class Province:
    money = 0
    selected = False

    def __init__(self, player_number, number, tiles):
        self.tiles = []
        self.number = number
        self.size = len(tiles)
        for tile in tiles:
            self.add_tile(tile)
        self.player_number = player_number
        self.capital = tiles[randint(0,len(tiles)-1)]
        self.capital.is_capital = True

    def select(self, grid):
        self.selected = True
        for tile in self.tiles:
            if not tile.highlighted:
                tile.highlight(grid)
            tile.select(grid)

    def evaluate_new_tile(self, tile):
        if tile.province == self:
            pass
        elif tile.province != None:
            if tile.province.size > self.size:
                tile.province.combine_provinces(self)
            else:
                self.combine_provinces(tile.province)
        else:
            self.add_tile(tile)

    def add_tile(self, tile):
        self.tiles.append(tile) 
        tile.province = self
        self.size += 1

    def combine_provinces(self,prov2):
        for tile in prov2.tiles:
            self.add_tile(tile)
        self.money += prov2.money
        prov2.capital.hex.draw();
        del prov2