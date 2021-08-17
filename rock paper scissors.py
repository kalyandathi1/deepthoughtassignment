#import the library function "random" so that you can use it for computer 
#choice 
#contributed by Kalyan Dathi
import random 

#define main 
def main(): 
    #assign win, lose, and tie to zero for tallying
    win = 0 
    lose = 0 
    tie = 0 

    #control loop with 'y' variable 
    play_again = 'y' 

    #start the game 
    while play_again == 'y': 
        #make a welcome message and give directions 
        print('Prepare to battle in a game of paper, rock, scissors!') 
        print('Please input the correct number according') 
        print('to the object you want to choose.') 

        #Get the player and computers choices and 
        #assign them to variables 
        computer_choice = get_computer_choice() 
        player_choice = get_player_choice() 

        #print choices 
        print('Computer chose', computer_choice, '.') 
        print('You chose', player_choice, '.') 

        #determine who won 
        winner_result(computer_choice, player_choice) 

        #ask the user if they want to play again 
        play_again = input("Play again? Enter 'y' for yes or 'n' for no. ") 

    #print results 
    print('Your total wins are', win, '.') 
    print('Your total losses are', lose, '.') 
    print('Your total ties are', tie, '.') 

#define computer choice 
def get_computer_choice(): 
    #use imported random function from library 
    choice = random.randint(1,3) 

    #assign what the computer chose to rock, paper, or scissors 
    if choice == 1: 
        choice = 'ROCK' 
    elif choice == 2: 
        choice = 'PAPER' 
    else: 
        choice = 'SCISSORS' 

    #return value 
    return choice 

#define player choice 
def get_player_choice(): 
    #assign input to variable by prompting user 
    choice = int(input("Select rock(1), paper(2), or scissors(3): ")) 

    #Detect invalid entry
    while choice != 1 and choice != 2 and choice != 3: 
        print('The valid numbers are rock(type in 1), paper(type in 2),') 
        print('or scissors(type in 3).') 
        choice = int(input('Enter a valid number please: ')) 

    #assign what the player chose based on entry 
    if choice == 1: 
        choice = 'ROCK' 
    elif choice == 2: 
        choice = 'PAPER' 
    else: 
        choice = 'SCISSORS' 

    #return value 
    return choice 

#determine the winner from the variables 
def winner_result(computer_choice, player_choice): 
    #if its a tie, add 1 to tie variable and display message 
    if computer_choice == player_choice:
        result = 'tie'
        print("It's a tie!")

    #if its a win, add to win tally and display message 
    elif computer_choice == 'SCISSORS' and player_choice == 'ROCK':
        result = 'win'
        print('ROCK crushes SCISSORS! You win!')
    elif computer_choice == 'PAPER' and player_choice == 'SCISSORS': 
        result = 'win'
        print('SCISSORS cut PAPER! You win!')
    elif computer_choice == 'ROCK' and player_choice == 'PAPER': 
        result = 'win'
        print('PAPER covers ROCK! You win!')

    #if it does not match any of the win criteria then add 1 to lose and 
    #display lose message 
    else: 
        result = 'lose'
        print('You lose!')

def result(winner_result,player_choice, computer_choice):

    # accumulate the appropriate winner of game total
    if result == 'win':
        win += 1
    elif result == 'lose':
        lose += 1
    else:
        tie += 1
    return result

main() 
