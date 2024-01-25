import pygame
import random


class DamageTXT(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, color, font):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(damage, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.update_time = pygame.time.get_ticks()
        self.animation_cd = 1000
        self.direction = random.uniform(-1, 1)

    def update(self):
        super().update()
        self.rect.centerx += random.uniform(-0.7, 0.7) + self.direction
        self.rect.centery -= 1
        if pygame.time.get_ticks() - self.update_time > self.animation_cd:
            self.kill()
