
'''# World Map Layout
world_map = [
    '                                                                  ',
    '                                                                  ',
    '                t  t                                              ',
    '        X     XXXXXXXXXs                   XX   X                 ',
    ' tXXXt     XX         XX                XXXX tt XX                ',
    ' XX XX                                      XXXXX                 ',
    '          Xt    t           t  t   X                            G ',
    '        XXXXXX  XXXXs    XXXXXXXXXXX  XX              tt t     XXX',
    ' P   XX  X XX X  X XXXt     X XX  XX  XXX  XXXXXXXXs  XXXXXX      ',
    'XXXXXXX  X  X X  X  XXXXXXXXX XX  XX  XXX  XX XX XXXXXXX  X       ',
]

tile_size = 50
WIDTH, HEIGHT = 1000, len(world_map) * tile_size#'''

import random

# Define tile types with a reduced chance of 't'
TILES = [' ', ' ', ' ', 'X', 's', 'G']  # empty space, obstacle, start, goal (no 't' here for less ground)
WIDTH, HEIGHT = 1000, 600  # Width of the world and the height based on the map's length
# blah blah blah blah
tile_size = 50
map_width = WIDTH // tile_size
map_height = HEIGHT // tile_size

def generate_world_map(width, height):
    world_map = []
    for y in range(height):
        row = ''
        for x in range(width):
            # Randomly select a tile for the current position
            tile = random.choice(TILES)
            row += tile
        world_map.append(row)
    return world_map

def place_player_on_obstacle(world_map):
    # Iterate over the map to find an 'X' tile and place 'P' on it if it's not next to a 't'
    for y in range(len(world_map)):
        for x in range(len(world_map[y])):
            if world_map[y][x] == 'X':
                # Check if any adjacent tiles are 't' (ground), if so, skip this 'X'
                if (x > 0 and world_map[y][x-1] == 't') or (x < len(world_map[y]) - 1 and world_map[y][x+1] == 't') or (y > 0 and world_map[y-1][x] == 't') or (y < len(world_map) - 1 and world_map[y+1][x] == 't'):
                    continue
                # Place 'P' on top of 'X' and return the modified map
                world_map[y] = world_map[y][:x] + 'P' + world_map[y][x + 1:]
                return world_map  # Stop once 'P' is placed
    return world_map  # If no valid 'X' found, return the original map

def ensure_x_under_goal(world_map):
    # Find the position of 'G' and place 3 'X' tiles directly below it
    for y in range(len(world_map)):
        for x in range(len(world_map[y])):
            if world_map[y][x] == 'G':
                # Ensure at least 3 'X' tiles directly below the 'G' tile
                for i in range(1, 4):
                    if y + i < len(world_map):
                        # Replace the tile directly below 'G' with 'X'
                        world_map[y + i] = world_map[y + i][:x] + 'X' + world_map[y + i][x + 1:]
                return world_map
    return world_map  # If no 'G' found, return the original map

# Generate a new random world map
world_map = generate_world_map(map_width, map_height)

# Now place the player 'P' on top of an 'X' tile that is not adjacent to 't'
world_map = place_player_on_obstacle(world_map)

# Ensure there are at least 3 'X' tiles under the 'G' tile
world_map = ensure_x_under_goal(world_map)

# Print the generated world map for visualization
for row in world_map:
    print(row)




