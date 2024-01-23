import pygame
from config import Config as cfg
from player import Player

pygame.init()

screen = pygame.display.set_mode((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
pygame.display.set_caption(cfg.GAME_NAME)

clock = pygame.time.Clock()

move_up, move_down, move_right, move_left = False, False, False, False
player = Player(100, 100)


def move_player(key):
    screen.fill(cfg.COLORS["BG"])
    dx = 0
    dy = 0

    if key[pygame.K_w]:
        dy -= cfg.SPEED1
    if key[pygame.K_s]:
        dy += cfg.SPEED1
    if key[pygame.K_a]:
        dx -= cfg.SPEED1
    if key[pygame.K_d]:
        dx += cfg.SPEED1

    player.move(dx, dy)


def main():
    running = True
    while running:
        clock.tick(cfg.FPS)
        curr_key = pygame.key.get_pressed()
        move_player(curr_key)
        player.draw(screen)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        pygame.display.update()


main()
pygame.quit()
