from player.Player import *

class InactivePlayer(Player):
    
    def __init__(self, location, randomStart, mazeSize):
        Player.__init__(self,location, randomStart, mazeSize) 
        self._name = "InactivePlayer"
    
    # An InactivePlayer doesn't play (it is inactive)
    def plays(self):
        return False                       