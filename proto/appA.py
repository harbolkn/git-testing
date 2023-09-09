import random

"""
Use to generate the sum of 5 random numbers squares
"""


def generate_random_numbers(n):
    return [random.randint(1, 100) for _ in range(n)]


def main():
    numbers = generate_random_numbers(5)
    squared_numbers = [num ** 2 for num in numbers]
    sum_of_squares = sum(squared_numbers)
    return sum_of_squares


if __name__ == "__main__":
    print(main())
