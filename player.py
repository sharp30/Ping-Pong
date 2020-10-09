
class Player:
    PLAYER_SIZE = 5
    sign = '8'
    def __init__(self,player_side):
        self.loc = [0,0]
        self.len = PLAYER_SIZE
        self.side = player_side #right or left

    def move(self):
        while(True):
            #get input  
            #set location
            pass
    
    #is player in location - return player's sign
    def is_here(self,loc):
        options = [[loc[0],loc[1] + i] for i in range(Player.PLAYER_SIZE)]
        return Player.sign if loc in options else None


    