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
    print(config.DIGITS[score.left],config.DIGITS[score.right])
    for x in range(config.GAME_SIZE[0]):
        for y in range(config.GAME_SIZE[1]):
            if x == 0 or x == config.GAME_SIZE[0] - 1:
                print("-", end = "")
                continue
            
            found = False
            for i in parts:
                ch = i.is_here([x,y])
                if ch is not None:
                    print(ch,end = "")
                    found = True
                    break

            if not found and (y == 0 or y == config.GAME_SIZE[1] - 1):
                print("| ", end = "")
            else:
                print("", end = " ")

        print()
    
            

def main():
    score = Score.Score()
    while not score.is_over():
        parts,threads= init_all(score)
        score_was_changed = False
        while threads[2].isAlive():#while the score is not changed
            stop = datetime.datetime.now() + datetime.timedelta(seconds = 2)                 
            
            while(datetime.datetime.now() < stop):
                pass
            
            
            update_screen(score,parts)
        score.inc_score(parts[2].loc != 0)
        update_screen(score,parts)
        parts[0].kill_thread()
        parts[1].kill_thread()




if __name__ == "__main__":
    main()