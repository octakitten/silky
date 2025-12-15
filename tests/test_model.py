import sys
import os
import pytest
import silky
from silky import model as Mdl

def make_model():
    return Mdl.ferret()

def make_model2():
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

def test_ferret_model_initialization():
    model = Mdl.ferret()
    assert model is not None
    #assert isinstance(model, Mdl.ferret())
    params = init_params()
    model.create(params)
    assert model.width == params[0]
    assert model.height == params[1]
    assert model.depth == params[2]
    assert model.bounds == params[3]
    assert model.num_controls == params[4]
    assert model.num_sensations == params[5]
    assert len(model.controls) == params[4]
    assert len(model.thresholds_pos) == params[4]
    assert len(model.thresholds_neg) == params[4]
    assert model.thresholds_pos[0,0] <= params[3]
    assert model.thresholds_neg[0,0] >= -params[3]
    assert len(model.sensations) == params[5]
    assert len(model.layers) == 61
    assert model.layers[0].shape == (params[0], params[1], params[2])
    assert model.layers[7].shape == (params[0], params[1], params[2])
    assert model.layers[59].shape == (params[0], params[1], params[2])
    assert len(model.firing) == 8
    assert model.layers[0][0, 0, 0] == 0
    assert model.layers[4][0, 0, 0] == 0
    assert model.layers[43][0, 0, 0] == 0
    return

def test_hamster_model_initialization():
    model2 = Mdl.hamster()
    assert model2 is not None
    #assert isinstance(model2, Mdl.hamster())
    params = init_params()
    model2.create(params)
    assert model2.width == params[0]
    assert model2.height == params[1]
    assert model2.depth == params[2]
    assert model2.bounds == params[3]
    assert model2.num_controls == params[4]
    assert model2.num_sensations == params[5]
    assert len(model2.controls) == params[4]
    assert len(model2.control_thresholds_pos) == params[4]
    assert len(model2.control_thresholds_neg) == params[4]
    assert model2.control_thresholds_pos[0,0] <= params[3]
    assert model2.control_thresholds_neg[0,0] >= -params[3]
    assert len(model2.sensations) == params[5]
    assert len(model2.layers) == 61
    assert model2.layers[0].shape == (params[0], params[1], params[2])
    assert model2.layers[7].shape == (params[0], params[1], params[2])
    assert model2.layers[59].shape == (params[0], params[1], params[2])
    assert model2.layers[0][0, 0, 0] == 0
    assert model2.layers[4][0, 0, 0] == 0
    assert model2.layers[43][0, 0, 0] != 0
    guess = model2.update(torch.ones((params[0], params[1]), device=model2.device))
    assert len(model2.layers) == 61
    assert model2.layers[0].shape == (params[0], params[1], params[2])
    assert model2.layers[6].shape == (params[0], params[1], params[2])
    assert model2.layers[43].shape == (params[0], params[1], params[2])
    answer = torch.ones(torch.shape(guess), device=model2.device)
    model2.backprop(guess, answer)
    assert len(model2.layers) == 61
    assert model2.layers[0].shape == (params[0], params[1], params[2])
    assert model2.layers[5].shape == (params[0], params[1], params[2])
    assert model2.layers[52].shape == (params[0], params[1], params[2])
