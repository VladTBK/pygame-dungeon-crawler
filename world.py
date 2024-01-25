from config import Config

cfg = Config()


class World:
    def __init__(self):
        self.map_tiles = []

    def process_data(self, data, tile_list):
        self.level_length = len(data)

        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                image = tile_list["idle"][tile]
                image_rect = image.get_rect()
                image_x = x * cfg.TILE_SIZE
                image_y = y * cfg.TILE_SIZE
                image_rect.center = (image_x, image_y)
                tile_data = [image, image_rect, image_x, image_y]

                if tile >= 0:
                    self.map_tiles.append(tile_data)

    def update(self, screen_scroll):
        for tile in self.map_tiles:
            tile[2] += screen_scroll[0]
            tile[3] += screen_scroll[1]
            tile[1].center = (tile[2], tile[3])

    def draw(self, screen):
        for tile in self.map_tiles:
            screen.blit(tile[0], tile[1])
