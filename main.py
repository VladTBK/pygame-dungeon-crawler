import pygame
from config import Config
from player import Player

pygame.init()
cfg = Config()
screen = pygame.display.set_mode((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
pygame.display.set_caption(cfg.GAME_NAME)

clock = pygame.time.Clock()

player_idle_imgs = cfg.load_imgs(cfg.PLAYER_MALE_ELF_IDLE_PATH)
player = Player(100, 100, player_idle_imgs[0])


def move_player(key):
    screen.fill(cfg.COLORS["BG"])
    dx = 0
    dy = 0

    if key[pygame.K_w]:
        dy -= cfg.SPEED1
    if key[pygame.K_s]:
        dy += cfg.SPEED1
    if key[pygame.K_a]:
        player.flip = True
        dx -= cfg.SPEED1
    if key[pygame.K_d]:
        player.flip = False
        dx += cfg.SPEED1
    if key[pygame.K_q]:
        pygame.quit()

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
