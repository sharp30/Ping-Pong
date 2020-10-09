import config
SIDES = {True : ['i','l'],False : ['w','l']}
class Player:
    PLAYER_SIZE = 5
    sign = '8'
    def __init__(self,player_side):
        self.loc = [0,0]
        self.len = PLAYER_SIZE
        self.side = player_side #right or left

    def move(self):
        while(True):
            #TODO: on key and not input
            inp = input()
            while(inp not in SIDES[self.side]):
                inp = input()
            if SIDES[self.side][0] == inp:
                if not self.loc[0] +5 > config.GAME_SIZE[0]:
                    self.loc[0] +=1
            else:
                if not self.loc[0] ==0:
                    self.loc[0] -=1
            

    
    #is player in location - return player's sign
    def is_here(self,loc):
        options = [[loc[0],loc[1] + i] for i in range(Player.PLAYER_SIZE)]
        return Player.sign if loc in options else None


    