#screen size
SIZE = width, height = 1280, 720

#constants representing colors
BLUE = (71,106,165)
RED = (190,61,52)
GREEN = (119,182,60)
YELLOW = (244,234,61)
GREY = (200,200,200)
WHITE = (255,255,254)
BLACK = (0,0,0)

#boardsize and tilesize
TILESIZE = int (SIZE[1] / 14)
MAPSIZE = 14
OFFSET = (SIZE[0] - (TILESIZE*MAPSIZE)) / 2