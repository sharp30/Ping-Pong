import threading 
import config
import time 
import random
class Ball:
    sign = '0'
    def __init__(self,players):
        self.loc = [config.GAME_SIZE[0]//2,config.GAME_SIZE[1]//2]
        self.direction = [random.choice(range(5)),self.loc[0]]#random something
        self.speed = random.choice([-1,1])
        self.players = players   
        self.th = threading.Thread(target=self.move, args=())   

    #when hitting an object (player,wall)
    def hit(self):
        if self.direction[0] != 0:
            m = -1 / self.direction[0]
        b = self.loc[0] - m*self.loc[1]#TODO:should be more impressive   
        if self.loc[1] <=1  or self.loc[1] >= config.GAME_SIZE[1]-1: #change direction
            self.speed *= -1
        self.direction = [m,b]

    #set next step
    def move(self):
        #check if some thing was hit
        #check if there was a goal
        cond = False
        while not ( self.loc[1] == 0 or self.loc[1] == config.GAME_SIZE[1]-1) or self.is_hit(): # while not making point
            if self.is_hit() and not cond:
                self.hit()
                
            cond = False

            col = self.loc[1] + self.speed if self.direction[0] != 0 else 2*self.speed
            row = self.direction[0] *col + self.direction[1]
            if row >= 0 and col >=0 and row <= config.GAME_SIZE[0] and col <= config.GAME_SIZE[1]:
                self.loc = [int(row),int(col)]
            else:
                self.hit()
                cond = True
                
            time.sleep(0.15)

            #TODO:wait for a

    #is ball in location
    def is_here(self,location):
        return Ball.sign if self.loc == location else None 

    #is ball hitting something
    def is_hit(self):
        if self.players[0].is_here(self.loc) != None or self.players[1].is_here(self.loc) != None:
            return True

        if self.loc[0] == 0 or self.loc[0] +1 == config.GAME_SIZE[0]:
            return True
        
        return False
    
    def start_thread(self):
        self.th.start()
        return self.th
