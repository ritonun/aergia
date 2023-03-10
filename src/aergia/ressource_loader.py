import os
import pygame
from .gameobject import AnimatedSprite


class RessourceManager:
    def __init__(self, ressource_path):
        self.res_path = ressource_path
        self.tilesets = {}
        self.images = {}
        self.fonts = {}
        self.animations = {}

    def load_tilesets(self, tileset_folder, tile_width, tile_height, subfolders=[]):
        subfolders = list(subfolders)
        full_path = os.path.join(self.res_path, tileset_folder, "")
        files = load_folder(full_path)
        for file in files:
            if find_extension(file) not in [".png", ".jpeg"]:
                continue
            tileset_name = get_file_name_from_path(file)
            tileset = load_tileset_image(file, tile_width, tile_height)
            self.tilesets[tileset_name] = tileset

        for subfolder in subfolders:
            path = os.path.join(full_path, subfolder, "")
            files = load_folder(path)
            for file in files:
                if find_extension(file) not in [".png", ".jpeg"]:
                    continue
                tileset_name = get_file_name_from_path(file)
                tileset = load_tileset_image(file, tile_width, tile_height)
                subname = get_folder_name_from_path(file)
                if subname not in self.tilesets:
                    self.tilesets[subname] = {}
                self.tilesets[subname][tileset_name] = tileset

    def load_images(self, image_folder, subfolders=[]):
        subfolders = list(subfolders)
        full_path = os.path.join(self.res_path, image_folder, "")
        files = load_folder(full_path)
        for file in files:
            image_name = get_file_name_from_path(file)
            image = pygame.image.load(file).convert_alpha()
            self.images[image_name] = image

        for subfolder in subfolders:
            path = os.path.join(full_path, subfolder, "")
            files = load_folder(path)
            for file in files:
                image_name = get_file_name_from_path(file)
                image = pygame.image.load(file).convert_alpha()
                subname = get_folder_name_from_path(file)
                if subname not in self.images:
                    self.images[subname] = {}
                self.images[subname][image_name] = image

    def load_fonts(self, fonts_folder, subfolders=[]):
        subfolders = list(subfolders)
        full_path = os.path.join(self.res_path, fonts_folder, "")
        files = load_folder(full_path)
        for file in files:
            font_name = get_file_name_from_path(file)
            font = file
            self.fonts[font_name] = font

        for subfolder in subfolders:
            path = os.path.join(full_path, subfolder, "")
            files = load_folder(path)
            for file in files:
                font_name = get_file_name_from_path(file)
                font = file
                subname = get_folder_name_from_path(file)
                if subname not in self.tilesets:
                    self.fonts[subname] = {}
                self.fonts[subname][font_name] = font

    def load_animations(self, animation_folder, tile_width, tile_height, subfolders=[]):
        subfolders = list(subfolders)
        full_path = os.path.join(self.res_path, animation_folder, "")
        files = load_folder(full_path)
        for file in files:
            animation_name = get_file_name_from_path(file)
            animation_tileset = load_tileset_1d(file, tile_width, tile_height)
            animation = AnimatedSprite(0, 0, animation_tileset)
            self.animations[animation_name] = animation

        for subfolder in subfolders:
            path = os.path.join(full_path, subfolder, "")
            files = load_folder(path)
            for file in files:
                animation_name = get_file_name_from_path(file)
                animation_tileset = load_tileset_1d(file, tile_width, tile_height)
                animation = AnimatedSprite(0, 0, animation_tileset)
                subname = get_folder_name_from_path(file)
                if subname not in self.animations:
                    self.animations[subname] = {}
                self.animations[subname][animation_name] = animation


def get_folder_name_from_path(path):
    try:
        head, base = os.path.split(path)
        if find_extension(base) is None:
            return base
        folder_name = os.path.split(head)[-1]
        return folder_name
    except Exception:
        return None


def get_file_name_from_path(path):
    base = os.path.split(path)[-1]
    ext = find_extension(base)
    name = base.replace(ext, "")
    return name


def find_extension(name):
    name_index = name.rfind('.')
    if name_index == -1:
        return None
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
