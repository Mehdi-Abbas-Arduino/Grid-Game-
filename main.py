import random

rows, cols = 5, 5
Grid = [['0' for _ in range(cols)] for _ in range(rows)]

def place_X(grid):  
    while True:
        # Checks it's not on top left corner of page  
        x = random.randint(0, rows - 1)
        y = random.randint(0, cols - 1)
        if x != 0 or y != 0:
            grid[x][y] = 'X'
            break
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 'X':
                grid[i][j] = '0'
    return x, y 

def display_grid(grid, player_pos):
    for i in range(rows):
        for j in range(cols):
            if [i, j] == player_pos:
                print("P", end=" ")  # Display the player position
            else:
                print(grid[i][j], end=" ")
        print()

x_pos, y_pos = place_X(Grid)

# Player's starting position
player_pos = [0, 0]
moves_remaining = 10

print("Welcome to the game! You have 10 moves to find the secret cell.")

def give_hint(player_pos, secret_pos):
    player_x, player_y = player_pos
    secret_x, secret_y = secret_pos
    # Calculate the difference in position
    x_diff = secret_x - player_x
    y_diff = secret_y - player_y
    # Provide directional hints
    if x_diff == 0 and y_diff > 0:
        print("A little bit right.")
    elif x_diff == 0 and y_diff < 0:
        print("A little bit left.")
    elif x_diff > 0 and y_diff == 0:
        print("A little bit down.")
    elif x_diff < 0 and y_diff == 0:
        print("A little bit up.")
    elif x_diff > 0 and y_diff > 0:
        print("Down-right.")
    elif x_diff > 0 and y_diff < 0:
        print("Down-left.")
    elif x_diff < 0 and y_diff > 0:
        print("Up-right.")
    elif x_diff < 0 and y_diff < 0:
        print("Up-left.")

while moves_remaining > 0:
    print(f"\nMoves remaining: {moves_remaining}")
    display_grid(Grid, player_pos)  # Display the grid with the player position
    direction = input("Enter move (left/right/up/down): ").lower()
    x, y = player_pos
    if direction == 'left':
        y -= 1
    elif direction == 'right':
        y += 1
    elif direction == 'up':
        x -= 1
    elif direction == 'down':
        x += 1
    else:
        print("Invalid move. Please enter left, right, up, or down.")
        continue
    # Ensure the player stays within the grid boundaries
    if x < 0 or x >= rows or y < 0 or y >= cols:
        print("Move out of bounds. Try a different direction.")
        continue
    player_pos = [x, y]
    moves_remaining -= 1
    
    # Give a hint after each move
    give_hint(player_pos, (x_pos, y_pos))

    # Check if the player has found the 'X'
    if Grid[x][y] == 'X':
        display_grid(Grid, player_pos)  # Display the final board with the player at 'X'
        print("You Win! You found the secret cell.")
        break
else:
    display_grid(Grid, player_pos)  # Display the final board when moves are over
    print("You Lose! You couldn't find the secret cell.")
