import config
class Score:
    def __init__(self):
        self.left = 0
        self.right = 0
    
    #change score
    def inc_score(self,side):
        if side:
            self.right += 1
            print("Right ++")
        else:
            self.left += 1
            print("Left ++")
    #return list of score
    def get_score(self):
        return [left,right]
    
    def is_over(self):
        return self.left == config.MAX_POINT or self.right == config.MAX_POINT    