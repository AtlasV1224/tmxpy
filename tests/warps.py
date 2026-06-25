from pathlib import Path
from .common import MAP_PATH

from src.tmxpy import TMXpy, convertMapNameToFile
#from tmxpy import TMXpy
import json

def get_warps(name: str) -> list[dict]:
    if name.__contains__('VolcanoEntrance'):
        return []
    tmx = TMXpy(
        [Path(MAP_PATH)],
        path=Path.joinpath(Path(MAP_PATH), name + ".tmx"))
    
    return tmx.parseWarps()

def recursive_get_warps(name: str, source: dict = {
    "map_x": 0,
    "map_y": 0,
    "destination": "Farm",
    "dest_x": 0,
    "dest_y": 0,
}, warps: list[dict] = [], depth: int = 0) -> list[dict]:
    for warp in get_warps(convertMapNameToFile(name)):
        if warp not in warps and warp['destination'] != source['destination'] \
                and warp['map_x'] != source['map_x'] and warp['map_y'] != source['map_y']:
            print(f'Handling warp {warp} at depth {depth}')
            # if depth > 25:
            #     return warps

            warps.append(warp)
            
            recursive_get_warps(warp['destination'], warp, warps, depth + 1)

    return warps

# for x in ['Farm', 'Island_W']:
for x in ['Island_W']:
    w = recursive_get_warps(x)
    with open(Path("tests") / f"warps-{x}.json", 'w') as f:
        json.dump(w, f, indent=4)
        print(f'Wrote {len(w)} warps to tests\\warps-{x}.json')
        