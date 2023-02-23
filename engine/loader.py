import os
import pygame
from .tools import Animation


def find_extension(name):
    name_index = name.rfind('.')
    ext = name[name_index:]
    return ext


def load_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    full_files = []
    for file in files:
        full_files.append(folder_path + file)
    return full_files


def load_tileset_1d(path, tile_width, tile_height, resize=1):
    image = pygame.image.load(path).convert_alpha()
    image_width, image_height = image.get_size()

    tile_table = []
    for tile_x in range(0, int(image_width / tile_width)):
        for tile_y in range(0, int(image_height / tile_height)):
            rect = (tile_x * tile_width, tile_y * tile_height,
                    tile_width, tile_height)
            img = image.subsurface(rect)
            if resize != 1:
                w, h = img.get_size()
                img = pygame.transform.scale(img, (w * resize, h * resize))
            tile_table.append(img)
    return tile_table


def load_tileset_from_folder(folder_path):
    files = load_folder(folder_path)
    tile_table = []
    for file in files:
        img = pygame.image.load(file).convert_alpha()
        tile_table.append(img)
    return tile_table


def load_tileset_image(path, tile_width, tile_height):
    image = pygame.image.load(path).convert_alpha()
    image_width, image_height = image.get_size()

    tile_table = []
    for tile_x in range(0, int(image_width / tile_width)):
        line = []
        tile_table.append(line)
        for tile_y in range(0, int(image_height / tile_height)):
            rect = (tile_x * tile_width, tile_y * tile_height,
                    tile_width, tile_height)
            line.append(image.subsurface(rect))
    return tile_table


def draw_tileset(table, display, tile_width, tile_height):
    for x, row in enumerate(table):
        for y, tile in enumerate(row):
            display.blit(tile, (x * tile_width, y * tile_height))


def load_all_graphics(folder_path):
    images = {}
    files = load_folder(folder_path)
    for file in files:
        ext = find_extension(file)
        if ext in [".png", ".jpeg", ".webp"]:
            image = pygame.image.load(file)

            if image.get_alpha():
                image.convert_alpha()
            else:
                image.convert()

            name = file.replace(folder_path, "")
            point = name.find('.')
            name = name[:point]
            images[name] = image
    return images


def load_animations_from_folder(folder_path, tile_width, tile_height, animation_speed, loop, resize_size=1):
    files = load_folder(folder_path)
    tilesets = {}
    for file in files:
        name = file.split('/')[-1].split('.')[0]
        tilesets[name] = load_tileset_1d(file, tile_width, tile_height, resize=resize_size)

    anims = {}
    for key in tilesets:
        anims[key] = Animation(0, 0, tilesets[key], speed=animation_speed, loop=loop)

    return anims


def load_image(path, resize=1):
    img = pygame.image.load(path).convert_alpha()
    w, h = img.get_size()
    img = pygame.transform.scale(img, (w * resize, h * resize))
    return img


def get_map_from_txt(path):
    lines = []
    with open(path, 'r') as f:
        lines = f.readlines()

    level = []
    i, j = 0, 0
    for line in lines:
        line = line.replace("\n", "")
        level.append([])
        for char in line:
            level[i].append(char)
            j += 1
        j = 0
        i += 1
    return level


def get_tile_map(grid, tileset):
    level = []
    for y in range(len(grid)):
        level.append([])
        for x in range(len(grid[0])):
            level[y].append([])

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            tile = grid[y][x]
            if tile == "D":
                surf = tileset[0][2]
            else:
                surf = tileset[0][1]
            level[y][x] = surf
    return level


def draw_map(display, grid):
    for y, line in enumerate(grid):
        for x, tile in enumerate(line):
            display.blit(grid[y][x], (x, y))
