def display_board(board):
    print("\n")
    print("     |     |")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}")
    print("     |     |")
    print()

def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for combination in winning_combinations:
        if all(board[position] == player for position in combination):
            return True

    return False

def check_draw(board):
    return all(position in ["X", "O"] for position in board)

def play_game():
    board = [
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"
    ]
    current_player = "X"

    print("=" * 40)
    print("        TIC-TAC-TOE GAME")
    print("=" * 40)

    print("\nPlayer 1 : X")
    print("Player 2 : O")
    print("Select a position from 1 to 9.")

    while True:
        display_board(board)
        print(f"Player {current_player}'s turn")

        try:
            position = int(input("Enter position (1-9): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if position < 1 or position > 9:
            print("Please enter a number between 1 and 9.")
            continue

        index = position - 1

        if board[index] in ["X", "O"]:
            print("Position already occupied! Choose another position.")
            continue

        board[index] = current_player

        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            display_board(board)
            print("Game Draw!")
            break
        
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

play_game()