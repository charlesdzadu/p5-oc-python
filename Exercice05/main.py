"""Module providing utility functions for mathematical operations and text processing."""


def calculate_average(numbers):
    """Calculate the arithmetic mean of a list of numbers.

    Args:
        numbers (list): A list of numbers (int or float)

    Returns:
        float: The arithmetic mean of the numbers
        
    Raises:
        ValueError: If the input list is empty
        TypeError: If the list contains non-numeric values
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)


def count_words(text):
    """Count the number of words in a given text.

    Args:
        text (str): The input text to analyze

    Returns:
        int: The number of words in the text
        
    Note:
        Words are considered to be separated by whitespace
    """
    return len(text.split())


def find_max_min(numbers):
    """Find the maximum and minimum values in a list of numbers.

    Args:
        numbers (list): A list of numbers to analyze

    Returns:
        tuple: A pair of (maximum, minimum) values from the list
        
    Raises:
        ValueError: If the input list is empty
    """
    if not numbers:
        raise ValueError("Cannot find max and min of empty list")
    return (max(numbers), min(numbers))


def reverse_string(text):
    """Reverse the characters in a string.

    Args:
        text (str): The input string to reverse

    Returns:
        str: The reversed string
    """
    return text[::-1]


def main():
    """Demonstrate the usage of the utility functions."""
    # Example usage of calculate_average
    numbers = [1, 2, 3, 4, 5]
    print(f"Average: {calculate_average(numbers)}")

    # Example usage of count_words
    text = "This is a sample text"
    print(f"Word count: {count_words(text)}")

    # Example usage of find_max_min
    print(f"Max and min: {find_max_min(numbers)}")

    # Example usage of reverse_string
    print(f"Reversed text: {reverse_string(text)}")


if __name__ == "__main__":
    main()
