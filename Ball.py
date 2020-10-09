import config
class Ball:
    sign = '0'
    def __init__(self,players):
        self.loc = [10,10]
        self.direction = [0 ]#random something
        self.speed = 1 #TODO
        self.players = players      
    
    
    def __init__(self,start_loc,dir,speed):
        self.loc = start_loc
        self.direction = dir #random something
        self.speed = speed #TODO

    #when hitting an object (player,wall)
    def hit(self):
        m = -1 *self.direction[0]
        b = self.loc[1] - m*self.loc[0]#should be more impressive
        self.direction = [b,m]

    #set next step
    def move(self):
        #check if some thing was hit
        #check if there was a goal
        while not (loc[0] == 0 or loc[1] == config.GAME_SIZE[1]): # while not making point
            if is_hit():
                hit()
            else:
                x =  self.loc[0] + self.speed
                y =  self.direction[0] * x + self.direction[1]
            self.loc = [x,y]
            #TODO:wait for a

    #is ball in location
    def is_here(self,location):
        return Ball.sign if self.loc == location else None 

    #is ball hitting something
    def is_hit(self):
        if self.players[0].is_here(loc) != None or self.players[1].is_here() != None:
            return True

        #TODO:check sides
        for i in range(loc):
            if loc[i] == 0 or loc[i] +1 == config.GAME_SIZE[i]:
                return True
        
        return False