import numpy as np
import torch
import sys
import os
#from pathlib import Path

#print(sys.path)
#sys.path.insert(0, str(Path(__file__).parent.parent.parent))
#print(sys.path)

from ..models.d8a4gs import d8a4gs
from ..models.d16a1gs import d16a1gs
from ..utilities.screen import screen
from ..models.camel import camel
from ..models.horse import horse
from ..utilities.game import find_food_01
from ..utilities.game import find_food_02
from ..routines.grizzlybear_routine import grizzlybear_routine
from ..routines.horse_routine import horse_routine
from ..models.general import general
from ..models.general_dev2 import general_dev2
from ..utilities.game import find_food_03
from ..games.forest import forest
from ..routines import iteration

'''
def test001():
    model01 = d8a4gs()
    for i in range(100):
        input_image_fake = np.random.randint(0, 255, (256,256))
        next_action = model01.update(input_image_fake)
        print(next_action)

def test002():
    model02 = d16a1gs()
    a, b = 50, 50
    w, h = 255, 255
    for i in range(3):
        input_image_real = screen.snap_desktop(a, b, w, h)
        next_action = model02.update(input_image_real)
        if next_action == 2:
            print(next_action)
            a += 1
        elif next_action == 3:
            print(next_action)
            a -= 1
        else:
            print(next_action)

def test003():
    blob = camel()
    test_game = find_food_01(blob.width, blob.height)

    iter = 0
    max_iter = 1000

    prev = 0
    combo = 0
    max_combo = blob.width * 1.415
    
    while (test_game.victory() == False):
        act = blob.update(test_game.game_screen)
        print(act)
        if prev == act:
            combo += 1
        else:
            combo = 0
        
        if combo > max_combo:
            break

        prev = act

        x, y = test_game.blob_action(act)
        test_game.screen_update(x, y)

        iter += 1
        print(iter)
        if iter > max_iter:
            break
    
    if (test_game.victory() == True):
        print("victory!")
        print('Personality layer 1')
        print(blob.layer1_1_1)
        print('Personality layer 2')
        print(blob.layer1_1_2)
        print('Personality layer 3')
        print(blob.layer1_2_1)
        print('Personality layer 4')
        print(blob.layer1_2_2)
        print('Personality layer 5')
        print(blob.layer2_1_1)
        print('Personality layer 6')
        print(blob.layer2_1_2)
        print('Personality layer 7')
        print(blob.layer2_2_1)
        print('Personality layer 8')
        print(blob.layer2_2_2)
    else:
        print("defeat!")

def test004():
    the_game = find_food_01(255, 255)
    the_game.play_game()
    return

def test005():
    the_game = find_food_02(255, 255)
    the_game.play_game()
    return

def test006():
    winner = grizzlybear_routine.run_routine()
    print(winner)
    return

def test007():
    winner = horse_routine.run_routine()
    print(winner)
    return

def test008():
    model = horse()
    game = find_food_02(model)
    iters = 0
    while (game.play_game() == False):
        iters+=1
        print('game over! number of tries:')
        print(iters)
        print('restarting...')
    pers = game.blob.get_a_personality()
    print(pers)
    
def test009():
    model = general()
    model.create(255, 255, 100, 1024, 4, 2)
    game = find_food_02(model)
    iters = 0
    while (True):
        if (game.play_game() == False):
            iters+=1
            print('game over! number of tries:')
            print(iters)
            print('restarting...')
        else:
            break
        model.create(255, 255, 100, 1024, 4, 2)
        game = find_food_02(model)
    print('victory! it took this many iterations:')
    print(iters)
    print('saving to disk...')
    model.save(sys.path[0] + '/saved_models/latest.pth')
    
def test010():
    model = general()
    prev_model = 0
    model.create(255, 255, 255, 4, 4, 2)
    iters = 0
    first_attempt = True
    while (True):
        game = find_food_02(model)
        if (game.play_game() == False):
            iters+=1
            print('game over! number of tries:')
            print(iters)
            print('restarting...')
        else:
            break
        if (first_attempt):
            prev_model = model
            model.permute
        else: 
            if (model.min_dx + model.min_dy ) < (prev_model.min_dx + prev_model.min_dy):
                prev_model = model
                model.permute 
            else:
                model = prev_model
                model.permute
        first_attempt = False
    print('victory! it took this many iterations:')
    print(iters)
    print('saving to disk...')
    model.save(sys.path[0] + '/saved_models/')
    
'''
def test011():
    '''
    :Parameters:
    none
    :Returns:
    none
    :Comments:
    This function is a test for iterating on the general_dev model. This is the latest model as of 05-17-2024. The goal with iterating
    on the model is to develop a set of parameters that work to have the model solve the game it's currently playing.
    For this function we're making use of the game find_food_003, where the model is supposed to move a dot from a random 
    location on the screen and get it to the top left corner of the screen. This function will run the game until it's won,
    changing the models parameters each time it fails. The model's parameters will be saved to a file if it wins a game, otherwise
    this function will run indefinitely.
    '''
    model = general()
    prev_model = 0
    model.create(255, 255, 255, 1000, 4, 2)
    iters = 0
    first_attempt = True
    while (True):
        game = find_food_03(model)
        if (game.play_game() == False):
            iters+=1
            print('game over! number of tries:')
            print(iters)
            print('restarting...')
        else:
            break
        if (first_attempt):
            prev_model = model
            model.permute(2,1)
        else: 
            if (model.min_dx + model.min_dy ) < (prev_model.min_dx + prev_model.min_dy):
                prev_model = model(1,2)
                model.permute 
            else:
                model = prev_model
                model.permute(2,1)
        first_attempt = False
    print('victory! it took this many iterations:')
    print(iters)
    print('saving to disk...')
    model.save(sys.path[0] + '/saved_models/')

# run test for the in development general model
# test011()

def test012(dir):
    '''
    Parameters:
    none
    Returns:
    none
    Comments:
    Here we'll be testing a new game mode called forest. The game will have the model move a dot through a forest of dots until it 
    reaches the goal somewhere in the image. It receives positive input when it gets closer and negative when it gets further. Also,
    the model receives a powerful negative input when it gets too close to a tree. If it hits a tree, it dies.
    We'll be using the general_dev model for this.
    
    '''
    
    try:
        os.makedirs(sys.path[0] + dir + '/saved_models/')
        os.makedirs(sys.path[0] + dir + '/saved_models/in_progress')
        os.makedirs(sys.path[0] + dir + '/saved_models/victory')
    except:
        pass
    first_attempt = True
    model = general()
    prev_model = 0
    model.create(255, 255, 255, 1000, 4, 3)
    iters = 0
    game = forest(model)
    while (True):
        if (first_attempt == False):
            game.restart()
        if (game.play_game() == False):
            iters+=1
            print('game over! number of tries:')
            print(iters)
            print('restarting...')
        else:
            break
        if (first_attempt):
            prev_model = model
            model.permute(2,1)
        else: 
            if (model.min_dx + model.min_dy ) < (prev_model.min_dx + prev_model.min_dy):
                prev_model = model(1,2)
                model.permute 
            else:
                model = prev_model
                model.permute(2,1)
        first_attempt = False
        if (iters % 100 == 0):
            print('saving in progress...')
            model.save(sys.path[0] + dir + '/saved_models/in_progress')
    print('victory! it took this many iterations:')
    print(iters)
    print('saving to disk...')
    model.save(sys.path[0] + dir + '/saved_models/victory')
    
def test013(dir):
    first_attempt = True
    model = general()
    prev_model = 0
    if (os.path.exists(sys.path[0] + dir + '/saved_models/victory')):
        try:
            model.load(sys.path[0] + dir + '/saved_models/victory')
            print('loading model from disk...')
        except:
            print('unable to load a winning model')
            try:
                model.load(sys.path[0] + dir + '/saved_models/in_progress')
                print('loading in progress model from disk...')
            except:
                print('unable to load an in progress model')
                model.create(255, 255, 255, 1000, 4, 3)
                print('creatng a new model...')
    elif (os.path.exists(sys.path[0] + dir + '/saved_models/in_progress')):
        try:
            model.load(sys.path[0] + dir + '/saved_models/in_progress')
            print('loading model from disk...')
        except:
            print('unable to load an in progress model')
            model.create(255, 255, 255, 1000, 4, 3)
            print('creating a new model...')
    else:
        model.create(255, 255, 255, 1000, 4, 3)
        print('creatng a new model...')
    iters = 0
    game = forest(model)
    while (True):
        if (first_attempt == False):
            game.restart()
        if (game.play_game() == False):
            iters+=1
            print('game over! number of tries:')
            print(iters)
            print('restarting...')
        else:
            break
        if (first_attempt):
            prev_model = model
            model.permute(2,1)
        else: 
            if (model.min_dx + model.min_dy ) < (prev_model.min_dx + prev_model.min_dy):
                prev_model = model
                model.permute(1,2)
            else:
                model = prev_model
                model.permute(2,1)
        first_attempt = False
        if (iters % 100 == 0):
            print('saving in progress...')
            model.save(sys.path[0] + dir + '/saved_models/in_progress')
    print('victory! it took this many iterations:')
    print(iters)
    print('saving to disk...')
    model.save(sys.path[0] + dir + '/saved_models/victory')
    
def test014(dir):
    first_attempt = True
    model = general_dev2()
    prev_model = 0
    if (os.path.exists(sys.path[0] + dir + '/saved_models/victory')):
        try:
            model.load(sys.path[0] + dir + '/saved_models/victory')
            print('loading model from disk...')
        except:
            print('unable to load a winning model')
            try:
                model.load(sys.path[0] + dir + '/saved_models/in_progress')
                print('loading in progress model from disk...')
            except:
                print('unable to load an in progress model')
                model.create(255, 255, 255, 1000, 4, 3)
                print('creatng a new model...')
    elif (os.path.exists(sys.path[0] + dir + '/saved_models/in_progress')):
        try:
            model.load(sys.path[0] + dir + '/saved_models/in_progress')
            print('loading model from disk...')
        except:
            print('unable to load an in progress model')
            model.create(255, 255, 255, 1000, 4, 3)
            print('creating a new model...')
    else:
        model.create(255, 255, 255, 1000, 4, 3)
        print('creatng a new model...')
    iters = 0
    game = forest(model)
    while (True):
        if (first_attempt == False):
            game.restart()
        if (game.play_game() == False):
            iters+=1
            print('game over! number of tries:')
            print(iters)
            print('restarting...')
        else:
            break
        if (first_attempt):
            prev_model = model
            model.permute(2,1)
            first_attempt = False
        else: 
            if (model.min_dx + model.min_dy ) < (prev_model.min_dx + prev_model.min_dy):
                prev_model = model
            else:
                model = prev_model
        if (iters % 100 == 0):
            print('saving in progress...')
            model.save(sys.path[0] + dir + '/saved_models/in_progress')
        model.permute(1, 2)
    print('victory! it took this many iterations:')
    print(iters)
    print('saving to disk...')
    model.save(sys.path[0] + dir + '/saved_models/victory')
    
    return

def run_general_dev():
    iters = 0
    prev_iters = 10000
    path = sys.path[0] + '/general_dev/saved_models'
    vic_path = path + '/victory'
    prog_path = path + '/in_progress'
    model = general_dev2()
    stored_model = 0
    params = ( 255, 255, 255, 1000, 4, 3 )
    first_attempt = True
    while (True):
        iters = 0
        prev_model = 0
        if (os.path.exists(vic_path) & first_attempt):
            try:
                model.load(vic_path)
                print('loading model from disk... ')
            except:
                print('unable to load a winning model...')
                try:
                    model.load(prog_path)
                    print('loading an in-progress model from disk...')
                except:
                    print('unable to load an in-progress model')
                    print('creating a new model...')
                    model.create(params[0], params[1], params[2], params[3], params[4], params[5])
        elif (os.path.exists(prog_path) & first_attempt):
            try:
              model.load(prog_path)
              print('loading an in-progress model from disk...')
            except:
                print('unable to load an in-progress model')
                print('creating a new model')
                model.create(params[0], params[1], params[2], params[3], params[4], params[5])
        elif (first_attempt):
              print('creating a new model...')
              model.create(params[0], params[1], params[2], params[3], params[4], params[5])

        game = forest(model)
        first_game_attempt = True
        while (True):
              permute_degree = 2
              if (first_game_attempt == False):
                    game.restart()
              if (game.play_game() == False):
                    iters+=1
                    print('game over! number of attempts so far:')
                    print(iters)
                    print('restarting...')
              else:
                    break
              if (first_game_attempt):
                    prev_model = model
                    first_game_attempt = False
              else:
                    if (model.min_dx + model.min_dy ) < (prev_model.min_dx + prev_model.min_dy):
                        prev_model = model
                        permute_degree = 10
                    else:
                        model = prev_model
                        permute_degree = 5
              if (iters % 100 == 0):
                    print('saving in progress, this may take a moment... ...')
                    model.save(prog_path)
              model.permute(1, permute_degree)
        print('victory! a winning model was found! it took this many iterations:')
        print(iters)
        if (iters < prev_iters):
              prev_iters = iters
              model.save(vic_path)
        if (iters < 5):
            break
