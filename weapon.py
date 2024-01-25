import pygame
import math
import random
from config import Config
from damage_display import DamageTXT

cfg = Config()


class Weapon:
    def __init__(self, img_list, arrow_image):
        self.image_list = img_list
        self.frame_idx = 0
        self.state = "idle"
        self.original_img = self.image_list[self.state][self.frame_idx]
        self.arrow_image = arrow_image
        self.angle = 0
        self.image = pygame.transform.rotate(self.original_img, self.angle)
        self.rect = self.image.get_rect()
        self.update_fire_time = pygame.time.get_ticks()
        self.fired = False
        self.fire_cd = 1000

    def update(self, player):
        self.rect.center = player.rect.center
        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.rect.centerx
        y_dist = -(pos[1] - self.rect.centery)
        self.angle = math.degrees(math.atan2(y_dist, x_dist))

        # offset so the bow is around the player
        self.rect.centerx += math.cos(math.radians(self.angle)) * 20
        self.rect.centery -= math.sin(math.radians(self.angle)) * 20
        if (
            pygame.mouse.get_pressed()[0]
            and pygame.time.get_ticks() - self.update_fire_time > self.fire_cd
        ):
            arrow = Arrow(
                self.arrow_image, self.rect.centerx, self.rect.centery, self.angle
            )
            self.update_fire_time = pygame.time.get_ticks()
            return arrow
        return None

    def draw(self, screen):
        self.image = pygame.transform.rotate(self.original_img, self.angle)
        true_center_x = self.rect.centerx - int(self.image.get_width() / 2)
        true_center_y = self.rect.centery - int(self.image.get_height() / 2)
        screen.blit(
            self.image,
            (
                true_center_x,
                true_center_y,
            ),
        )
        # pygame.draw.rect(screen, cfg.COLORS["RED"], self.rect, 1)


class Arrow(pygame.sprite.Sprite):
    def __init__(self, img_list, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image_list = img_list
        self.frame_idx = 0
        self.state = "idle"
        self.original_img = self.image_list[self.state][self.frame_idx]
        self.angle = angle - 90
        self.image = pygame.transform.rotate(self.original_img, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = cfg.ARROW_SPEED

    def update(self, enemy_group, damage_text_group, font):
        self.rect.centerx += math.cos(math.radians(self.angle + 90)) * self.speed
        self.rect.centery -= math.sin(math.radians(self.angle + 90)) * self.speed
        if (
            self.rect.right < 0
            or self.rect.left > cfg.SCREEN_WIDTH
            or self.rect.bottom < 0
            or self.rect.top > cfg.SCREEN_HEIGHT
        ):
            self.kill()
        for enemy in enemy_group:
            if enemy.rect.colliderect(self.rect):
                damage = cfg.ARROW_DMG + random.uniform(
                    -cfg.ARROW_DMG * 0.5, cfg.ARROW_DMG * 0.5
                )
                enemy.health -= damage
                self.kill()
                damage = str(damage)[:4]
                damage_text_group.add(
                    DamageTXT(
                        enemy.rect.centerx,
                        enemy.rect.centery,
                        damage,
                        cfg.COLORS["RED"],
                        font,
                    )
                )
                break

    def draw(self, screen):
        self.image = pygame.transform.rotate(self.original_img, self.angle)
        true_center_x = self.rect.centerx - int(self.image.get_width() / 2)
        true_center_y = self.rect.centery - int(self.image.get_height() / 2)
        screen.blit(
            self.image,
            (
                true_center_x,
                true_center_y,
            ),
        )
        pygame.draw.rect(screen, cfg.COLORS["RED"], self.rect, 1)
