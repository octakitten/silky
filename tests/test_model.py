import sys
import os
import pytest
# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model import Model

@pytest.fixture
def model():
    return Model.ferret()

def init_params():
    return (
        256,
        256,
        10,
        256,
        6,
        2
        )

def test_ferret_model_initialization(model):
    assert model is not None
    assert isinstance(model, Model.ferret)
    params = init_params()
    model.create(params[0], params[1], params[2], params[3], params[4], params[5])
    assert model.width == params[0]
    assert model.height == params[1]
    assert model.depth == params[2]
    assert model.bounds == params[3]
    assert model.num_controls == params[4]
    assert model.num_sensations == params[5]
    assert model.controls.len() == params[4]
    assert model.thresholds_pos.len() == params[4]
    assert model.thresholds_neg.len() == params[4]
    assert model.thresholds_pos[0,0] <= params[3]
    assert model.thresholds_neg[0,0] >= -params[3]
    assert model.sensations.len() == params[5]
    assert model.layers.len() == 62
    assert model.layers[0].shape == (params[0], params[1], params[2])
    assert model.layers[7].shape == (params[0], params[1], params[2])
    assert model.layers[59].shape == (params[0], params[1], params[2])
    assert model.firing.len() == 8
    assert model.layers[0][0, 0, 0] == 0
    assert model.layers[4][0, 0, 0] == 0
    assert model.layers[43][0, 0, 0] == 0
    return
