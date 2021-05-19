#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Author: James Carter Garrett

# Creates a blank game board
def create_board():
  board = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]
  return board

# Display the game board
def display_board(gameboard):
  counter = 0
  
  for rows in gameboard:
    pos = 0
    for position in rows:
      # First Row
      if counter == 0:
        if position == 0:
          print("_ | ", end='')
          pos += 1
        
        elif position == 1:
          print("X | ", end='')
          pos += 1
        
        else:
          print("O | ", end='')
          pos += 1
        
        if pos == 4:
          print("\n---------------")
      
      # Second Row
      elif counter == 1:
        if position == 0:
          print("_ | ", end='')
          pos += 1
        
        elif position == 1:
          print("X | ", end='')
          pos += 1
        
        else:
          print("O | ", end='')
          pos += 1
        
        if pos == 4:
          print("\n---------------")
      
      # Third Row
      elif counter == 2:
        if position == 0:
          print("_ | ", end='')
          pos += 1
        
        elif position == 1:
          print("X | ", end='')
          pos += 1
        
        else:
          print("O | ", end='')
          pos += 1
        
        if pos == 4:
          print("\n---------------")
      
      # Fourth Row
      else:
        if position == 0:
          print("_ | ", end='')
          pos += 1
        
        elif position == 1:
          print("X | ", end='')
          pos += 1
        
        else:
          print("O | ", end='')
          pos += 1
        
        if pos == 4:
          print("\n---------------")
    
    counter += 1

# Check for winning -
def check_winner(gameboard, currentMoves):
  noWinner = " "
  xWins = "X"
  oWins = "O"
  
  # If there have been less than 7 moves made, there can't be a winner
  if currentMoves < 7:
    return noWinner
  
  # If there have been 7 or more, continue checking
  else:

    # Checking each row for a winner
    for rows in gameboard:
      if rows == [1, 1, 1, 1]:
        return xWins
      elif rows == [2, 2, 2, 2]:
        return oWins
      else:
        continue
    
    # Checking each column for a winner
    for columns in range(0, 3):
      
      # Checking for 4 X's in each column
      if gameboard[0][columns] == 1:
        if gameboard[1][columns] == 1:
          if gameboard[2][columns] == 1:
            if gameboard[3][columns] == 1:
              return xWins

      # Checking for 4 O's in each column
      if gameboard[0][columns] == 2:
        if gameboard[1][columns] == 2:
          if gameboard[2][columns] == 2:
            if gameboard[3][columns] == 2:
              return oWins
    
    # Checking diagonal

    # Top Left -> Bottom Right
    if gameboard[0][0] == 1:
      if gameboard[1][1] == 1:
        if gameboard[2][2] == 1:
          if gameboard[3][3] == 1:
            return xWins
    
    if gameboard[0][0] == 2:
      if gameboard[1][1] == 2:
        if gameboard[2][2] == 2:
          if gameboard[3][3] == 2:
            return oWins
    
    # Bottom Left -> Top Right
    if gameboard[3][0] == 1:
      if gameboard[2][1] == 1:
        if gameboard[1][2] == 1:
          if gameboard[0][3] == 1:
            return xWins
    
    if gameboard[3][0] == 2:
      if gameboard[2][1] == 2:
        if gameboard[1][2] == 2:
          if gameboard[0][3] == 2:
            return oWins
    
    # If there's no winning combination
    else:
      return noWinner
      

# Runs the game
player1 = input("Enter player one's name: ")
player2 = input("Enter player two's name: ")
print()

p1Wins = 0
p2Wins = 0 
movesMade = 0
keepRunning = True

while (keepRunning == True):
  newBoard = create_board()

  while ((check_winner(newBoard, movesMade) == " " and movesMade < 16) or (check_winner(newBoard, movesMade) == None and movesMade < 16)):
    display_board(newBoard)
    inputChecker = True

    while (inputChecker == True):
      try:
        userRow = int (input("Enter the row you would like to choose (1-4): "))
        if (userRow >= 1 and userRow <= 4):
          inputChecker = False
        else:
          print("Invalid number, must be either 1, 2, 3, or 4. Try again.")
      except:
        print("Invalid input. Try again.")
    
    inputChecker = True

    while (inputChecker == True):
      try:
        userColumn = int (input("Enter the column you would like to choose (1-4): "))
        if (userColumn >= 1 and userColumn <= 4):
          inputChecker = False
        else:
          print("Invalid number, must be either 1, 2, 3, or 4. Try again.")
      except:
        print("Invalid input. Try again.")

    if ((movesMade + 1) % 2) == 0:
      if (newBoard[(userRow - 1)][(userColumn - 1)] == 0):
        newBoard[(userRow - 1)][(userColumn - 1)] = 2
        movesMade += 1
      else:
        print("That space is not empty. Choose another space.")
    
    else:
      if (newBoard[(userRow - 1)][(userColumn - 1)] == 0):
        newBoard[(userRow - 1)][(userColumn - 1)] = 1
        movesMade += 1
      else:
        print("That space is not empty. Choose another space.")

  if (check_winner(newBoard, movesMade) == "X"):
    p1Wins += 1
  
  if (check_winner(newBoard, movesMade) == "O"):
    p2Wins += 1
  
  display_board(newBoard)
  inputChecker = True
  
  while (inputChecker == True):
    try:
      userAns = input("Would you like to play again? (yes/no): ")

      if (userAns.upper() == "YES"):
        inputChecker = False
      elif (userAns.upper() == "NO"):
        inputChecker = False
        keepRunning = False
      else:
        print("Invalid input, type either \"yes\" or \"no\". Try again.")
    except:
      print("Invalid input. Try again.")

print()
print("Wins for", player1, ":", p1Wins)
print("Wins for", player2, ":", p2Wins)

