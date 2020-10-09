class Score:
    def __init__(self):
        self.left = 0
        self.right = 0
    
    #change score
    def inc_score(self,side):
        if side:
            self.right += 1
        else:
            self.left += 1
    #return list of score
    def get_score(self):
        return [left,right]
    