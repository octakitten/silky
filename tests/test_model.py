import sys
import os
import pytest
# Add the parent directory to the system path
from silky import Model as Mdl

@pytest.fixture
def model():
    return Mdl.ferret()

def model2():
    return Mdl.hamster()

def init_params():
    return (
        256,
        256,
        12,
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

def test_hamster_model_initialization():
    assert model2 is not None
    assert isinstance(model2, Model.hamster)
    params = init_params()
    model2.create(params[0], params[1], params[2], params[3], params[4], params[5])
    assert model2.width == params[0]
    assert model2.height == params[1]
    assert model2.depth == params[2]
    assert model2.bounds == params[3]
    assert model2.num_controls == params[4]
    assert model2.num_sensations == params[5]
    assert model2.controls.len() == params[4]
    assert model2.thresholds_pos.len() == params[4]
    assert model2.thresholds_neg.len() == params[4]
    assert model2.thresholds_pos[0,0] <= params[3]
    assert model2.thresholds_neg[0,0] >= -params[3]
    assert model2.sensations.len() == params[5]
    assert model2.layers.len() == 62
    assert model2.layers[0].shape == (params[0], params[1], params[2])
    assert model2.layers[7].shape == (params[0], params[1], params[2])
    assert model2.layers[59].shape == (params[0], params[1], params[2])
    assert model2.layers[0][0, 0, 0] == 0
    assert model2.layers[4][0, 0, 0] == 0
    assert model2.layers[43][0, 0, 0] == 0
    guess = model2.update(torch.ones((params[0], params[1]), device=model2.device))
    assert model2.layers.len() == 62
    assert model2.layers[0].shape == (params[0], params[1], params[2])
    assert model2.layers[6].shape == (params[0], params[1], params[2])
    assert model2.layers[43].shape == (params[0], params[1], params[2])
    answer = torch.ones(torch.shape(guess), device=model2.device)
    model2.backprop(guess, answer)
    assert model2.layers.len() == 62
    assert model2.layers[0].shape == (params[0], params[1], params[2])
    assert model2.layers[5].shape == (params[0], params[1], params[2])
    assert model2.layers[52].shape == (params[0], params[1], params[2])
