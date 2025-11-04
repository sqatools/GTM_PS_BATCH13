# Create a Python program that takes a list of numbers as input and returns a new list containing only the even numbers from the original list.
def filter_even_numbers(numbers):
    """Return a list of even numbers from the given list."""
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers
# Example usage:
input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(input_numbers)
print("Even numbers:", even_numbers)  # Output: Even numbers: [2, 4, 6, 8, 10]