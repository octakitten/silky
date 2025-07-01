import sys
import os
import pytest
import silky
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from silky import forest


def model_params():
    return (
            256,
            256,
            50,
            100,
            6,
            3)

def test_forest_init():
    game = forest.forest(model_params())
    #assert game.blob == type(mdl.ferret)
    assert game.victory_x >= 0
    assert game.victory_y >= 0
    assert game.victory_x <= model_params()[0]
    assert game.victory_y <= model_params()[1]
    assert game.starting_x >= 0
    assert game.starting_y >= 0
    assert game.starting_x <= model_params()[0]
    assert game.starting_y <= model_params()[1]
    assert game.width == model_params()[0]
    assert game.height == model_params()[1]
    assert game.play_game() is Bool
