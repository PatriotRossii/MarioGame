from src.storage.images_storage import ImagesStorage
from src.storage.settings_storage import SettingsStorage
from src.storage.world_storage import WorldStorage

images_storage = ImagesStorage.singleton()
settings_storage = SettingsStorage.singleton()
world_storage = WorldStorage.singleton()

storages = [images_storage, settings_storage, world_storage]

for storage in storages:
    for key in storage.defaults:
        globals()[key] = storage.defaults[key]
