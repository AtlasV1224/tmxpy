from .common import *
from src.tmxpy import TMXpy, convertMapNameToFile
from pathlib import Path

tmx = TMXpy(
    [Path(MAP_PATH)],
    path=Path.joinpath(Path(MAP_PATH), "Farm.tmx")
)

tmx.generateMapPropertiesDict()
tmx.properties['asdf'] = 'ghjk'

tmx.save(Path("tests") / "Farm-properties-changed.tmx")