class Paths:
    def __init__(self):
        ############### PLAYERS ###############
        self.PLAYER_MALE_ELF_IDLE_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/player-male-elf/idle"
        self.PLAYER_MALE_ELF_RUN_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/player-male-elf/run"
        self.PLAYER_FEMALE_ELF_IDLE_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/player-female-elf/idle"
        self.PLAYER_FEMALE_ELF_RUN_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/player-female-elf/run"
        self.PLAYER_MALE_DWARF_IDLE_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/player-male-dwarf/idle"
        self.PLAYER_MALE_DWARF_RUN_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/player-male-dwarf/run"
        self.PLAYER_FEMALE_DWARF_IDLE_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/player-female-dwarf/idle"
        self.PLAYER_FEMALE_DWARF_RUN_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/player-female-dwarf/run"

        ############### ENEMEYS ###############
        self.ENEMY_DOC_IDLE_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/enemy-doc/idle"
        self.ENEMY_DOC_RUN_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/enemy-doc/run"
        self.ENEMY_GOBLIN_IDLE_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/enemy-goblin/idle"
        self.ENEMY_GOBLIN_RUN_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/enemy-goblin/run"
        self.ENEMY_CHORT_IDLE_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/enemy-chort/idle"
        self.ENEMY_CHORT_RUN_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/enemy-chort/run"

        ############### WEAPONS ###############
        self.BOW_IDLE_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/weapons/bow/idle"
        self.BOW_LOAD_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/weapons/bow/load"
        self.ARROW_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/weapons/bow/arrow"

        ############### ITEMS ###############
        self.HEARTH_FULL_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/items/hearths/full"
        self.HEARTH_HALF_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/items/hearths/half"
        self.HEARTH_EMPTY_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/items/hearths/empty"

        ############### MAP ###############
        self.MAP_PATH = "/home/vlad/Desktop/projects/python-projects/game-projects/dungeon-crawler/assets/images/tiles"

        self.IMAGE_DICT = {
            "elf-m": {
                "idle": [self.PLAYER_MALE_ELF_IDLE_PATH, []],
                "run": [self.PLAYER_MALE_ELF_RUN_PATH, []],
            },
            "elf-f": {
                "idle": [self.PLAYER_FEMALE_ELF_IDLE_PATH, []],
                "run": [self.PLAYER_FEMALE_ELF_RUN_PATH, []],
            },
            "dwarf-m": {
                "idle": [self.PLAYER_MALE_DWARF_IDLE_PATH, []],
                "run": [self.PLAYER_MALE_DWARF_RUN_PATH, []],
            },
            "dwarf-f": {
                "idle": [self.PLAYER_FEMALE_DWARF_IDLE_PATH, []],
                "run": [self.PLAYER_FEMALE_DWARF_RUN_PATH, []],
            },
            "doc": {
                "idle": [self.ENEMY_DOC_IDLE_PATH, []],
                "run": [self.ENEMY_DOC_RUN_PATH, []],
            },
            "goblin": {
                "idle": [self.ENEMY_GOBLIN_IDLE_PATH, []],
                "run": [self.ENEMY_GOBLIN_RUN_PATH, []],
            },
            "chort": {
                "idle": [self.ENEMY_CHORT_IDLE_PATH, []],
                "run": [self.ENEMY_CHORT_RUN_PATH, []],
            },
            "bow": {
                "idle": [self.BOW_IDLE_PATH, []],
                "load": [self.BOW_LOAD_PATH, []],
            },
            "arrow": {
                "idle": [self.ARROW_PATH, []],
            },
            "hearth": {
                "full": [self.HEARTH_FULL_PATH, []],
                "half": [self.HEARTH_HALF_PATH, []],
                "empty": [self.HEARTH_EMPTY_PATH, []],
            },
            "map": {
                "idle": [self.MAP_PATH, []],
            },
        }
        self.player_list = "elf-m", "elf-f", "dwarf-m", "dwarf-f"
        self.mob_list = "doc", "goblin", "chort"
        self.weapon_list = "bow", "arrow"
        self.items_list = "hearth", "hearth"
        self.map = "map", "map"
