


# mynumber : list = [1,3,2,5,3]
# mynumber.reverse()
# print(mynumber)


# n : int = 35231

# digit_list =  [int(digit) for digit in str(n)]
# digit_list.reverse()
# print(digit_list)



# def atm_machine(n:str):
#     if n == "1234":
#         print("true")
#     elif  n == "12345":
#         print("false")
#     elif n == "a1234":
#         print("false")

# n : str = str(input("Enter the Numbers :"))
# atm_machine(n)

# def is_valid_pin(pin:str)-> bool:
#     return len(pin)  in [4,6] and pin.isdigit()


# print(is_valid_pin("1234"))
# print(is_valid_pin("123345"))
# print(is_valid_pin("a234"))
# print(is_valid_pin("123456"))
# print(is_valid_pin("123456"))






# squares = [x**2 for x in range(11)]

# print(type(squares))

# [expression for item in iterable]


# squares = [x**2 for x in range(10)]

# print(squares)

# Problem 1: Square Numbers
# Task: Create a list of squares of numbers from 1 to 10.

# squareNumbers = [x**2 for x in range(1,11)]

# print(squareNumbers)

# ==========================================================================================
# difference between the is and in is it is used for the comparison variables check the variables are the same
# object or not and in variables are used the variables are use the to check inside the it is or not
# n : list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squareNumbers = [n for n in  x if n %2 == 0]

# print(squareNumbers)



# ==================================================================

# Problem 3: Lengths of Words
# Task: Given a list of words, create a new list containing the lengths of those words.

# Input: ["apple", "banana", "cherry", "date"]

# Example Output: [5, 6, 6, 4]


# input = ["apple", "banana", "cherry", "date"]


# check_input = [len(i) for i in  ["apple", "banana", "cherry", "date"]]

# print(check_input)


# Problem 4: Capitalize Words
# Task: Given a list of words, create a new list with each word capitalized.

# Input: ["hello", "world", "python"]

# Example Output: ["Hello", "World", "Python"]


# Input: list = ["hello", "world", "python"]


# output = [i.capitalize() for i in Input]


# print(output)

# ======================================================

# Problem 5: Filter Words Containing 'a'
# Task: Given a list of words, create a new list containing only the words that have the letter 'a' in them.

# Input: ["apple", "banana", "cherry", "date", "fig", "grape"]


# input = ["apple", "banana", "cherry", "date", "fig", "grape"]

# output = [i for i in input  if 'a' in i]

# print(output)

# Problem 7: Convert Strings to Integers
# Task: Given a list of strings representing numbers, create a new list of integers.

# Input = ["1", "2", "3", "4", "5"]

# output = [int(i) for i in Input]

# print(output)

# ================================================

# filter positive numbers 

# Task: Given a list of numbers, create a new list containing only the positive numbers.

# Input: [-1, 2, -3, 4, -5, 6]

# Example Output: [2, 4, 6]

# values = [-1, 2, -3, 4, -5, 6]

# output = [i for i in  values if i > 0]

# print(output)

# cartesian_product = [(x, y) for x in ["A", "B"] for y in [1, 2, 3]]
# print(cartesian_product)

