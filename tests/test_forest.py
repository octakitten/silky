import sys
import os
import pytest
import silky
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from silky import Forest


@pytest.fixture
def model_params():
    return (
            256,
            256,
            50,
            100,
            6,
            2)

@pytest.fixture
def forest(model_params):
    return Forest(model_params())

def test_forest_init(forest(model_params)):
    assert forest.blob == type(mdl.ferret)
    assert forest.victory_x >= 0
    assert forest.victory_y >= 0
    assert forest.victory_x <= model_params[0]
    assert forest.victory_y <= model_params[1]
    assert forest.starting_x >= 0
    assert forest.starting_y >= 0
    assert forest.starting_x <= model_params[0]
    assert forest.starting_y <= model_params[1]
    assert forest.width == model_params[0]
    assert forest.height == model_params[1]

def test_forest_play_game(forest(model_params)):
    assert forest.play_game() is Bool
