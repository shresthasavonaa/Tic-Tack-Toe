import random
import os.path
import json
random.seed()

board = [[' ' for j in range(3)] for i in range(3)]

def draw_board(board):
    # develop code to draw the board
    print(" ---+---+---")
    print(" | {} | {} | {} |".format(board[0][0], board[0][1], board[0][2]))
    print(" ---+---+---")
    print(" | {} | {} | {} |".format(board[1][0], board[1][1], board[1][2]))
    print(" ---+---+---")
    print(" | {} | {} | {} |".format(board[2][0], board[2][1], board[2][2]))
    print(" ---+---+---")
    print()

def welcome(board):
    # prints the welcome message
    # display the board by calling draw_board(board)
    print("Welcome to Tic Tac Toe!\n")
    draw_board(board)

def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board

def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    print("Your turn. Which cell would you like to place X in?")
    cell = input("Enter cell number (1-9): ")
    row = (int(cell) - 1) // 3
    col = (int(cell) - 1) % 3
    if board[row][col] == ' ':
        board[row][col] = 'X'
    else:
        print("Cell already occupied. Please choose another cell.")
        get_player_move(board)
    return row, col

def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            return row, col

def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    
    # Check for horizontal wins
    for row in board:
      if row == [mark, mark, mark]:
        return True
    
    # Check for vertical wins
    for col in range(3):
      if board[0][col] == mark and board[1][col] == mark and board[2][col] == mark:
        return True
  
    # Check for diagonal wins
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
      return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
      return True
  
    return False


def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark)
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    #repeat the loop
    board = initialise_board(board)
    draw_board(board)
    while True:
        #Player's turn
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            print("You win!!")
            return 1
        if check_for_draw(board):
            print("Draw game.")
            return 0

        #Computer's turn
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            print("Computer wins!!")
            return -1
        if check_for_draw(board):
            print("Draw game.")
            return 0

def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    choice = str(input("1 - Play the game, 2 - Save score in file 'leaderboard.txt', 3 - Load scores and display the leaderboard from the 'leaderboard.txt', q - Quit\nEnter your choice: "))
    return choice

def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    leaders = {}
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt") as f:
            leaders = json.load(f)
    return leaders

def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    player_name = input("Enter your name: ")
    leaders = load_scores()
    leaders[player_name] = score
    with open("leaderboard.txt", "w") as f:
        json.dump(leaders, f)
    return

def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    if len(leaders) > 0:
        print("Leaders:")
        for i, (player_name, score) in enumerate(leaders.items()):
            print(f"{i + 1}. {player_name}: {score}")
    else:
        print("No scores saved yet.")
