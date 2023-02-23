import pygame
import json


class LevelHandler:
    def __init__(self, path_dict):
        self.levels_path = path_dict
        self.levels = self.load_level()
        self.current_level = list(self.levels.keys())[0]

    def get_level_size(self):
        return self.levels[self.current_level].size

    def get_collisions_rect(self):
        return self.levels[self.current_level].collisions_rects

    def load_level(self):
        levels = {}
        for level_name in self.levels_path:
            levels[level_name] = Level(self.levels_path[level_name], level_name)
        return levels

    def change_level(self, level_name):
        # level_name: key in levels dict
        if level_name in self.levels:
            self.current_level = level_name
        else:
            raise KeyError("Level name '{}' does not exist.".format(level_name))

    def draw(self, display, offset=[0, 0]):
        self.levels[self.current_level].draw(display, offset=offset)


class Level:
    def __init__(self, path, name):
        self.name = name

        self.objects = None
        self.collisions_rects = None
        self.size = None
        self.tile_size = None
        self.load_level(path)

    def load_level(self, path):
        pass
    """
        data = None
        with open(path, "r") as f:
            data = json.load(f)

        w = data["width"]
        h = data["height"]
        tile_size = data["tilewidth"]
        self.size = (w * tile_size, h * tile_size)
        self.tile_size = tile_size

        obj_layer = []
        for layer in data["layers"]:
            if layer["name"].find("Calque d'Objets") != -1:
                obj_layer = layer

        all_objects = []

        for obj in obj_layer["objects"]:
            obj_values = {
                "x": obj["x"],
                "y": obj["y"],
                "h": obj["height"],
                "w": obj["width"],
                "color": self.get_color_from_string(obj["properties"][0]["value"])
            }
            all_objects.append(obj_values)

        collisions_rects = []
        objects = []
        for obj in all_objects:
            rect = pygame.Rect(obj["x"], obj["y"], obj["w"], obj["h"])
            neon_rect = engine.NeonRect(obj["color"], rect, n=10, outline=1)

            collisions_rects.append(rect)
            objects.append(neon_rect)

        self.collisions_rects = collisions_rects
        self.objects = objects


    def get_color_from_string(self, string):
        color = None
        if string == "RED":
            color = RED
        elif string == "BLUE":
            color = BLUE
        elif string == "GREEN":
            color = GREEN
        elif string == "WHITE":
            color = WHITE
        elif string == "NONE" or string == "none" or string == "None":
            color = (0, 0, 0, 0)
        return color
    """

    def draw(self, display, offset=[0, 0]):
        for obj in self.objects:
            obj.draw(display, offset=offset)
