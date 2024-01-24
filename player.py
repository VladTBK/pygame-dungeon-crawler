import pygame
import math
from config import Config

cfg = Config()


class Player:
    def __init__(self, x, y, img):
        self.flip = False
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)
        self.image = img

    def move(self, dx, dy):
        if dx != 0 and dy != 0:
            dx *= math.sqrt(2) / 2
            dy *= math.sqrt(2) / 2
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, screen):
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(flipped_image, self.rect)
        pygame.draw.rect(screen, cfg.COLORS["RED"], self.rect, 1)
