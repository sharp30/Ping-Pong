import config
import threading 

SIDES = {True : ['i','l'],False : ['w','l']}

class Player:
    sign = '8'
    def __init__(self,player_side):
        self.loc = [0,0]
        self.len = config.PLAYER_SIZE
        self.side = player_side #right or left
        self.th = threading.Thread(target=self.move, args=())   
        self.stopped = False

    def move(self):
        while(not self.stopped):
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
        options = [[self.loc[0] +i,self.loc[1]] for i in range(config.PLAYER_SIZE)]
        return Player.sign if loc in options else None

    def start_thread(self):
        self.th.start()
        return self.th
    
    def kill_thread(self):
        self.stopped = True
    