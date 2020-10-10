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
        m = self.direction[0]
        if self.direction[0] != 0:
            m = -1 / self.direction[0]
        b = self.loc[0] - m*self.loc[1]#TODO:should be more impressive 

        if self.loc[1] <=1 or self.loc[1] >= config.GAME_SIZE[1]-2: #change direction
            self.speed *= -1
        self.direction = [m,b]

    #set next step
    def move(self):
        #check if some thing was hit
        #check if there was a goal
        cond = False
        while not (self.loc[1] <= 0 or self.loc[1] >= config.GAME_SIZE[1]-1) or self.is_hit():# while not making point
            if self.is_hit():
                self.hit()

            #move ball
            col = self.loc[1] + (self.speed if self.direction[0] != 0 else 2*self.speed)
            row = self.direction[0] *col + self.direction[1]

            row_ok = row >= 0 and row < config.GAME_SIZE[0]
            col_ok = col >= 0 and col < config.GAME_SIZE[1] 

            if col_ok and row_ok:
                self.loc = [int(row),int(col)]
            elif col_ok:
                self.hit()
            else: #col is the problem
                maxx,minn = max(col,self.loc[1]),min(col,self.loc[1])
                for i in range(minn,maxx+1):
                    if i == 0 or i == config.GAME_SIZE[1]-1:
                        if self.is_hit2([int(row),i]):
                           self.hit()
                        else:
                            self.loc = [int(row),int(col)] 
                        break
            time.sleep(0.15)

    #is ball in location
    def is_here(self,location):
        return Ball.sign if self.loc == location else None 

    #is ball hitting something
    def is_hit(self):
        return self.is_hit2(self.loc)
    
    def is_hit2(self,loc):
        if self.players[0].is_here(loc) != None or self.players[1].is_here(loc) != None:
            return True

        if (loc[0] == 0 or loc[0] +1 == config.GAME_SIZE[0]) and self.direction[0] != 0:  #hitting up or down edge
            return True
        
        return False
    
    def start_thread(self):
        self.th.start()
        return self.th

