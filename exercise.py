def sum_with_while(start, end):
    """
    Calculate the sum of all numbers between start and end (inclusive) using a while loop.
    """
    count = start + 1
    sum = start + end
    while count > start and count < end:
        sum += count
        count += 1
    return sum

def count_vowels_in_string(input_string):
    """
    Count the number of vowels in a given string using a for loop.
    """
    vowels = ["A", "E", "I", "O", "U"]
    count = 0
    for l in range(len(input_string)):
        if input_string[l].upper() in vowels:
            count += 1
    return count


def filter_numbers(numbers):
    """
    Filter a list of numbers based on specific conditions using a for loop and conditionals.
    """
    new_list = {"positive": [],
                "negative": [],
                "even": [],
                "odd": []}
    for n in numbers:
        if n > 0:
            new_list["positive"].append(n)
            if n % 2 == 0:
                new_list["even"].append(n)
            elif n % 2 != 0:
                new_list["odd"].append(n)

        elif n < 0:
            new_list["negative"].append(n)
            if n % 2 == 0:
                new_list["even"].append(n)
            elif n % 2 != 0:
                new_list["odd"].append(n)
        else:
            new_list["even"].append(n)
    return new_list
    

def fibonacci_sequence(n):
    """
    Generate Fibonacci sequence up to n terms using a while loop.
    """
    fibo = [0, 1]
    count = 1
    while count < n:
        fibo.append(fibo[count - 1] + fibo[count])
        count += 1
    return fibo

def pascals_triangle(rows):
    """
    Generate Pascal's Triangle up to a given number of rows.
    """
    

def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solve the Tower of Hanoi problem recursively.
    """
    pass

def find_dna_sequence(dna, sequence):
    """
    Find the first occurrence of a DNA subsequence within a larger DNA string.
    """
    pass

def is_palindrome(input_string):
    """
    Check if a given string is a palindrome (ignoring spaces, capitalization, and punctuation).
    """
    pass

def generate_permutations(input_string):
    """
    Return all possible permutations of a given string.
    """
    pass

def is_valid_sudoku(board):
    """
    Validate a given 9x9 Sudoku board.
    """
    pass

def solve_n_queens(n):
    """
    Find all possible solutions to the N-Queens problem.
    """
    pass

def longest_common_subsequence(str1, str2):
    """
    Find the length of the longest subsequence common to both strings.
    """
    pass

if __name__ == "__main__":
    pass
