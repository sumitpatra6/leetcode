def perfect_sqquares(number):
    counter = 0
    while number > 0:
        for i in reversed(range(1, number+1)):
            if (i ** 0.5) % 1 == 0:
                print(i)
                number = number - i
                counter += 1
                break
    return counter
print(perfect_sqquares(12))