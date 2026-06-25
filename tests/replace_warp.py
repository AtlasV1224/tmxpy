from pathlib import Path
from .common import MAP_PATH

from src.tmxpy import TMXpy, convertMapNameToFile
#from tmxpy import TMXpy
import json

# for x in ['Farm', 'Island_W']:
for x in ['Farm']:
    tmx = TMXpy(
        [Path(MAP_PATH)],
        path=Path.joinpath(Path(MAP_PATH), x + ".tmx"))
    
    tmx.replace_warp(0, {
        "map_x": 23,
        "map_y": 17,
        "destination": "Town",
        "dest_x": 10,
        "dest_y": 8,
    })

    tmx.save(Path("tests") / f"{x}-warp-replaced.tmx")
        


        