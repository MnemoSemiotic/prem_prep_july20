def factorial(n):
    if n < 0:
        return None

    prod = 1

    for i in range(2, n+1):
        prod *= i
    
    return prod

print(factorial(5))