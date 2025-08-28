import sys
import os
#from pathlib import Path

#print(sys.path)
#sys.path.insert(0, str(Path(__file__).parent.parent.parent))
#print(sys.path)
from . import model as mdl
from . import forest
from . import game as gm

from silky import train as tr

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
    model = mdl.general()
    prev_model = 0
    model.create((255, 255, 255, 1000, 4, 2))
    iters = 0
    first_attempt = True
    while (True):
        game = gm.find_food_03(model)
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
    model = mdl.general()
    prev_model = 0
    model.create((255, 255, 255, 1000, 4, 3))
    iters = 0
    game = forest.forest(model)
    model = 0
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
    model = mdl.general()
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
                model.create((255, 255, 255, 1000, 4, 3))
                print('creatng a new model...')
    elif (os.path.exists(sys.path[0] + dir + '/saved_models/in_progress')):
        try:
            model.load(sys.path[0] + dir + '/saved_models/in_progress')
            print('loading model from disk...')
        except:
            print('unable to load an in progress model')
            model.create((255, 255, 255, 1000, 4, 3))
            print('creating a new model...')
    else:
        model.create((255, 255, 255, 1000, 4, 3))
        print('creatng a new model...')
    iters = 0
    game = forest.forest(model)
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
    model = mdl2.general_dev2()
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
                model.create((255, 255, 255, 1000, 4, 3))
                print('creatng a new model...')
    elif (os.path.exists(sys.path[0] + dir + '/saved_models/in_progress')):
        try:
            model.load(sys.path[0] + dir + '/saved_models/in_progress')
            print('loading model from disk...')
        except:
            print('unable to load an in progress model')
            model.create((255, 255, 255, 1000, 4, 3))
            print('creating a new model...')
    else:
        model.create((255, 255, 255, 1000, 4, 3))
        print('creatng a new model...')
    iters = 0
    game = forest.forest(model)
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

def run_ferret_forest():
    iters = 0
    prev_iters = 10000
    pth = os.getcwd() + '/ferret_forest'
    vic_path = pth + '/victory'
    prog_path = pth + '/in_progress'
    params = ( 255, 255, 20, 1000, 4, 3 )
    first_attempt = True
    high_score = 0
    high_score_attempt = 0
    high_score_is_victory = False
    attempt_num = 0
    while (True):
        iters = 0
        prev_mindx = 0
        prev_mindy = 0
        game = None
        if (os.path.exists(vic_path) & first_attempt):
            try:
                print('loading model from disk... ')
                game = forest.forest(params, path=vic_path)
            except:
                print('unable to load a winning model...')
                try:
                    game = forest.forest(params, path=prog_path)
                    print('loading an in-progress model from disk...')
                except:
                    print('unable to load an in-progress model')
                    print('creating a new model...')
                    game = forest.forest(params)
        elif (os.path.exists(prog_path) & first_attempt):
            try:
                game = forest.forest(params, path=prog_path)
                print('loading an in-progress model from disk...')
            except:
                print('unable to load an in-progress model')
                print('creating a new model')
                game = forest.forest(params)
        elif (first_attempt):
            print('creating a new model...')
            game = forest.forest(params)
        first_game_attempt = True
        while (True):
              attempt_num += 1
              permute_degree = 2
              if (first_game_attempt == False):
                    game.restart()
              if (game.play_game() == False):
                    iters+=1
                    print('game over! number of attempts so far:')
                    print(iters)
                    if (iters > high_score):
                        high_score = iters
                        high_score_attempt = attempt_num
                        print('new high score found!')
                        print(f"the score is: ", (high_score))
                        print(f"at attempt number: ", (high_score_attempt))
                        print("on a defeat.")
                    print('restarting...')
              else:
                    break
              if (first_game_attempt):
                    prev_mindx = game.blob.min_dx
                    prev_mindy = game.blob.min_dy
                    first_game_attempt = False
              else:
                    if (game.blob.min_dx + game.blob.min_dy ) < (prev_mindx + prev_mindy):
                        permute_degree = 10
                    else:
                        permute_degree = 5
              if (iters % 100 == 0):
                    print('saving in progress, this may take a moment... ...')
                    print(f"the current high score is ", (high_score))
                    print(f"from attempt number: ", (high_score_attempt))
                    game.blob.save(prog_path)
              game.blob.permute(1, permute_degree)
        print(f"victory! a winning model was found! it took this many iterations: ", (iters))
        if (high_score_is_victory == False):
            high_score = iters
            high_score_attempt = attempt_num
            print("new high score found!")
            print(f"the score is: ", (high_score))
            print(f"at attempt number: ", (high_score_attempt))
            print("on a victory!")
        elif (iters < high_score):
            high_score = iters
            high_score_attempt = attempt_num
            print("new high score found!")
            print(f"the score is: ", (high_score))
            print(f"at attempt number: ", (high_score_attempt))
            print("on a victory!")
        if (iters < prev_iters):
              prev_iters = iters
              game.blob.save(vic_path)
        if (iters < 5):
            break
    print("finished!")
    print(f"the high score is: ", (high_score))
    print(f"on attempt number: ", (high_score_attempt))
    if (high_score_is_victory):
        print("it was on a victory!")
    return high_score_attempt

def run_hamster():
    iters = 0
    prev_iters = 10000
    path = sys.path[0] + '/velvet/models'
    vic_path = path + '/victory'
    prog_path = path + '/in_progress'
    model = mdl.hamster()
    params = ( 100, 100, 16, 500, 4, 3 )
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
                    model.create(params)
        elif (os.path.exists(prog_path) & first_attempt):
            try:
              model.load(prog_path)
              print('loading an in-progress model from disk...')
            except:
                print('unable to load an in-progress model')
                print('creating a new model')
                model.create(params)
        elif (first_attempt):
              print('creating a new model...')
              model.create(params)

        game = forest.forest(type='hamster', model=model)
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
              model.permute(permute_degree)
        print('victory! a winning model was found! it took this many iterations:')
        print(iters)
        if (iters < prev_iters):
              prev_iters = iters
              model.save(vic_path)
        if (iters < 5):
            break
    return iters

def train_ferret():
    opts = tr.optionsobj("", None, "./ferrettest1/", 256, 256, 200, 50, 200, 2, 400)
    percent = 0.0
    while (percent < .95):
        tr.train(opts)
        percent = tr.test(opts)
    return

def train_hamster():
    opts = tr.optionsobj("", None, "./hamstertest1/", 64, 64, 10, 50, 200, 2, 10)
    percent = 0.0
    while (percent < .95):
        tr.train_hamster(opts)
        percent = tr.test_hamster(opts)
    return

def train_hamster_forest():
    total_iters = 0
    total_attempts = 0
    while (True):
        total_attempts += 1
        total_iters += run_hamster()
        if ((total_iters/total_attempts) < 5):
            break
    print("Consistency in output achieved! Average iterations per attempt is lower than 5!")
    return

def run_ferret_forest_tracked():
    total_iters = 0  # Track total iterations across all attempts
    high_score = 0   # Best number of steps survived
    high_score_iter = 0  # Which iteration achieved the high score
    prev_iters = 10000
    pth = os.getcwd() + '/ferret_forest'
    vic_path = pth + '/victory'
    prog_path = pth + '/in_progress'
    params = ( 255, 255, 255, 1000, 4, 3 )
    first_attempt = True
    
    while (True):
        iters = 0
        prev_mindx = 0
        prev_mindy = 0
        game = None
        
        if (os.path.exists(vic_path) & first_attempt):
            try:
                print('loading model from disk... ')
                game = forest.forest(params, path=vic_path)
            except:
                print('unable to load a winning model...')
                try:
                    game = forest.forest(params, path=prog_path)
                    print('loading an in-progress model from disk...')
                except:
                    print('unable to load an in-progress model')
                    print('creating a new model...')
                    game = forest.forest(params)
        elif (os.path.exists(prog_path) & first_attempt):
            try:
                game = forest.forest(params, path=prog_path)
                print('loading an in-progress model from disk...')
            except:
                print('unable to load an in-progress model')
                print('creating a new model')
                game = forest.forest(params)
        elif (first_attempt):
            print('creating a new model...')
            game = forest.forest(params)
            
        first_game_attempt = True
        while (True):
            permute_degree = 2
            if (first_game_attempt == False):
                game.restart()
                
            # Play the game and track steps
            steps = 0
            game_result = game.play_game()
            if hasattr(game, 'steps'):
                steps = game.steps
            
            total_iters += 1
            
            if game_result == False:
                iters += 1
                print(f'Iteration {total_iters}: Lost after {steps} steps')
                
                # Update high score if this attempt was better
                if steps > high_score:
                    high_score = steps
                    high_score_iter = total_iters
                    print(f'New high score! Steps: {high_score} (Iteration: {high_score_iter})')
                
                print('restarting...')
            else:
                print(f'Iteration {total_iters}: Won after {steps} steps!')
                if steps > high_score:
                    high_score = steps
                    high_score_iter = total_iters
                break
                
            if (first_game_attempt):
                prev_mindx = game.blob.min_dx
                prev_mindy = game.blob.min_dy
                first_game_attempt = False
            else:
                if (game.blob.min_dx + game.blob.min_dy ) < (prev_mindx + prev_mindy):
                    permute_degree = 10
                else:
                    permute_degree = 5
                    
            if (iters % 100 == 0):
                print('saving in progress, this may take a moment... ...')
                print(f'Current stats - High Score: {high_score} (from iteration {high_score_iter})')
                game.blob.save(prog_path)
                
            game.blob.permute(1, permute_degree)
            
        print('victory! a winning model was found!')
        print(f'Final Statistics:')
        print(f'Total iterations: {total_iters}')
        print(f'Best performance: {high_score} steps (achieved on iteration {high_score_iter})')
        
        if (iters < prev_iters):
            prev_iters = iters
            game.blob.save(vic_path)
        if (iters < 5):
            break

def iterate_ferret_aliens():
    params = (640, 480, 20, 256, 6, 0)
    total_iters = 0
    high_score = 0
    high_turns = 0
    high_score_iter = 0
    pth = os.getcwd() + '/aliens'
    latest_path = pth + '/latest'
    best_path = pth + '/best'
    permute_degree = 2

    first_attempt = True
    turns = 0
    score = 0
    prev_turns = 0
    prev_score = 0
    done = False

    #mdl = silky.model.ferret()
    #while (!done):
        #if (os.path.exists(best_path) & first_attempt):
            #try:
