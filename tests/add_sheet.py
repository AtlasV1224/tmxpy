from .common import *
from src.tmxpy import TMXpy, convertMapNameToFile
from pathlib import Path

tmx = TMXpy(
    [Path(MAP_PATH)],
    path=Path.joinpath(Path(MAP_PATH), "Farm.tmx")
)

tmx.generateGIDDict()
tmx.addTilesheet("spring_beach", "Beach", {})

tmx.generateGIDDict()
tmx.setTile(23, 17, str(tmx.maxGID - 10), layerName="Buildings")

tmx.save(Path("tests") / "Farm-added-tile-replaced.tmx")
tmx.renderAllLayers().save(Path("tests") / "Farm-added-tile-replaced.png")