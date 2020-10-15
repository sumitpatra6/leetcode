def tripie_steps_recursive(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return tripie_steps_recursive(n-1) + tripie_steps_recursive(n-2) + tripie_steps_recursive(n-3)


def tripie_steps_dynamic(n):
    result = [0]*(n+1)
    result[0] = 1
    steps = [1,2,3]
    for i in range(1, n+1):
        for j in steps:
            if i - j >= 0:
                result[i] += result[i-j]
    print(result)   
    return result

print(tripie_steps_recursive(4))
print(tripie_steps_dynamic(4))