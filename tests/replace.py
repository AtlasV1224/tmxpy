from .common import *
from src.tmxpy import TMXpy, convertMapNameToFile
from pathlib import Path


tmx = TMXpy(
    [Path(MAP_PATH)],
    path=Path.joinpath(Path(MAP_PATH), "Farm.tmx")
)

tmx.parseWarps()

tmx.setTile(23, 17, "129", layerName="Buildings")

print(tmx.warps)
tmx.replace_warp(0, {
    "map_x": 23,
    "map_y": 17,
    "destination": "Town",
    "dest_x": 10,
    "dest_y": 8,
})
print(tmx.warps)

# tmx.generateGIDDict()
# tmx.renderAllLayers().save("tests\\Farm-warp-tile-replaced.png")
tmx.save(Path("tests") / "Farm-warp-tile-replaced.tmx")
