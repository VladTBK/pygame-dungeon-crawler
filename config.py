import pygame
from paths import Paths
from os import listdir


class Config(Paths):
    def __init__(self):
        super().__init__()
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.SPEED1 = 5
        self.FPS = 60
        self.SCALE = 3
        self.GAME_NAME = "Dungeon Crawler"
        self.COLORS = {"RED": (255, 0, 0), "BG": (0, 0, 0)}

    def scale_img(self, img):
        return pygame.transform.scale(
            img, (img.get_width() * self.SCALE, img.get_height() * self.SCALE)
        )

    def load_imgs(self, img_type):
        img_list = []
        for f in listdir(img_type):
            path = img_type + "/" + f
            player_img = pygame.image.load(path).convert_alpha()
            player_img = self.scale_img(player_img)
            img_list.append(player_img)
        return img_list

    def build_animations_list(self, *args):
        for arg in args:
            if arg in self.IMAGE_DICT:
                states = list(self.IMAGE_DICT[arg].keys())
                for state in states:
                    img_type = self.IMAGE_DICT[arg][state][0]
                    self.IMAGE_DICT[arg][state][1] = self.load_imgs(img_type)

    def get_images(self, img_type):
        values = list(self.IMAGE_DICT[img_type].keys())
        out_dict = {}
        for val in values:
            out_dict[val] = self.IMAGE_DICT[img_type][val][1]
        return out_dict
