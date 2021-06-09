# Author: Chitturi Sai Suman
# Date: 2021-06-01
# Created with LOVE


# Reads each text file present in the folder named Letters
# Hashes the contents as a key-value pair

from typing import Dict, List


def preProcess() -> Dict:
    # Dictionary for Key-Value pair
    chars = dict()

    for i in range(10):
        # ch takes values from [0-9]
        ch = str(i)
        with open("Letters/" + ch + ".txt", "r") as file:
            # Read the contents line by line
            lines = list(map(str, file.read().split("\n")))
            # Pop last newline character
            lines.pop()
            # Store it in Dictionary
            chars[ch] = lines

    for i in range(65, 91):
        # ch takes values from [A-Z]
        ch = chr(i)

        # Open the file associated with the Character
        with open("Letters/" + ch + ".txt", "r") as file:
            # Read the contents line by line
            lines = list(map(str, file.read().split("\n")))
            # Pop last newline character
            lines.pop()
            # Store it in Dictionary
            chars[ch] = lines

    for i in range(97, 123):
        # ch takes values from [a-z]
        ch = chr(i)

        # Open the file associated with the Character
        with open("Letters/" + ch + ".txt", "r") as file:
            # Read the contents line by line
            lines = list(map(str, file.read().split("\n")))
            # Pop last newline character
            lines.pop()
            # Store it in Dictionary
            chars[ch] = lines

    # Exclusive snippet for Space Character
    with open("Letters/space.txt", "r") as file:
        lines = list(map(str, file.read().split("\n")))
        lines.pop()
        chars[' '] = lines

    # Return the Dictionary
    return chars


# Concatenates two characters Horizontally

def concat(a: List, b: List) -> List:
    if len(a) == 0:
        return b
    m = len(a)
    new_matrix = []
    for i in range(m):
        new_matrix.append(a[i] + b[i])
    return new_matrix


# Utility Function to write the String to a file

def write(line: str, chars:dict) -> None:
    # Create matrix to store the formatted output
    base_matrix = []

    # Append the characters to the matrix
    for char in line:
        small_matrix = chars[char]
        base_matrix = concat(base_matrix, small_matrix)

    # Write the output to a file
    try:
        # If the file already exists
        # Append the string after a new line
        with open("Output.txt", "a") as file:
            file.write('\n'.join(base_matrix) + '\n')
    except:
        # If the file doesn't exists
        # Create the file and Write the string
        with open("Output.txt", "w") as file:
            file.write('\n'.join(base_matrix) + '\n')


# Main function to read input and call other utility functions
def main() -> None:
    # Preprocess the Formatted Letters
    chars = preProcess()
    
    n = int(input("Number of Lines: "))
    for i in range(n):
        line = input("Enter line: ")
        write(line, chars)
    
# Call main function
if __name__ == '__main__':
    main()