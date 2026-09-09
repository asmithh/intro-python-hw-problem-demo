# Get player names
p1_name = input("What is player 1's name? ")
p2_name = input("What is player 2's name? ")

# Initialize scores
p1_score = 0
p2_score = 0

def validate_input(p_choice, p_name):
    """
    Make sure the input is one of "rock", "paper", or "scissors".
    Print out an error message if not.

    Inputs:
      p_choice: string; hopefully one of {rock, paper, scissors}.
      p_name: string; name of the player who played p_choice.

    Outputs:
      Boolean indicating whether p_choice was valid.
    """
    if p_choice != "rock" and p_choice != "scissors" and p_choice != "paper":
        print(f'{p_name} did not make a valid move!')
        return False
    else:
        return True
    
def play_rock_paper_scissors(p1_name, p2_name):
    """
    Main gameplay loop for a single game of rock, paper, scissors.

    Inputs:
      p1_name: string; name of player 1
      p2_name: string; name of player 2
    
    Returns: 
      a tuple with 2 integer values, each of which can either be 0 or 1. 
      a 1 at index 0 indicates that player 1 won, and a 1 at index 1 indicates player 2 won.
      there cannot be two 1s in the tuple, but there can be 2 0s if there was a tie.  
    """
    p1_choice = input("What does player 1 play? ")
    p2_choice = input("What does player 2 play? ")

    p1_valid = validate_input(p1_choice, p1_name)
    p2_valid = validate_input(p2_choice, p2_name)

    if p1_valid + p2_valid == 0:
        print(f"Both {p1_name} and {p2_name} made invalid moves, so nobody wins!")
        return 0, 0
    elif p1_valid == 0:
        print(f"f{p1_name} made an invalid move, so {p2_name} wins!")
        return 0, 1
    elif p2_valid == 0:
        print(f"f{p2_name} made an invalid move, so {p1_name} wins!")
        return 1, 0

    if p1_choice == p2_choice:
        print(f"{p1_name} and {p2_name} both played {p1_choice}, so nobody wins!")
        return 0, 0
    elif p1_choice == 'rock':
        if p2_choice == 'scissors':
            print(f"{p1_name} wins! Rock crushes scissors!")
            return 1, 0
        elif p2_choice == 'paper':
            print(f"{p2_name} wins! Paper covers rock!")
            return 0, 1
    elif p1_choice == 'paper':
        if p2_choice == 'rock':
            print(f"{p1_name} wins! Paper covers rock!")
            return 1, 0
        elif p2_choice == 'scissors':
            print(f"{p2_name} wins! Scissors cut paper!")
            return 0, 1
    elif p1_choice == 'scissors':
        if p2_choice == 'rock':
            print(f"{p2_name} wins! Rock crushes scissors!")
            return 0, 1
        elif p2_choice == 'paper':
            print(f"{p1_name} wins! Scissors cut paper!")
            return 1, 0

# Run the main gameplay loop 3 times.
p1_update, p2_update = play_rock_paper_scissors(p1_name, p2_name)
p1_score += p1_update
p2_score += p2_update
p1_update, p2_update = play_rock_paper_scissors(p1_name, p2_name)
p1_score += p1_update
p2_score += p2_update
p1_update, p2_update = play_rock_paper_scissors(p1_name, p2_name)
p1_score += p1_update
p2_score += p2_update

# Announce final scores
print(f"{p1_name} has a score of {p1_score}, and {p2_name} has a score of {p2_score}.")

# Determine a winner
if p2_score == p1_score:
    print(f"{p1_name} and {p2_name} tie!")
elif p2_score > p1_score:
    print(f"{p2_name} wins!")
else:
    print(f"{p1_name} wins!")

