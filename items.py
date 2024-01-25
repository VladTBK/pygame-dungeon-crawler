import pygame
from config import Config

cfg = Config()


class Hearth:
    def __init__(self, x, y, img_list):
        self.image_list = img_list
        self.offsety = cfg.CHARACTER_SPECS["hearth"]["offsety"]
        self.offsetx = cfg.CHARACTER_SPECS["hearth"]["offsetx"]
        self.states = ["full", "half", "empty"]
        self.state = "full"
        self.image = self.image_list[self.state][0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_cd = 1000

    def update(self, player):
        self.image = self.image_list[self.state][0]
        moded_health = player.health - player.hearth_idx * player.hearth_val
        threshold = player.hearth_val / 2
        if 0 < moded_health <= 2:
            self.state = self.states[2]
            player.health -= 0.5
        elif 2 < moded_health <= threshold:
            self.state = self.states[1]
            player.health -= 0.5
        else:
            self.state = self.states[0]
            player.health -= 0.5

    def draw(self, screen):
        screen.blit(
            self.image,
            (
                self.rect.centerx - cfg.SCALE_ITEMS * self.offsetx,
                self.rect.centery - cfg.SCALE_ITEMS * self.offsety,
            ),
        )
