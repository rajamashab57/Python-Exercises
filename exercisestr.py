
# abc : str = "Raja Mashab Turk"

# xyz = abc.upper()

# print(xyz)


# data = "2023-08-04"


# print(data.isalnum())

# print(data.isnumeric())

# tempelate : str = "The price of {} is {} dollars"


# print(tempelate.format("Apple","1.50"))

# def weird_check(n: int):
#     if n % 2 !=0:
#         print("Weird")
#     elif  2 <= n  <= 5:
#         print("Not Weird")
#     elif  6 <= n <= 20:
#         print("Weird")
#     elif n > 20 :
#      print("Not Weird")
# n: int = int(input("Enter your Numbers :"))
# weird_check(n)

# ==========================================================

# n = [0,1,2]


# for i in n:
#     square = i ** 2
#     print(square)

# Read the integer from standard input
n = int(input().strip())

# Initialize the variable to store the sum of squares


# Iterate through all non-negative integers less than n
for i in range(n):
    # Compute the square of i and add it to sum_squares
    sum_squares = i**2

# Print the total sum of squares
print(f"""Sum of squares:", {sum_squares}""")
