import sys
from pathlib import Path

#print(sys.path)
sys.path.insert(0, str(Path(__file__).parent))
#print(sys.path)

from silky import game
from silky import model

def test_find_food_02_initialization():
    test_w = 255
    test_h = 255
    m = ferret()
    g = find_food_02(m)
    assert g.width == test_w
    assert g.height == test_h
    return

test_find_food_02_initialization()
