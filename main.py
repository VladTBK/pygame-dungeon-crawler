import pygame
from config import Config
from player import Enemy, Player
from weapon import Weapon
from world import World

pygame.init()
cfg = Config()
screen = pygame.display.set_mode((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
pygame.display.set_caption(cfg.GAME_NAME)
font = pygame.font.Font(cfg.FONT[0], cfg.FONT[1])

clock = pygame.time.Clock()

cfg.build_animations_list(cfg.player_list)
cfg.build_animations_list(cfg.mob_list)
cfg.build_animations_list(cfg.weapon_list)
cfg.build_animations_list(cfg.items_list)
cfg.build_animations_list(cfg.map)

player_imgs = cfg.get_images("elf-m")
hearth_imgs = cfg.get_images("hearth")
goblin_imgs = cfg.get_images("goblin")
weapon_imgs = cfg.get_images("bow")
ammo_img = cfg.get_images("arrow")
map_imgs = cfg.get_images("map")

player = Player(100, 100, player_imgs, hearth_imgs)
goblin = Enemy(100, 100, goblin_imgs)


bow = Weapon(weapon_imgs, ammo_img)

# groups
arrow_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
enemy_group.add(goblin)
damage_text_group = pygame.sprite.Group()


screen_scroll = [0, 0]
# def draw_grid():
#     for x in range(30):
#         pygame.draw.line(
#             screen,
#             cfg.COLORS["WHITE"],
#             (x * cfg.TILE_SIZE, 0),
#             (x * cfg.TILE_SIZE, cfg.SCREEN_HEIGHT),
#         )
#         pygame.draw.line(
#             screen,
#             cfg.COLORS["WHITE"],
#             (0, x * cfg.TILE_SIZE),
#             (cfg.SCREEN_WIDTH, x * cfg.TILE_SIZE),
#         )


def main_loop(key):
    dx = 0
    dy = 0
    player.state = "idle"
    if key[pygame.K_w]:
        dy -= cfg.PLAYER_SPEED
    if key[pygame.K_s]:
        dy += cfg.PLAYER_SPEED
    if key[pygame.K_a]:
        player.flip = True
        dx -= cfg.PLAYER_SPEED
    if key[pygame.K_d]:
        player.flip = False
        dx += cfg.PLAYER_SPEED

    if key[pygame.K_q]:
        pygame.quit()

    if dx != 0 or dy != 0:
        player.state = "run"
        bow.fire_cd = 1000
    else:
        bow.fire_cd = 500

    map.draw(screen)
    screen_scroll = player.move(dx, dy)
    map.update(screen_scroll)
    player.update()
    player.draw(screen)
    arrow = bow.update(player)
    if arrow:
        arrow_group.add(arrow)
    bow.draw(screen)

    for enemy in enemy_group:
        enemy.update()
        enemy.draw(screen)
    for arrow in arrow_group:
        arrow.draw(screen)
        arrow.update(enemy_group, damage_text_group, font)

    damage_text_group.update()
    damage_text_group.draw(screen)


map_layout = [
    [13, 13, 13, 13, 14],
    [17, 0, 1, 2, 18],
    [17, 3, 6, 8, 18],
    [17, 2, 5, 2, 18],
    [17, 2, 5, 2, 18],
    [22, 22, 22, 22, 24],
]
map = World()
map.process_data(map_layout, map_imgs)


def main():
    running = True
    while running:
        clock.tick(cfg.FPS)
        screen.fill(cfg.COLORS["BG"])
        curr_key = pygame.key.get_pressed()
        # draw_grid()
        main_loop(curr_key)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        pygame.display.update()


main()
pygame.quit()
