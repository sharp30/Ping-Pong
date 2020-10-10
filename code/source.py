#libraries
import datetime
import _thread 
from os import system
#classes
import Ball
import Player
import Score
import config


#initial game state
def init_all(score):
    right = Player.Player(True)
    left = Player.Player(False)
    parts = [right,left,Ball.Ball((right,left))]
    update_screen(score,parts)

    threads = [i.start_thread() for i in parts]
    return parts,threads

#update screen terminal
def update_screen(score,parts):
    system("cls")
    output = """"""
    #print(config.DIGITS[score.left],config.DIGITS[score.right]) //TODO: fix this printing
    print(" "*(config.GAME_SIZE[1]//2) + "%d - %d\n"%(score.left,score.right))
    output += '-'*config.GAME_SIZE[1] +"\n"
    
    for row in range(config.GAME_SIZE[0]):
        for col in range(config.GAME_SIZE[1]):
            found = False
            for i in parts:
                ch = i.is_here([row,col])
                if ch is not None:
                    output += ch
                    found = True
                    break
                
            if not found:
                if col == 0 or col == config.GAME_SIZE[1] - 1:
                    output+="|"
                else:
                    output += " "
        output += "\n"
    output += '-'*config.GAME_SIZE[1]

    print(output)

def main():
    score = Score.Score()
    while not score.is_over():
        parts,threads= init_all(score)
        score_was_changed = False
        while threads[2].isAlive():#while the score is not changed
            stop = datetime.datetime.now() + datetime.timedelta(seconds = config.GAME_DELAY)                 
            
            while(datetime.datetime.now() < stop):
                pass
            
            update_screen(score,parts)
        score.inc_score(parts[2].loc[1] == 0)
        update_screen(score,parts)
        parts[0].kill_thread()
        parts[1].kill_thread()



if __name__ == "__main__":
    main()