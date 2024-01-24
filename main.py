import pygame
from config import Config
from player import Player

pygame.init()
cfg = Config()
screen = pygame.display.set_mode((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
pygame.display.set_caption(cfg.GAME_NAME)

clock = pygame.time.Clock()

cfg.build_animations_list(
    "elf-m", "elf-f", "dwarf-m", "dwarf-f", "doc", "goblin", "chort"
)
player_imgs = cfg.get_images("goblin")
player = Player(100, 100, player_imgs)


def move_player(key):
    screen.fill(cfg.COLORS["BG"])
    dx = 0
    dy = 0
    player.state = "idle"
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

    if dx != 0 or dy != 0:
        player.state = "run"

    player.move(dx, dy)
    player.update()
    player.draw(screen)


def main():
    running = True
    while running:
        clock.tick(cfg.FPS)
        curr_key = pygame.key.get_pressed()
        move_player(curr_key)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        pygame.display.update()


main()
pygame.quit()
