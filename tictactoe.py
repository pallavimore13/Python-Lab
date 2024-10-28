import random

# Function to display the game board
def display(size, gamestate):
    rows = size * 2 + 1
    columns = size * 2 + 1
    
    for i in range(rows):
        for j in range(columns):
            if i % 2 == 0 and j % 2 == 0:
                print(" ", end="")
            elif i % 2 == 0:
                print("_", end="")
            elif j % 2 == 0:
                print("|", end="")
            else:
                row, col = i // 2 + 1, j // 2 + 1
                print(gamestate[row][col] if gamestate[row][col] != '' else " ", end="")
        print()

# Function to handle game logic
def initialization():
    # Initialize the game state with an empty 3x3 grid
    gamestate = {
        1: {1: '', 2: '', 3: ''},
        2: {1: '', 2: '', 3: ''},
        3: {1: '', 2: '', 3: ''}
    }

    # Get player names
    player1 = input("Enter the name of player 1: ")
    player2 = input("Enter the name of player 2: ")

    # Randomly assign 'X' or 'O' to the players
    players = {player1: random.choice(['X', 'O'])}
    players[player2] = 'O' if players[player1] == 'X' else 'X'

    # Randomly select who will start first
    current_player = random.choice([player1, player2])

  
    for turn in range(9):
        display(3, gamestate)
        print(f"{current_player}'s turn ({players[current_player]}).")
        
        # Get the player's move
        try:
            move = input("Enter your move (row and column, e.g., '1 2'): ")
            row, col = map(int, move.split())
        except ValueError:
            print("Invalid input! Please enter row and column as numbers.")
            continue

        # Check if the move is valid (within the grid)
        if row not in range(1, 4) or col not in range(1, 4):
            print("Invalid position! Please enter numbers between 1 and 3.")
            continue

        # Check if the cell is already occupied
        if gamestate[row][col] != '':
            print("That position is already taken. Please choose another.")
            continue

        # Update the game state with the current player's move
        gamestate[row][col] = players[current_player]

        # Check for a winner after the move (no separate function, inline check)
        # Check rows
        for i in range(1, 4):
            if gamestate[i][1] == gamestate[i][2] == gamestate[i][3] != '':
                display(3, gamestate)
                print(f"Congratulations {current_player}! You win!")
                return

        # Check columns
        for i in range(1, 4):
            if gamestate[1][i] == gamestate[2][i] == gamestate[3][i] != '':
                display(3, gamestate)
                print(f"Congratulations {current_player}! You win!")
                return

        # Switch players
        current_player = player1 if current_player == player2 else player2

    # If all turns are completed and no winner, it's a draw
    display(3, gamestate)
    print("It's a draw!")

if __name__ == "__main__":
    initialization()

