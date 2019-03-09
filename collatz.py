def collatz(number):
    if number % 2 == 0:
        val = number // 2
    else:
        val = number * 3 + 1

    print(val)
    return val


result = 3

while result is not 1:
    result = collatz(result)
