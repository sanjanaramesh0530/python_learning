def is_prime(num):
    """Checks if a single number is prime."""
    if num <= 1:
        return False
    # Check divisibility up to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def primes_between(start, end):
    """Returns a list of prime numbers between start and end (exclusive)."""
    # Use start + 1 to exclude the starting prime itself
    return [num for num in range(start + 1, end) if is_prime(num)]
lower_prime = 9
upper_prime = 20

# Get the list of primes in between
result = primes_between(lower_prime, upper_prime)

# Display the output
print(f"Prime numbers between {lower_prime} and {upper_prime}:")
print(result)

