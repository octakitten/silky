import pytest
import silky
from silky import aliens as alns

#def test_aliens():

def test_player_class():
    player = alns.Player(all)
    assert player is alns.Player

    
    alns.iterate()
    assert alns.high_score > 0
    assert alns.high_turns > 0
