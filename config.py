import pygame
from os import listdir


class Config:
    def __init__(self):
        self.PLAYER_MALE_ELF_IDLE_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/player-male-elf/idle"
        self.PLAYER_MALE_ELF_RUN_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/player-male-elf/run"
        self.PLAYER_FEMALE_ELF_IDLE_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/player-female-elf/idle"
        self.PLAYER_FEMALE_ELF_RUN_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/player-female-elf/run"
        self.IMAGE_DICT = {self.PLAYER_MALE_ELF_IDLE_PATH: []}
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
        if img_type in self.IMAGE_DICT:
            for f in listdir(img_type):
                path = img_type + "/" + f
                player_img = pygame.image.load(path).convert_alpha()
                player_img = self.scale_img(player_img)
                self.IMAGE_DICT[img_type].append(player_img)
            return self.IMAGE_DICT[img_type]
        else:
            return "Unkown image type path"
