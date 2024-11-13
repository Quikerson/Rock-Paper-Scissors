import random
import math

def play():
    user = input("Whats your choice? 'rock', 'paper', 'scissors', 'lizard' or 'spock'\n")
    user = user.lower()

    computer = random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])

    if user == computer:
        return (0, user, computer)
    

    #r > s, s > p, p > r
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, opponent):
    #Return true if the player beats the oponent
    #Winning conditions r > sc, r > l, l > sp, l > p, sp > r, sp > sc, sc > p, sc > l, p > r, p > sp
    if (player == 'rock' and opponent == 'scissors') or (player == 'rock' and opponent == 'lizard') or (player == 'lizard' and opponent == 'spock') or (player == 'lizard' and opponent == 'paper') or (player == 'spock' and opponent == 'rock') or (player == 'spock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') or (player == 'scissors' and opponent == 'lizard') or (player == 'paper' and opponent == 'rock') or (player == 'paper' and opponent == 'spock'):
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
            print("----------------------")
            print('It is a tie, You and the computer have both chosen {}. \n'.format(user))
            print(f"Player: {player_wins}, Computer: {computer_wins}")
            if player_wins < computer_wins:
                print("Don't give up, you can do it")
            elif player_wins > computer_wins:
                print("You're doing it pretty well")
            else:
                print("Maybe it's time to take the adventage")
            print("----------------------")
        
        #You win
        elif result == 1:
            player_wins += 1
            print("----------------------")
            print('You chose {}, and the computer chose {}, You won.\n'.format(user, computer))
            print(f"Player: {player_wins}, Computer: {computer_wins}")
            if player_wins < computer_wins:
                print("Don't give up, you can do it")
            elif player_wins > computer_wins:
                print("You're doing it pretty well")
            else:
                print("Maybe it's time to take the adventage")
            print("----------------------")
        #Computer wins
        else:
            computer_wins += 1
            print("----------------------")
            print('You chose {}, and the computer chose {}, You lost :(\n'.format(user, computer))
            print(f"Player: {player_wins}, Computer: {computer_wins}")
            if player_wins < computer_wins:
                print("Don't give up, you can do it")
            elif player_wins > computer_wins:
                print("You're doing it pretty well")
            else:
                print("Maybe it's time to take the adventage")
            print("----------------------")

    if player_wins > computer_wins:
        print("----------------------")
        print('You have won the best out of {} games! What a champ!!!'.format(n))
        print("----------------------")
    else:
        print("----------------------")
        print('The computer has won the best out of {} games, better luck next time :('.format(n))
        print("----------------------")

if __name__ == '__main__':
    play_best_of(3) #2 wins
