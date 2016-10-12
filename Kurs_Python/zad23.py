def factorial(n, acc=1):
    if n < 1:
        raise ArithmeticError("Foo")
    if n == 1:
        raise BaseException(acc)
    factorial(n-1, n*acc)

def fibonacci(n):
    # HOW?
    if n in [0, 1]:
        return 1
    return fibonacci(n-2) + fibonacci(n-2)
