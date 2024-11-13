import random
import math

def play():
    user = input("Whats your choice? 'r' for rock, 'p' for paper and 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)
    

    #r > s, s > p, p > r
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, opponent):
    #Return true if the player beats the oponent
    #Winning conditions r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    #Play against the computer until someone wins best of (n) games
    #To win, you must win ceilin(n/2) games (in 2/3, 3/5, 5/7)
    player_wins = 0
    computer_wins = 0
    wins_necesary = math.ceil(n/2)
    while player_wins < wins_necesary and computer_wins < wins_necesary:
        result, user, computer = play()
        #tie
        if result == 0:
            print('It is a tie, You and the computer have both chosen {}. \n'.format(user))
        #You win
        elif result == 1:
            player_wins += 1
            print('You chose {}, and the computer chose {}, You won.\n'.format(user, computer))
        #Computer wins
        else:
            computer_wins += 1
            print('You chose {}, and the computer chose {}, You lost :(\n'.format(user, computer))

    if player_wins > computer_wins:
        print('You have won the best out of {} games! What a champ!!!'.format(n))
    else:
        print('The computer has won the best out of {} games, better luck next time :('.format(n))

if __name__ == '__main__':
    play_best_of(3) #2 wins
