def caching_fibonacci():
    # Creating empty dictionary
    cache = {}
    # Creating internal function to calculate fibonacci numbers
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci


# Assigning function to new variable
fib = caching_fibonacci()


# Example
print(fib(10)) # 55
print(fib(15)) # 610
print(fib(25)) # 675025