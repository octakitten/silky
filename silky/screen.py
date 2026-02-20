from PIL import Image
from PIL import ImageGrab
from PIL import ImageOps
from PIL import features
from io import BytesIO
import numpy as np
import torch
import subprocess


def snap_desktop(a, b, w, h):
    # a,b = top left corner of the box
    # w,h = width and height of the box
    # returns a numpy array
    val = -1
    

    # this needs to be set to True but we're leaving it on False for now
    if(features.check_feature("xcb") == False):
        # if xcb is enabled, use ffmpeg with xcbgrab to take a screenshot of the desktop
        command = [
        'ffmpeg',
        '-s', f'{w}x{h}',
        '-framerate', '25',
        '-f', 'x11grab',
        '-i', ':0.0+{a},{b}',
        '-vframes', '1',
        'snap.png'
        ]
        subprocess.run(command)
        val = np.array(Image.open('snap.png'))
    else:
        # otherwise, use PIL's ImageGrab to take a screenshot of the desktop, 
        # which will probably default to gnome-screenshot
        im = ImageGrab.grab(bbox =(a, b, a+w, b+h))
        val = np.array(im).astype(np.uint8)[:,:,0]
    
    return val

def save(val, name):
    # save a numpy array or torch tensor as a png image
    # name should not have an extension
    if (isinstance(val, np.ndarray) == True):
        img = Image.fromarray(val)
        img.save(name, 'PNG')
        return 1
    elif (torch.is_tensor(val) == True):
        img = Image.fromarray(val.cpu().numpy())
        grey = img.convert('L')
        grey.save(name, 'PNG')
        return 2
    else:
        return -1

def convert_greyscale(val):
    # convert an image to greyscale
    # then convert the greyscale image to a pytorch tensor
    # and return the tensor
    if (isinstance(val, np.ndarray) == True):
        print('found an ndarray')
        img = Image.fromarray(val)
        grey = img.convert('L')
        out = torch.from_numpy(np.array(grey)).to(torch.float32)
    elif (torch.is_tensor(val) == True):
        print('found a torch tensor')
        grey = val.convert('L')
        out = torch.from_numpy(np.array(grey)).to(torch.float32)
    elif (isinstance(val, BytesIO) == True):
        print('found an image buffer')
        grey = Image.new('L', (1,1), 'red')
        grey.save(val, format='png')
        out = torch.from_numpy(np.array(grey)).to(torch.float32)
    else:
        print('found an image')
        img = Image.open(val)
        grey = img.convert('L')
        out = torch.from_numpy(np.array(grey)).to(torch.float32)
    pad = torch.zeros(640, 640, dtype=torch.float32)
    pad[:,480] = out
    return pad



