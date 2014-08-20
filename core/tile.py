class Tile:
    Directions =    {
                        "w":    [-1, 0],
                        "nw":   [0, -1],
                        "ne":   [1, -1],
                        "e":    [1, 0],
                        "se":   [0, 1],
                        "sw":   [-1, 1]
                    }

    def __init__(self, r, q):
        self.neighbors = {   "w": None,
                            "nw": None,
                            "ne": None,
                            "e": None,
                            "se": None,
                            "sw": None}

        self.units = []
        self.objects = []
        self.buildings = []

        self.r = r
        self.q = q

    def set_neighbor(self, direction):
        self.neighbors[direction] = Tile(self.r + Tile.Directions[direction][0], self.q + Tile.Directions[direction][1])
        return self.neighbors[direction]

    def add_unit(self, unit):
        self.units.append(unit)

    def remove_unit(self, unit):
        self.units.remove(unit)

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def add_building(self, building):
        self.buildings.append(building)

    def remove_building(self, building):
        self.buildings.remove(building)

    def __str__(self):
        return "R: " + str(self.r) + ", Q: " + str(self.q)