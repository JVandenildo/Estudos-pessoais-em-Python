# direct recursive
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


userNumber = int(input("Enter a number: "))
print(factorial(userNumber))


# indirect recursive
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return is_odd(x - 1)


def is_odd(x):
    return is_even(x)


print(is_odd(17))
print(is_even(23))
