import pygame
import math
from config import Config
from items import Hearth

cfg = Config()


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, img_list):
        pygame.sprite.Sprite.__init__(self)
        self.flip = False
        self.frame_idx = 0
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect(0, 0, cfg.TILE_SIZE, cfg.TILE_SIZE)
        self.rect.center = (x, y)
        self.image_list = img_list
        self.state = "idle"
        self.image = self.image_list[self.state][self.frame_idx]
        self.animation_cd = 100

    def update(self):
        self.image = self.image_list[self.state][self.frame_idx]
        if pygame.time.get_ticks() - self.update_time > self.animation_cd:
            self.frame_idx += 1
            self.update_time = pygame.time.get_ticks()
            self.frame_idx %= len(self.image_list[self.state])

    def draw(self, screen):
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        if self.offset:
            screen.blit(
                flipped_image,
                (self.rect.x, self.rect.y - cfg.SCALE_CHARACTER * self.offset),
            )
        else:
            screen.blit(flipped_image, self.rect)
        pygame.draw.rect(screen, cfg.COLORS["RED"], self.rect, 1)


class Enemy(Character):
    def __init__(self, x, y, img_list):
        super().__init__(x, y, img_list)
        self.health = cfg.CHARACTER_SPECS["goblin"]["health"]
        self.offset = cfg.CHARACTER_SPECS["goblin"]["offset"]

    def update(self):
        super().update()
        if self.health <= 0:
            self.kill()


class Player(Character):
    def __init__(self, x, y, img_list, hearth_img_list):
        super().__init__(x, y, img_list)
        self.health = cfg.CHARACTER_SPECS["elf-m"]["health"]
        self.offset = cfg.CHARACTER_SPECS["elf-m"]["offset"]
        self.hearth_idx = 2
        self.hearth_val = self.health / (self.hearth_idx + 1)
        self.hearth_list = [
            Hearth(self.rect.centerx - 30, self.rect.centery, hearth_img_list),
            Hearth(self.rect.centerx, self.rect.centery, hearth_img_list),
            Hearth(self.rect.centerx + 30, self.rect.centery, hearth_img_list),
        ]

    def update(self):
        super().update()
        for idx, hearth in enumerate(self.hearth_list):
            hearth.rect.centerx = self.rect.centerx - 30 + idx * 30
            hearth.rect.centery = self.rect.centery - 40
            if idx == self.hearth_idx:
                hearth.update(self)
        if self.health <= 0:
            self.hearth_idx = -1
        elif self.health <= self.hearth_val:
            self.hearth_idx = 0
        elif self.health <= 2 * self.hearth_val:
            self.hearth_idx = 1

    def draw(self, screen):
        super().draw(screen)
        for hearth in self.hearth_list:
            hearth.draw(screen)

    def move(self, dx, dy):
        if dx != 0 and dy != 0:
            dx *= math.sqrt(2) / 2
            dy *= math.sqrt(2) / 2
        self.rect.x += dx
        self.rect.y += dy

        screen_scroll = [0, 0]
        if self.rect.right > (cfg.SCREEN_WIDTH - cfg.SCROLL_TRESH):
            screen_scroll[0] = cfg.SCREEN_WIDTH - cfg.SCROLL_TRESH - self.rect.right
            self.rect.right = cfg.SCREEN_WIDTH - cfg.SCROLL_TRESH
        if self.rect.left < cfg.SCROLL_TRESH:
            screen_scroll[0] = cfg.SCROLL_TRESH - self.rect.left
            self.rect.left = cfg.SCROLL_TRESH

        return screen_scroll
