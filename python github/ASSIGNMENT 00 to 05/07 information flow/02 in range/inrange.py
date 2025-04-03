def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low."""
    return low <= n <= high

# Example calls to test the function
print(in_range(5, 1, 10))    # True (5 is between 1 and 10)
print(in_range(12, 1, 10))   # False (12 is outside 1-10)
print(in_range(0, -5, 5))    # True (0 is between -5 and 5)
print(in_range(10, 10, 20))  # True (10 is included in 10-20)