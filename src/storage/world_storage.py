import pygame

from src.storage.abstract_storage import AbstractStorage


class WorldStorage(AbstractStorage):
    defaults = {
        "all_sprites": pygame.sprite.Group(),

        "tiles_group": pygame.sprite.Group(),
        "borders_group": pygame.sprite.Group(),
        "player_group": pygame.sprite.Group(),

        "player": None,
    }

    @classmethod
    def create_singleton(cls):
        return WorldStorage()
