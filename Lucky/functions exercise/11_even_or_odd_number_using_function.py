def iseven(n):
    if n % 2 == 0:
        return True
    else:
        return False
def even_numbers_between_1_and_100():
    even_numbers = []
    for num in range(1, 101):
        if iseven(num):
            even_numbers.append(num)
    
    return even_numbers
start = 1
end = 100
even_numbers = even_numbers_between_1_and_100()
print(f"Even numbers between {start} and {end}: {even_numbers}")
def isodd(n):
    if n % 2 != 0:
        return True
    else:
        return False
def odd_numbers_between_1_and_100():
    odd_numbers = []
    for num in range(1, 101):
        if isodd(num):
            odd_numbers.append(num)
    
    return odd_numbers
start = 1
end = 100
odd_numbers = odd_numbers_between_1_and_100()
print(f"Odd numbers between {start} and {end}: {odd_numbers}")
