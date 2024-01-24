import pygame
import math
from config import Config

cfg = Config()


class Player:
    def __init__(self, x, y, img_list):
        self.flip = False
        self.frame_idx = 0
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)
        self.image_list = img_list
        self.state = "idle"
        self.image = self.image_list[self.state][self.frame_idx]

    def move(self, dx, dy):
        if dx != 0 and dy != 0:
            dx *= math.sqrt(2) / 2
            dy *= math.sqrt(2) / 2
        self.rect.x += dx
        self.rect.y += dy

    def update(self):
        animation_cooldown = 100
        self.image = self.image_list[self.state][self.frame_idx]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_idx += 1
            self.update_time = pygame.time.get_ticks()
            self.frame_idx %= len(self.image_list[self.state])

    def draw(self, screen):
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(flipped_image, self.rect)
        pygame.draw.rect(screen, cfg.COLORS["RED"], self.rect, 1)
