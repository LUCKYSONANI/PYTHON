def perfect_number(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
def perfect_numbers_between_1_and_500():
    perfect_numbers = []
    for num in range(1, 501):
        if perfect_number(num):
            perfect_numbers.append(num)
    
    return perfect_numbers
start = 1
end = 500
perfect_numbers = perfect_numbers_between_1_and_500()
print(f"Perfect numbers between {start} and {end}: {perfect_numbers}")
