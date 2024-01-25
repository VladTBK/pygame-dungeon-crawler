import pygame
from paths import Paths
from os import listdir


class Config(Paths):
    def __init__(self):
        super().__init__()
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.PLAYER_SPEED = 5
        self.ARROW_SPEED = 10
        self.ARROW_DMG = 5
        self.DMGTXT_DURATION = 100
        self.TILE_SIZE = 16 * 3
        self.FONT = ["assets/fonts/FiraCodeNerdFontMono-Retina.ttf", 20]
        self.FPS = 60
        self.SCALE_CHARACTER = 3
        self.SCALE_WEAPON = 2
        self.SCALE_ITEMS = 2
        self.SCROLL_TRESH = 200
        self.GAME_NAME = "Dungeon Crawler"
        self.COLORS = {"RED": (255, 0, 0), "BG": (0, 0, 0), "WHITE": (255, 255, 255)}
        self.CHARACTER_SPECS = {
            "elf-m": {"health": 100, "offset": 12},
            "goblin": {"health": 9999, "offset": 0},
            "hearth": {"offsetx": 6, "offsety": 6},
        }

    def scale_img(self, img, img_scale):
        return pygame.transform.scale(
            img, (img.get_width() * img_scale, img.get_height() * img_scale)
        )

    def load_imgs(self, img_type, character_type=None):
        img_list = []
        sorted_list = listdir(img_type)
        sorted_list.sort()
        for f in sorted_list:
            path = img_type + "/" + f
            player_img = pygame.image.load(path).convert_alpha()
            if character_type in self.weapon_list:
                player_img = self.scale_img(player_img, self.SCALE_WEAPON)
            elif character_type in self.items_list:
                player_img = self.scale_img(player_img, self.SCALE_ITEMS)
            else:
                player_img = self.scale_img(player_img, self.SCALE_CHARACTER)
            img_list.append(player_img)
        return img_list

    def build_animations_list(self, args):
        for arg in args:
            if arg in self.IMAGE_DICT:
                states = list(self.IMAGE_DICT[arg].keys())
                for state in states:
                    img_type = self.IMAGE_DICT[arg][state][0]
                    self.IMAGE_DICT[arg][state][1] = self.load_imgs(img_type, arg)

    def get_images(self, img_type):
        values = list(self.IMAGE_DICT[img_type].keys())
        out_dict = {}
        for val in values:
            out_dict[val] = self.IMAGE_DICT[img_type][val][1]
        return out_dict
