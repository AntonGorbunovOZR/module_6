def is_prime(func):
    def wrapper(*args):
        d = func(*args)
        k = 0
        for i in range(2, d // 2 + 1):
            if (d % i == 0):
                k = k + 1
        if (k <= 0):
            return ("Простое")
        else:
            return ("Составное")
    return wrapper
@is_prime
def sum_three(*num):
    f = sum(num)
    print(f)
    return f
result = sum_three(2, 3, 6)
print(result)