# A list makes a battleship board from A1 to E5 but skips C3

# Execution point

board = [f'{alph}{num}' for alph in ['A', 'B', 'C', 'D', 'E'] for num in range(1, 6, 1) if (f'{alph}{num}' != 'C3')]
# Breakdown: 
# - f'{alph}{num}' implies the string of the position 
# - - for alph in ['A', 'B', 'C', 'D', 'E'] for num in range(1, 6, 1) gives a concatenated string A1 A2 etc 
# - if (f'{alph}{num}' != 'C3') to remove C3 from the list
print(board)