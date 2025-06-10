def perfect_number(n):
    """Check if a number is a perfect number."""
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n