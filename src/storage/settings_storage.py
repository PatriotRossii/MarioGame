from src.storage.abstract_storage import AbstractStorage


class SettingsStorage(AbstractStorage):
    defaults = {
        "tile_width": 50,
        "tile_height": 50,

        "width": 500,
        "height": 500,
    }

    @classmethod
    def create_singleton(cls):
        return SettingsStorage()
