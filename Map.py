import random
import perlin_noise

# List of characters to randomly place on the map
vg = ["X", " ", "t", " ", " "]

# Function to create a random map
def generate_random_map(width, height):
    '''worldmap =  [
    '                                                                  ', # 0
    '                                                                  ', # 1
    '                t  t                                              ', # 2
    '        X     XXXXXXXXXs                   XX   X                 ', # 3 
    ' tXXXt     XX         XX                XXXX tt XX                ', # 4
    ' XX XX                                      XXXXX                 ', # 5
    '          Xt    t           t  t   X                              ', # 6
    '        XXXXXX  XXXXs    XXXXXXXXXXX  XX              tt t     XXX', # 7
    '     XX  X XX X  X XXXt     X XX  XX  XXX  XXXXXXXXs  XXXXXX      ', # 8
    'XXXXXXX  X  X X  X  XXXXXXXXX XX  XX  XXX  XX XX XXXXXXX  X       ', # 9
    ]#'''
    
    worldmap = []
    for row_idx in range(height):
        if row_idx == 0:
            # Top row should be all spaces
            row = ' ' * width
        if row_idx == 1:
            # Top row should be all spaces
            row = ' ' * width
        else:
            # Other rows are randomly generated
            row = ''.join(random.choice(vg) for _ in range(width))
        worldmap.append(row)
    return worldmap

# Generate a random worldmap with width and height
map_width = 70  # adjust the width 
map_height = 10  # adjust the height 
worldmap = generate_random_map(map_width, map_height)

for row in worldmap:
    print(row)
