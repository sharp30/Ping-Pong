class Ball:
    sign = '0'
    def __init__(self):
        self.loc = [10,10]
        self.direction = [0 ]#random something
        self.speed = 1 #TODO
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
        x =  self.loc[0] + self.speed
        y =  self.direction[0] * x + self.direction[1]
        self.loc = [x,y]

    def is_here(self,location):
        return Ball.sign if self.loc == location else None 

