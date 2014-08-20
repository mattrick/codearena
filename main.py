from settings import Settings
from core import Map, Tile

starting = Tile(0, 0)
my_map = Map(starting)

print my_map.get_staring_tile()

ne = starting.set_neighbor("ne")

print ne

ne2 = ne.set_neighbor("ne")

print ne2

print str(Map.hex_distance(starting, ne2))