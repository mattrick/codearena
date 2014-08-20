from tile import Tile

class Map:
    starting_tile = None

    def __init__(self, tile):
        self.starting_tile = tile

    def get_staring_tile(self):
        return self.starting_tile

    @staticmethod
    def hex_distance(tile1, tile2):
        return (abs(tile1.q - tile2.q) + abs(tile1.r - tile2.r)
          + abs(tile1.q + tile1.r - tile2.q - tile2.r)) / 2

    @staticmethod
    def get_range(tile, n):

    @staticmethod
    def get_ring(tile, n):
