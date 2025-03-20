#Write a Python program that takes a list of numbers as input and prints the largest number in the list.

def find_largest_number(numbers):
    # Use the max() function to find the largest number in the list
    largest_number = max(numbers)
    return largest_number

# Example usage
numbers = [10, 20, 4, 45, 99]
print(find_largest_number(numbers))