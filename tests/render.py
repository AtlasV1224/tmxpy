#import tmxpy does not work
import sys, random, time, argparse
from pathlib import Path

#sys.path.append('..')

from src.tmxpy import TMXpy#, hello#
#from tmxpy import TMXpy

#parser = argparse.ArgumentParser(description='Render a TMX file.')
#parser.add_argument('map', metavar='map', type=str, nargs=1, help='The path to the TMX file to render.')

from .common import MAP_PATH

def farm():
    tmx = TMXpy(
        [Path(MAP_PATH)],
        path=Path("tests") / "Farm.tmx")
                
    #print(tmx.__dict__)

    tmx.generateGIDDict()

    # random.seed = time.time()
    # randomlySelectedTile = random.choice(list(tmx.tiles.keys()))
    # print(randomlySelectedTile)

    #tmx.renderLayer(1).save("tests\\render.png")
    tmx.renderAllLayers().save(Path("tests") / "render-farm.png")


def render(name: str):
    tmx = TMXpy(
        [Path(MAP_PATH)],
        path=Path.joinpath(Path(MAP_PATH), name + ".tmx"))
                
    #print(tmx.__dict__)

    tmx.generateGIDDict()

    # random.seed = time.time()
    # randomlySelectedTile = random.choice(list(tmx.tiles.keys()))
    # print(randomlySelectedTile)

    #tmx.renderLayer(1).save("tests\\render.png")
    tmx.renderAllLayers(blocked=['Paths']).save(Path("tests") / f"render-{name}.png")

#for x in ['AnimalShop', 'Beach', 'Darkroom', 'Desert', 'Town', 'Farm', 'FarmCave']:
for x in ['Farm']:
    render(x)


