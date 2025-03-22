import os

# Create a dictionary for the spots on the board
spots = {
    1: '1', 2: '2', 3: '3',
    4: '4', 5: '5', 6: '6',
    7: '7', 8: '8', 9: '9'
}

# This variable keeps track of whether the game is still playing
playing = True
turn = 0

# Function to print the board
def draw_board():
    print(f"|{spots[1]}|{spots[2]}|{spots[3]}|")
    print(f"|{spots[4]}|{spots[5]}|{spots[6]}|")
    print(f"|{spots[7]}|{spots[8]}|{spots[9]}|")

# Function to determine which player's turn it is
def get_player_turn():
    if turn % 2 == 0:
        return 'X'  # Player 1 (X)
    else:
        return 'O'  # Player 2 (O)

# Function to check if someone has won
def check_for_win():
    # Check horizontal lines
    if (spots[1] == spots[2] == spots[3]) or (spots[4] == spots[5] == spots[6]) or (spots[7] == spots[8] == spots[9]):
        return True
    # Check vertical lines
    if (spots[1] == spots[4] == spots[7]) or (spots[2] == spots[5] == spots[8]) or (spots[3] == spots[6] == spots[9]):
        return True
    # Check diagonal lines
    if (spots[1] == spots[5] == spots[9]) or (spots[3] == spots[5] == spots[7]):
        return True
    return False

# Start the game loop
while playing:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    draw_board()  # Print the current board

    print(f"Player {get_player_turn()}'s turn: Pick a spot or press 'q' to quit")

    choice = input("Enter a spot (1-9): ")

    if choice == 'q':
        playing = False  # End the game if the player presses 'q'
    elif choice.isdigit() and int(choice) in spots:  # Check if input is a valid number
        spot = int(choice)
        # If the spot is available, mark it
        if spots[spot] not in ['X', 'O']:
            spots[spot] = get_player_turn()
            turn += 1
        else:
            print("That spot is already taken, try again.")
    else:
        print("Invalid input, please choose a number between 1-9.")

    # Check if the game has a winner
    if check_for_win():
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_board()
        print(f"Player {get_player_turn()} wins!")
        playing = False  # End the game when someone wins

    # If all spots are filled and there's no winner, it's a tie
    if turn >= 9:
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_board()
        print("It's a tie!")
        playing = False

print("Thanks for playing!")
